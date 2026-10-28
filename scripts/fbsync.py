#!/usr/bin/env python3
"""臉書同步輔助程式（規格見 src/content/_sync/同步說明.md）

  import --fb 編號 --date YYMMDD --post 內文.txt [--comment 留言.txt]
                       收錄或更新一篇（內文、相關文章、貼文索引與留言指紋），之後自動執行 sync
  sync                 依貼文索引重寫所有相關文章、補上雙向前後篇、把已收錄的標題改成連結
  comment 檔名         產生某篇的臉書整理留言
  check                列出待辦（需要更新的臉書留言、待確認、建議共用區塊）
  mark-posted 檔名     把產生的留言記為已貼到臉書
  due [N]              列出最久沒檢查的 N 篇已收錄文章（預設 5）
  metrics 檔名 JSON    把臉書洞察數字寫進該篇的屬性（只留最新）
  export [路徑]        把所有文章的洞察數字匯出成 CSV（分析用）
  checked 檔名…        記錄這些文章已檢查、沒有變動
"""
import os, re, sys, glob, json, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, 'src/content/docs')
SYNC = os.path.join(ROOT, 'src/content/_sync')
SHARED = os.path.join(SYNC, '共用區塊')
REG = os.path.join(SYNC, '貼文索引.md')
FBU = 'https://www.facebook.com/lunglung0815/posts/'
HEAD = '## 相關文章'
SEP = '--'

def read(p): return open(p, encoding='utf-8').read().replace('\r\n', '\n')
def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
def fbid(u):
    m = re.search(r'lunglung0815/posts/(\d+)', u or ''); return m.group(1) if m else None
def split_date(t):
    m = re.match(r'^(.*?)\s?(\d{6})$', t); return (m.group(1), m.group(2)) if m else (t, None)
def norm_title(t): return re.sub(r'^▌\s+', '▌', t.strip())
def with_date(t, d): return t + (((' ' if re.search(r'[A-Za-z.!?]$', t) else '') + d) if d else '')

# ---------------- 貼文索引 ----------------
COLS = ['臉書編號', '標題', '日期碼', '網站檔名', '舊標題', '內文指紋', '留言指紋', '最後檢查', '備註']
# 臉書洞察數字：存在各篇文章的屬性（frontmatter），不出現在網站上
INSIGHT_KEYS = ['洞察日期', '瀏覽次數', '瀏覽者', '追蹤者瀏覽', '非追蹤者瀏覽', '心情', '留言', '點擊', '分享', '收益', '第1天瀏覽', '第3天瀏覽', '第7天瀏覽', '第14天瀏覽']
class Registry:
    def __init__(self):
        self.rows = {}
        if os.path.exists(REG):
            head = None
            for l in read(REG).splitlines():
                if not l.startswith('| ') or l.startswith('| ---'): continue
                c = [x.strip().replace('\\|', '|') for x in re.split(r'(?<!\\)\|', l.strip())[1:-1]]
                if c and c[0] == '臉書編號': head = c; continue
                if head and c and c[0].isdigit():
                    r = dict(zip(head, c)); self.rows[c[0]] = {k: r.get(k, '') for k in COLS}
    def get(self, i): return self.rows.get(i)
    def title(self, i): return self.rows.get(i, {}).get('標題', i)
    def date(self, i): return self.rows.get(i, {}).get('日期碼') or None
    def by_title(self, t):
        t = norm_title(t)
        for i, r in self.rows.items():
            if r['標題'] == t: return i
        for i, r in self.rows.items():
            if t in [x for x in r['舊標題'].split('／') if x]: return i
        return None
    def note(self, i, msg):
        r = self.rows[i]
        if '已確認' in r['備註']: return  # 已由作者決定，不再詢問
        if msg not in r['備註']: r['備註'] = (r['備註'] + '；' if r['備註'] else '') + msg
    def add(self, i, title, date, where, authoritative=False):
        title = norm_title(title)
        r = self.rows.get(i)
        if not r:
            self.rows[i] = {k: '' for k in COLS}; self.rows[i].update({'臉書編號': i, '標題': title, '日期碼': date or ''}); return
        if title != r['標題']:
            if authoritative:
                olds = [x for x in r['舊標題'].split('／') if x]
                if r['標題'] not in olds: olds.append(r['標題'])
                r['舊標題'] = '／'.join(x for x in olds if x != title); r['標題'] = title
            elif title not in r['舊標題'].split('／'):
                self.note(i, '標題另見「%s」（%s），待確認' % (title, where))
        if date:
            if not r['日期碼']: r['日期碼'] = date
            elif date != r['日期碼']:
                if authoritative: r['日期碼'] = date
                else: self.note(i, '日期另見 %s（%s），待確認' % (date, where))
    def save(self):
        rows = sorted(self.rows.values(), key=lambda r: (r['日期碼'] or '000000', r['臉書編號']), reverse=True)
        esc = lambda s: s.replace('|', '\\|')
        out = ['# 貼文索引', '', '所有出現過的臉書貼文。留言與相關文章裡的標題、日期都以這裡為準（已收錄的文章以文章本身的標題為準）。「留言指紋」記錄目前貼在臉書上的整理留言版本。臉書洞察數字存在各篇文章的屬性裡。', '',
               '| ' + ' | '.join(COLS) + ' |', '| ' + ' | '.join(['---'] * len(COLS)) + ' |']
        for r in rows: out.append('| ' + ' | '.join(esc(r[c]) for c in COLS) + ' |')
        write(REG, '\n'.join(out) + '\n')

