# astro-modular 客製化紀錄（交接備忘）

> 用途：未來要再修整網站、或開新對話時，把這份貼給 Claude，就能快速知道「現況」與「動過哪些東西」。
> 這份是技術備忘，跟對外的那篇文章用途不同。

---

## 一、基本資料

- **主題**：astro-modular（作者 davidvkimball），透過 GitHub 上的 Quick Start 一鍵部署到 **Cloudflare Workers**。
- **正式網域**：https://tzulungchang.com （自有網域，已在 Cloudflare 綁定到 Worker）
- **原始預設網址**：https://astro-modular.kstin0815.workers.dev （workers.dev 子網域，仍可運作）
- **編輯流程**：本機 clone → 用 Obsidian 編輯 → `git push` → Cloudflare 自動重新建置。
- **本地預覽**：在專案資料夾執行 `pnpm install`（第一次），之後 `pnpm dev`，瀏覽器開 `http://localhost:4321`。
- **重要背景**：Quick Start 複製的是主題的 **master 分支**，當時正處於「升級到 Astro 7」的不穩定中間狀態，下面的建置修正就是為了讓它能成功 build。

---

## 二、為了能成功建置做的修正（一次性）

1. **`package.json`** 加入指定 pnpm 版本（Cloudflare 預設抓的版本太舊）：
   ```json
   "packageManager": "pnpm@10.29.3"
   ```
2. **`.npmrc`**（在 repo 根目錄新建這個檔）：
   ```
   shamefully-hoist=true
   ```
   解決 `Cannot find module '@astrojs/markdown-remark'`（config 引用了一個 pnpm 嚴格隔離下找不到的套件）。
3. **`src/config.ts` 必填欄位**：`site / title / description / author` 不能空白，且 `site` 必須以 `http` 開頭，否則建置會以「Site configuration is invalid」失敗。曾因這幾項空白多次失敗。

---

## 三、設定與客製化（逐檔案）

### `src/config.ts`
- `site`：**應為** `"https://tzulungchang.com"`（不要結尾斜線、不要 `/posts/`）。
  - ⚠️ **待確認/待修**：曾發現 `site` 還停在 `"https://astro-modular.kstin0815.workers.dev/posts/"`，導致 canonical、OG、sitemap、RSS 全部指向舊網址，且 OG 圖網址出現壞掉的雙斜線 `/posts//open-graph.png`。若還沒改，請改成上面正確值。
- `navigation.showNavigation: true`（這才是「顯示導覽列」的開關，不是 style）
- `navigation.showMobileMenu: true`（手機選單）
- `navigation.style: "minimal"`（外觀；minimal 仍會顯示導覽列）
- `footer.showSocialIconsInFooter: true`（社群圖示顯示在**頁尾**，不是頂部；social 連結清單在 `navigation.social`）
- `postOptions.readingTime: true`、`wordCount: true`、`tags: true`
- `postOptions.comments.enabled: true`（`provider` 欄位仍是 `"giscus"` 但已不使用；其餘 giscus 欄位留空無妨）
- ⚠️ **雷區**：有一個「Astro Modular Settings」Obsidian 外掛會用它表單裡的值**整份覆寫** config.ts。**不要同時手改檔案又用外掛存檔**，否則手改的會被洗掉。**選一種方式就好**（目前採手改）。`// [CONFIG:...]` 那些註解標記不要刪。

### `src/components/GiscusComments.astro`
- 已**整個換成 Cusdis 版**（取代內建 giscus）：訪客可匿名留言、留言需審核（email 核准）。
- 內含 `<div id="cusdis_thread" data-app-id="（你的 App ID）">` + 一段 inline script：載入 `cusdis.es.js`、用 `location` 帶入 page-id/url/title、並掛上 Swup 的 `page:view` 事件讓換頁時留言重載。
- App ID 必須放在**雙引號**內（放進 `{ }` 會被當 JS 解析而建置失敗）。