# ---------------- 文章 ----------------
def split_fm(s):
    m = re.match(r'^---\n(.*?)\n---\n', s, re.S)
    return (m.group(1), s[m.end():]) if m else ('', s)
def fm_get(fm, key):
    m = re.search(r'^' + re.escape(key) + r':\s*(.*)$', fm, re.M)
    if not m: return None
    v = m.group(1).strip(); return json.loads(v) if v.startswith('"') else v

def load_posts():
    posts = {}
    for p in sorted(glob.glob(os.path.join(POSTS, '*.md')) + glob.glob(os.path.join(POSTS, '*', '*.md'))):
        if os.sep + 'attachments' + os.sep in p: continue
        fm, body = split_fm(read(p)); i = fbid(fm_get(fm, 'fb') or '')
        if i: posts[i] = {'path': p, 'file': os.path.basename(p)[:-3], 'fm': fm, 'body': body}
    return posts

def split_related(body):
    k = body.find('\n' + HEAD + '\n')
    if k < 0: return body.rstrip('\n'), None
    return body[:k].rstrip('\n'), body[k + len(HEAD) + 2:]

WIKI = re.compile(r'^\[\[([^|\]]+)\|([^\]]*)\]\](\d{6})?$')
EMBED = re.compile(r'^!\[\[([^\]|]+)\]\]$')
EXT = re.compile(r'^\[(.+)\]\((https?://\S+)\)$')

def parse_lines(text, reg, f2i):
    """相關文章或共用區塊的文字 → 區塊清單；每項是 ('post',id) ('ext',文字,網址) ('embed',名) ('label',文字)"""
    blocks, cur = [], []
    for raw in text.split('\n'):
        l = raw.strip()
        if not l: continue
        if l == SEP: blocks.append(cur); cur = []; continue
        m = WIKI.match(l)
        if m and m.group(1) in f2i: cur.append(('post', f2i[m.group(1)])); continue
        m = EMBED.match(l)
        if m: cur.append(('embed', m.group(1))); continue
        m = EXT.match(l)
        if m:
            i = fbid(m.group(2))
            cur.append(('post', i) if i else ('ext', m.group(1), m.group(2))); continue
        t, _ = split_date(l); i = reg.by_title(t)
        cur.append(('post', i) if i else ('label', l.strip('`')))
    blocks.append(cur)
    return [b for b in blocks if b] if any(blocks) else []

def site_line(it, reg, posts, me=None):
    if it[0] == 'post':
        t, d = reg.title(it[1]), reg.date(it[1])
        if it[1] in posts and it[1] != me: return '[[%s|%s]]%s' % (posts[it[1]]['file'], t, ((' ' if re.search(r'[A-Za-z.!?]$', t) else '') + d) if d else '')
        return with_date(t, d)
    if it[0] == 'ext': return '[%s](%s)' % (it[1], it[2])
    if it[0] == 'embed': return '![[%s]]' % it[1]
    return '`%s`' % it[1] if it[1].startswith('#') else it[1]

def render_blocks(blocks, reg, posts, me=None):
    return ('\n\n' + SEP + '\n\n').join('\n'.join(site_line(it, reg, posts, me) for it in b) for b in blocks)

def shared_names(): return sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(SHARED, '*.md')))
def shared_split(name):
    return split_fm(read(os.path.join(SHARED, name + '.md')))
def shared_items(name, reg, f2i):
    b = parse_lines(shared_split(name)[1], reg, f2i)
    return b[0] if b else []

def render_ai(txt, reg, posts, f2i):
    """AI 精選：保留標籤、--、空行；每行「文章｜選入理由」的文章部分照一般規則改成連結"""
    out = []
    for raw in txt.strip('\n').split('\n'):
        l = raw.strip(); left, bar, why = l.partition('｜')
        if not l or l == SEP: out.append(l); continue
        b = parse_lines(left.strip(), reg, f2i); it = b[0][0] if b and b[0] else None
        line = site_line(it, reg, posts) if it and it[0] in ('post', 'ext', 'embed') else raw.rstrip()
        out.append(line + ('｜' + why.strip() if bar else ''))
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(out))

def expand(block, reg, f2i):
    out = []
    for it in block:
        if it[0] == 'embed': out += shared_items(it[1], reg, f2i)
        else: out.append(it)
    return out

def compress(block, reg, f2i):
    """把區塊中與共用區塊完全相同的連續段落換成 ![[名稱]]"""
    for name in sorted([n for n in shared_names() if not n.startswith('A')], key=lambda n: -len(shared_items(n, reg, f2i))):
        s = shared_items(name, reg, f2i); n = len(s)
        if n < 2: continue
        for k in range(len(block) - n + 1):
            if block[k:k + n] == s: return compress(block[:k], reg, f2i) + [('embed', name)] + compress(block[k + n:], reg, f2i)
    return block

# ---------------- 內文轉換 ----------------
def convert_body(raw):
    lines = raw.replace('​', '').replace('\r\n', '\n').rstrip('\n').split('\n')
    title = norm_title(lines[0]); out = []
    for l in lines[1:]:
        if l.strip() == SEP: out += ['', SEP, '']; continue
        if re.fullmatch(r'#[^\s#`]+', l.strip()): out.append('`%s`' % l.strip()); continue
        out.append(l)
    s = re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip('\n')
    return title, s

def description(raw):
    lines = raw.replace('​', '').split('\n')[1:]
    for l in lines:
        l = l.strip()
        if not l or l == SEP or l.lstrip('`').startswith('#') or l.startswith('•') or ORIG.match(l): continue
        l = re.sub(r'^(?:[⒈-⒛]|\d+[.、．])\s*', '', l)
        if len(l) <= 80: return l
        cut = max(l.rfind(c, 0, 80) for c in '。？！')
        return l[:cut + 1] if cut >= 20 else l[:78] + '…'
    return ''

ORIG = re.compile(r'^［原文寫於：(\d{4})-(\d{2})-(\d{2})')
def original_date(raw):
    """內文第二行若是［原文寫於：YYYY-MM-DD …］，回傳原文日期碼 YYMMDD"""
    for l in raw.replace('\u200b', '').split('\n')[1:3]:
        m = ORIG.match(l.strip())
        if m: return m.group(1)[2:] + m.group(2) + m.group(3)
    return None