### `src/styles/global.css`（都加在檔案最後面）
- 內文左右對齊：`#post-content { text-align: justify; }`
- 內文超連結加底線：`.prose a:not(.wikilink) { text-decoration: underline; }`
- 引文精簡（去底色/圓角、縮內距、字略小）：`.prose blockquote { ... font-size: 0.9em; }` 搭配 `.prose blockquote p { margin: 0; }`
- **Cusdis 留言框底部被切的修法**：`#cusdis_thread iframe { min-height: 360px !important; }`
  - 原因：Cusdis 用 JS 設 `height`（用 offsetHeight 算、少了底部邊距）。我們改用 **`min-height`**（不同屬性、不會跟它打架），瀏覽器取較大值，底部就不會被切。數字（360）可依實際微調。

### `src/content.config.ts`
- posts schema 加入置頂欄位：在 `draft` 附近加 `pinned: z.boolean().optional(),`

### `src/utils/markdown.ts`（約第 292 行 `sortPostsByDate`）
- 排序改成「置頂優先、其餘照日期」：
  ```js
  return posts.sort((a, b) => {
    const ap = a.data.pinned ? 1 : 0;
    const bp = b.data.pinned ? 1 : 0;
    if (ap !== bp) return bp - ap;
    return b.data.date.getTime() - a.data.date.getTime();
  });
  ```
- 全站列表（含各 tag 分類頁）共用這個函式，改一處即全部生效。

### RSS / Atom 訂閱按鈕（已移除）
- 三個檔案各刪掉一段 `<div class="flex items-center space-x-2"> … </div>`（內含兩個 feed 連結）：
  - `src/pages/posts/index.astro`（View all posts 第一頁）
  - `src/pages/posts/[page].astro`（第 2 頁以後）
  - `src/pages/posts/tag/[...tag].astro`（標籤頁）
- `/rss.xml`、`/feed.xml` 本身仍存在，只是按鈕拿掉了。

---

## 四、內容慣例（已決定的規則）

- **檔名 = 網址**。所以 `.md` 檔名取**英文**（網址才乾淨）；frontmatter 的 `title:` 寫**中文**（顯示用）。兩者獨立、互不影響。
- **分類用 tag（英文 slug）**，成熟度三階 + 一個來源類：
  - `seedling`（種子，雜亂未整理）
  - `budding`（萌芽，加工中未完成）
  - `evergreen`（常青，完成的成品）
  - `gleaning`（拾穗，外來/讀書心得之類）
  - 導覽列主分類最多放三個（成熟度三階）；`gleaning` 等可當主題標籤或視情況獨立。
- **置頂**：在該篇 frontmatter 加 `pinned: true`（Obsidian 可用「屬性」面板加 checkbox 型別）。
- **aliases**：frontmatter 的 `aliases` 會變成「舊網址轉址」。**改了已上線文章的檔名**（網址變了）時，把舊檔名填進 aliases，舊連結才不會 404。

---

## 五、其他雷區提醒

- 主題 master 分支當時不穩定（升級中），這是建置要修正的根源。
- `node_modules` 很大且已被 `.gitignore` 忽略——不要 commit。
- 不要刪掉內容類型資料夾（posts / projects / docs / special），就算空的也別刪，否則建置 ENOENT 失敗。
- 改 CSS「沒效果」時，先確認是看**線上**還是**本地**：線上要 push＋等 Cloudflare 建置成功＋瀏覽器 `Ctrl/Cmd+Shift+R`；本地 `pnpm dev` 存檔即時更新。

---

## 六、未來開新對話怎麼快速跟上

1. **把這份文件貼給 Claude**（最快）。
2. 視問題**額外貼上相關的那個檔案**：
   - 留言相關 → `src/components/GiscusComments.astro`
   - 樣式相關 → `src/styles/global.css`
   - 設定/導覽/開關 → `src/config.ts`
   - 排序/置頂/內容處理 → `src/utils/markdown.ts`、`src/content.config.ts`
3. 想給最精準的「到底改了哪些」，在專案資料夾執行：
   ```
   git log --stat
   ```
   或對照原始主題看差異：
   ```
   git diff
   ```
   把輸出貼上來即可。