def insight_lines(fm):
    """從舊的 frontmatter 取出洞察數字那幾行（重新收錄時保留）"""
    return [l for l in fm.split('\n') if l.split(':', 1)[0].strip() in INSIGHT_KEYS]

def post_text(title, desc, date, fid, body, related, category='', image='', fbdate='', keep=()):
    fm = ['---', 'title: ' + json.dumps(title, ensure_ascii=False), 'description: ' + json.dumps(desc, ensure_ascii=False),
          'date: 20%s-%s-%s' % (date[:2], date[2:4], date[4:6]), 'category: ' + json.dumps(category, ensure_ascii=False), 'order: -%s' % date[:6],
          'fb: ' + FBU + fid]
    if fbdate: fm.append('fbDate: 20%s-%s-%s' % (fbdate[:2], fbdate[2:4], fbdate[4:6]))  # 臉書發文日期（與原文日期不同時）
    if image: fm += ['image: ' + json.dumps(image, ensure_ascii=False), 'hideCoverImage: true']
    fm += list(keep)
    fm.append('---')
    return '\n'.join(fm) + '\n' + body + '\n\n' + HEAD + '\n\n' + related.strip('\n') + '\n'

def parse_comment(text):
    """臉書整理留言 → (區塊[(類別,...)], [(id,標題,日期)])"""
    L = [l.strip() for l in text.replace('​', '').replace('\r\n', '\n').split('\n')]
    blocks, cur, seen, k = [], [], [], 0
    while k < len(L):
        l = L[k]
        if not l: k += 1; continue
        if l == SEP: blocks.append(cur); cur = []; k += 1; continue
        nxt = L[k + 1] if k + 1 < len(L) else ''
        if re.match(r'https?://', nxt):
            i = fbid(nxt)
            if i:
                t, d = split_date(l); cur.append(('post', i)); seen.append((i, t, d))
            else: cur.append(('ext', l, nxt))
            k += 2; continue
        cur.append(('label', l)); k += 1
    blocks.append(cur)
    return [b for b in blocks if b], seen

# ---------------- 指令 ----------------
def cmd_import(a):
    reg, posts = Registry(), load_posts()
    raw = read(a.post); title, body = convert_body(raw)
    fbdate = ''
    orig = original_date(raw)
    if orig and orig != a.date: fbdate, a.date = a.date, orig  # 舊文重發：檔名與日期碼用原文日期
    r0 = reg.get(a.fb)
    if r0 and '已確認' in r0['備註'] and title != r0['標題'] and title in r0['舊標題'].split('／'):
        title = r0['標題']  # 作者確認過的標題優先（臉書第一行列為舊標題）
    reg.add(a.fb, title, a.date, '本文', authoritative=True)
    taken = {v['file'] for v in posts.values()}
    old = posts.get(a.fb)  # 既有版本（先記下，最後才刪舊檔）
    if old:
        p = old; file = p['file']
        _, rel = split_related(p['body']); rel = rel or ''
        folder = a.folder or os.path.basename(os.path.dirname(p['path']))
        if folder == os.path.basename(POSTS): folder = ''
        path = os.path.join(POSTS, folder, file + '.md')
    else:
        file = a.date; n = 2
        while file in taken: file = '%s-%d' % (a.date, n); n += 1
        folder = a.folder or ''
        path = os.path.join(POSTS, folder, file + '.md'); rel = ''
    # 圖片：存到 docs/attachments/檔名-n.副檔名，放在內文最後；第一張當清單縮圖（頁面上方不重複顯示）
    imgs = []
    for k, src in enumerate(a.images or [], 1):
        ext = os.path.splitext(src)[1].lower() or '.jpg'
        name = '%s-%d%s' % (file, k, ext); dst = os.path.join(POSTS, 'attachments', name)
        os.makedirs(os.path.dirname(dst), exist_ok=True); open(dst, 'wb').write(open(src, 'rb').read()); imgs.append(name)
    if imgs: body = body + '\n\n' + '\n'.join('![](/docs/attachments/%s)' % n for n in imgs)
    image = '/docs/attachments/' + imgs[0] if imgs else ''
    reg.rows[a.fb]['網站檔名'] = file
    reg.rows[a.fb]['內文指紋'] = body_fingerprint(raw); reg.rows[a.fb]['最後檢查'] = today()
    if a.comment:
        ctext = read(a.comment).strip('\n')
        blocks, seen = parse_comment(ctext)
        for i, t, d in seen:
            if i != a.fb: reg.add(i, t, d, '%s 留言' % file)
        reg.save(); posts = load_posts(); posts.setdefault(a.fb, {'file': file})
        f2i = {v['file']: k for k, v in posts.items()}
        blocks = [compress(b, reg, f2i) for b in blocks]
        if not blocks or not blocks[0] or blocks[0][0] != ('post', a.fb): blocks.insert(0, [('post', a.fb)])
        rel = render_blocks(blocks, reg, posts, a.fb)
        reg.rows[a.fb]['留言指紋'] = fingerprint(ctext); save_fb_comment(file, ctext)
    if not rel.strip(): rel = with_date(reg.title(a.fb), a.date)
    reg.save()
    if not imgs and old:  # 重新收錄時保留原本的圖片
        old_main, _ = split_related(old['body'])
        kept = re.findall(r'^!\[\]\(/docs/attachments/[^)]+\)$', old_main, re.M)
        if kept: body = body + '\n\n' + '\n'.join(kept); image = fm_get(old['fm'], 'image') or ''
    write(path, post_text(title, description(raw), a.date, a.fb, body, rel, folder, image, fbdate, insight_lines(old['fm']) if old else ()))
    if old and os.path.abspath(old['path']) != os.path.abspath(path): os.remove(old['path'])
    print('已收錄：%s（%s）' % (file, title)); cmd_sync(quiet=True)
    # 詢問：本篇第一區塊引用的文章，是否也要在它們的前後篇加上本篇（由作者決定，不自動加）
    reg, posts = Registry(), load_posts(); f2i = {v['file']: k for k, v in posts.items()}
    _, rel = split_related(posts[a.fb]['body'])
    blocks = parse_lines(rel or '', reg, f2i)
    cited = [it[1] for it in (expand(blocks[0], reg, f2i) if blocks else []) if it[0] == 'post' and it[1] != a.fb]
    ask = []
    for j in cited:  # 只問：對方已收錄，且它的第一區塊還沒有本篇
        if j not in posts: continue
        _, jr = split_related(posts[j]['body']); jb = parse_lines(jr or '', reg, f2i)
        if ('post', a.fb) not in (expand(jb[0], reg, f2i) if jb else []): ask.append(j)
    if ask:
        print('要不要在這些文章的第一區塊加上本篇？' + '、'.join(reg.title(j) for j in ask))

def cmd_sync(quiet=False):
    reg, posts = Registry(), load_posts(); f2i = {v['file']: k for k, v in posts.items()}
    for i, p in posts.items(): reg.rows.setdefault(i, {k: '' for k in COLS})['網站檔名'] = p['file']
    for i, p in posts.items():  # 分類＝所在資料夾
        folder = os.path.basename(os.path.dirname(p['path'])); folder = '' if folder == os.path.basename(POSTS) else folder
        if fm_get(p['fm'], 'category') != folder:
            p['fm'] = re.sub(r'^category:.*$', 'category: ' + json.dumps(folder, ensure_ascii=False), p['fm'], flags=re.M)
            p['fm_changed'] = True
    parsed = {}
    for i, p in posts.items():
        main, rel = split_related(p['body'])
        parsed[i] = (main, [compress(b, reg, f2i) for b in parse_lines(rel or '', reg, f2i)])  # 新的共用區塊自動套用
    waiting = []  # 前後篇不再自動雙向；只在收錄新文章時詢問一次（見 cmd_import）
    changed = []
    for i, (main, blocks) in parsed.items():
        p = posts[i]; new = '---\n' + p['fm'] + '\n---\n' + main + '\n\n' + HEAD + '\n\n' + render_blocks(blocks, reg, posts, i) + '\n'
        if p.get('fm_changed') or new != read(p['path']): write(p['path'], new); changed.append(p['file'])
    for name in shared_names():
        fm, txt = shared_split(name)
        if name.startswith('A'): new = ('---\n' + fm + '\n---\n' if fm else '') + render_ai(txt, reg, posts, f2i) + '\n'
        else: b = shared_items(name, reg, f2i); new = ('---\n' + fm + '\n---\n' if fm else '') + '\n'.join(site_line(it, reg, posts) for it in b) + '\n'
        if new != read(os.path.join(SHARED, name + '.md')): write(os.path.join(SHARED, name + '.md'), new); changed.append('共用/' + name)
    reg.save()
    if not quiet: print('已更新：' + ('、'.join(changed) if changed else '（無）'))
    return changed, waiting

def fb_line(it, reg):
    if it[0] == 'post': return with_date(reg.title(it[1]), reg.date(it[1])) + '\n' + FBU + it[1]
    if it[0] == 'ext': return it[1] + '\n' + it[2]
    return it[1]

def cmd_comment(file):
    reg, posts = Registry(), load_posts(); f2i = {v['file']: k for k, v in posts.items()}
    i = f2i[file]; _, rel = split_related(posts[i]['body'])
    blocks = [expand(b, reg, f2i) for b in parse_lines(rel or '', reg, f2i)] or [[]]
    if not blocks[0] or blocks[0][0] != ('post', i): blocks[0] = [('post', i)] + blocks[0]
    return ('\n\n' + SEP + '\n\n').join('\n\n'.join(fb_line(it, reg) for it in b) for b in blocks)

def fingerprint(text):
    """臉書留言的比對碼（不計日期碼）"""
    import hashlib
    t = '\n'.join(l for l in text.replace('\u200b', '').split('\n') if l.strip())
    return hashlib.sha256(strip_dates(t).encode('utf-8')).hexdigest()[:10]

def body_fingerprint(raw):
    """內文指紋：去掉零寬空白後全文 SHA-256 的前 10 碼（和瀏覽器算的一致）"""
    import hashlib
    return hashlib.sha256(raw.replace('\u200b', '').replace('\r\n', '\n').rstrip('\n').encode('utf-8')).hexdigest()[:10]

FBC = os.path.join(SYNC, '留言原文')
def nonblank(t): return '\n'.join(l.strip() for l in t.replace('\u200b', '').split('\n') if l.strip())
def save_fb_comment(file, text): write(os.path.join(FBC, file + '.txt'), text.strip('\n') + '\n')
def comment_diff(file, gen, reg):
    """比對臉書上目前的留言（留言原文）和新產生的版本，用文字說明改了什麼"""
    p = os.path.join(FBC, file + '.txt')
    if not os.path.exists(p): return ['（沒有臉書目前留言的紀錄，無法比對；這是第一次產生整理留言）']
    ob, _ = parse_comment(read(p)); nb, _ = parse_comment(gen)
    name = lambda it: reg.title(it[1]) if it[0] == 'post' else (it[1] if it[0] != 'ext' else it[1])
    def where(blocks):
        d = {}
        for k, b in enumerate(blocks, 1):
            for it in b: d.setdefault(it, k)
        return d
    o, n = where(ob), where(nb); out = []
    for it in n:
        if it not in o: out.append('新增：%s（第 %d 區塊）' % (name(it), n[it]))
    for it in o:
        if it not in n: out.append('刪除：%s（原第 %d 區塊）' % (name(it), o[it]))
    for it in n:
        if it in o and o[it] != n[it]: out.append('移動：%s（第 %d → 第 %d 區塊）' % (name(it), o[it], n[it]))
    if not out and [list(b) for b in ob] != [list(b) for b in nb]: out.append('順序調整')
    oldtxt = {l.strip() for l in read(p).split('\n') if l.strip() and not l.startswith('http')}
    for l in gen.split('\n'):
        if l.strip() and not l.startswith('http') and l.strip() not in oldtxt and split_date(l.strip())[0] in {split_date(x)[0] for x in oldtxt}:
            out.append('補上日期：' + l.strip())
    titles_old = {split_date(x)[0] for x in oldtxt}
    for it in n:
        if it in o and it[0] == 'post' and reg.title(it[1]) not in titles_old: out.append('標題修正：%s' % reg.title(it[1]))
    if read(p).count('\n\n') == 0 and '\n\n' in gen: out.append('格式：項目之間改為空一行')
    return out or ['只有格式差異']

def today():
    import datetime
    return datetime.date.today().strftime('%y%m%d')

def strip_dates(text): return '\n'.join(split_date(l)[0] if not l.startswith('http') else l for l in text.split('\n'))  # 只忽略日期；格式差異（例如 ▌ 後的空格）也算要更新

def cmd_check():
    changed, waiting = cmd_sync(quiet=True)
    if changed: print('（已先同步：%s）' % '、'.join(changed))
    reg, posts = Registry(), load_posts(); f2i = {v['file']: k for k, v in posts.items()}
    need = []
    for i, p in sorted(posts.items(), key=lambda x: x[1]['file']):
        cur = reg.rows.get(i, {}).get('留言指紋', '')
        gen = cmd_comment(p['file'])
        # 只列：內容有變（只差日期不算），而且留言裡每一篇都有日期
        dated = all(re.search(r'\d{6}$', L[k - 1]) for L in [gen.split('\n')] for k in range(1, len(L)) if fbid(L[k]))
        fbp = os.path.join(FBC, p['file'] + '.txt')
        nodate = os.path.exists(fbp) and dated and nonblank(read(fbp)) != nonblank(gen)  # 只差日期也要補上
        if not cur or (cur != fingerprint(gen) and dated) or nodate: need.append(p['file'] + ('（沒有留言紀錄）' if not cur else ''))
    print('臉書留言需要更新：' + ('、'.join(need) if need else '（無）'))
    out = ['# 待貼留言', '', '以下臉書整理留言需要更新：點開臉書原文，用程式碼區塊右上角的複製鈕複製，整則取代原本的留言。貼好後告訴 Claude，它就會從這裡移除。', '']
    for f in need:
        f = f.split('（')[0]; i = f2i[f]
        g = cmd_comment(f)
        out += ['## %s %s' % (f, reg.title(i)), '', '[臉書原文](%s%s)' % (FBU, i), ''] + ['- ' + x for x in comment_diff(f, g, reg)] + ['', '```', g, '```', '']
    write(os.path.join(SYNC, '待貼留言.md'), '\n'.join(out).rstrip('\n') + '\n' if need else '# 待貼留言\n\n目前沒有需要更新的臉書留言。\n')
    todo = [r for r in reg.rows.values() if '待確認' in r['備註']]
    if todo:
        print('貼文索引待確認：')
        for r in todo: print('  %s %s：%s' % (r['臉書編號'], r['標題'], r['備註']))
    runs = {}
    for i, p in posts.items():
        _, rel = split_related(p['body'])
        for b in parse_lines(rel or '', reg, f2i):
            ids = [it[1] for it in b if it[0] == 'post']
            for n in range(3, len(ids) + 1):
                for k in range(len(ids) - n + 1): runs.setdefault(tuple(ids[k:k + n]), set()).add(p['file'])
    sug = [r for r, fs in runs.items() if len(fs) >= 2]
    sug = [r for r in sug if not any(len(o) > len(r) and any(o[k:k + len(r)] == r for k in range(len(o))) for o in sug)]
    for r in sug: print('建議建立共用區塊：' + '、'.join(reg.title(x) for x in r) + '（出現在 %s）' % '、'.join(sorted(runs[r])))

if __name__ == '__main__':
    if len(sys.argv) < 2: print(__doc__); sys.exit()
    c = sys.argv[1]
    if c == 'import':
        ap = argparse.ArgumentParser(); ap.add_argument('cmd'); ap.add_argument('--fb', required=True); ap.add_argument('--date', required=True)
        ap.add_argument('--post', required=True); ap.add_argument('--comment'); ap.add_argument('--folder', default='')
        ap.add_argument('--images', nargs='*'); cmd_import(ap.parse_args())
    elif c == 'sync': cmd_sync()
    elif c == 'metrics':  # metrics 檔名 '{"瀏覽次數":…}'：把臉書洞察數字寫進該篇的屬性（只留最新）
        reg, posts = Registry(), load_posts(); f2i = {v['file']: k for k, v in posts.items()}
        f = sys.argv[2]; i = f2i[f]; m = json.loads(sys.argv[3]); p = posts[i]
        m['洞察日期'] = __import__('datetime').date.today().isoformat()
        fm = '\n'.join(l for l in p['fm'].split('\n') if l.split(':', 1)[0].strip() not in INSIGHT_KEYS)
        def val(k):
            v = str(m.get(k, '')).replace(',', '')
            return v if re.fullmatch(r'\d+(\.\d+)?', v) else json.dumps(v, ensure_ascii=False)
        fm += '\n' + '\n'.join('%s: %s' % (k, val(k)) for k in INSIGHT_KEYS if str(m.get(k, '')) != '')
        write(p['path'], '---\n' + fm + '\n---\n' + p['body'])
        reg.rows[i]['最後檢查'] = today(); reg.save()
        print('已更新洞察：%s（瀏覽 %s、第7天 %s、收益 US$%s）' % (f, m.get('瀏覽次數'), m.get('第7天瀏覽'), m.get('收益')))
    elif c == 'export':  # 把所有文章的洞察數字匯出成 CSV（分析用，需要時才產生）
        import csv
        posts = load_posts(); out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(SYNC, '洞察匯出.csv')
        cols = ['檔名', '分類', '標題', '發文日期'] + INSIGHT_KEYS
        with open(out, 'w', encoding='utf-8-sig', newline='') as fh:
            w = csv.writer(fh); w.writerow(cols)
            for i, p in sorted(posts.items(), key=lambda x: x[1]['file'], reverse=True):
                fm = p['fm']; w.writerow([p['file'], fm_get(fm, 'category') or '', fm_get(fm, 'title') or '', str(fm_get(fm, 'fbDate') or fm_get(fm, 'date') or '')] + [fm_get(fm, k) or '' for k in INSIGHT_KEYS])
        print('已匯出：' + out)
    elif c == 'due':  # 最久沒檢查的已收錄文章（臉書編號、檔名、內文指紋、留言指紋）
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        reg, posts = Registry(), load_posts()
        for i in sorted(posts, key=lambda i: (reg.rows.get(i, {}).get('最後檢查', ''), posts[i]['file']))[:n]:
            r = reg.rows[i]; print(i, posts[i]['file'], r['內文指紋'], r['留言指紋'], r['最後檢查'] or '（未檢查）')
    elif c == 'checked':  # 檢查過、沒有變動
        reg, posts = Registry(), load_posts(); f2i = {v['file']: k for k, v in posts.items()}
        for f in sys.argv[2:]: reg.rows[f2i[f]]['最後檢查'] = today()
        reg.save(); print('已記錄檢查：' + '、'.join(sys.argv[2:]))
    elif c == 'comment': print(cmd_comment(sys.argv[2]))
    elif c == 'check': cmd_check()
    elif c == 'mark-posted':
        reg, posts = Registry(), load_posts(); f2i = {v['file']: k for k, v in posts.items()}
        for f in sys.argv[2:]:
            g = cmd_comment(f); reg.rows[f2i[f]]['留言指紋'] = fingerprint(g); save_fb_comment(f, g); print('已記錄：' + f)
        reg.save(); cmd_check()
    else: print(__doc__)
