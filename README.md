# astro-modular 客製化紀錄（交接備忘）

> 用途：未來要再修整網站、或開新對話時，把這份貼給 Claude，就能快速知道「現況」與「動過哪些東西」。
> 這份是技術備忘，跟對外的那篇文章用途不同。

---

## 一、基本資料

- **主題**：astro-modular（作者 davidvkimball），部署在 **Cloudflare Workers**。
- **主題版本**：1.1.9（2026-10-27 從 0.9.3 升級；Astro 7.4、Tailwind 4）。
- **正式網域**：https://tzulungchang.com （自有網域，已在 Cloudflare 綁定到 Worker）
- **原始預設網址**：https://astro-modular.kstin0815.workers.dev （workers.dev 子網域，仍可運作）
- **編輯流程**：本機 clone → 用 Obsidian 編輯 → Obsidian Git 同步 → Cloudflare 自動重新建置。
- **本地預覽**：在專案資料夾執行 `pnpm install`（第一次或升級後），之後 `pnpm dev`，瀏覽器開 `http://localhost:5000`。
- **只能打網址進去的頁面**（不在導覽列）：`/jci/`、`/judge/`（講義，`src/content/special/`）、`/argument_mapping.html`（互動工具，`public/`）。

---

## 二、建置設定（保留）

1. **`package.json`** 指定 pnpm 版本（Cloudflare 預設抓的版本太舊）：`"packageManager": "pnpm@10.29.3"`
2. **`.npmrc`**：`shamefully-hoist=true`。1.1.9 已正式宣告 `@astrojs/markdown-remark` 依賴，理論上不再需要，但保留無害。
3. **`src/config.ts` 必填欄位**：`site / title / description / author` 不能空白，且 `site` 必須以 `http` 開頭。

---

## 三、目前保留的客製化（升級主題時要逐項補回）

| # | 內容 | 檔案 |
|---|---|---|
| 1 | 網站標題下方顯示副標題（description） | `src/components/Header.astro` |
| 2 | 目錄（TOC）每項單行、過長以「…」截斷 | `src/components/TableOfContents.astro` |
| 3 | 腳註懸浮卡片（滑過腳註顯示內容） | `src/components/RefNoteCard.astro`（自建）＋ `src/layouts/BaseLayout.astro` 引入兩行 |
| 4 | 中文腳註錨點修正（`[^中文標籤]` 不被轉壞） | `src/utils/rehype-normalize-anchors.ts` |
| 5 | 文章置頂 `pinned: true` | `src/content.config.ts`（schema）＋ `src/utils/markdown.ts`（排序） |
| 6 | 拿掉文章列表的 RSS／Atom 按鈕（`/rss.xml` 仍存在） | `src/pages/posts/index.astro`、`[page].astro`、`tag/[...tag].astro` |
| 7 | robots.txt／llms.txt 網址補斜線（避免變成 `tzulungchang.comsitemap.xml`） | `src/pages/robots.txt.ts`、`src/pages/llms.txt.ts` |
| 8 | CSS：內文左右對齊；所有內文連結（站內 wikilink 與站外）一律實線底線；引文精簡樣式 | `src/styles/global.css` 最後面 |
| 9 | 內文寬度 40rem（原版 45rem） | `src/config.ts` 的 `layout.contentWidth` |
| 10 | 建置結果比對工具（升級前後比對頁面有沒有變） | `scripts/build-fingerprint.mjs`（自建） |
| 11 | llms.txt 改寫成正確的中文網站介紹（給 AI 讀） | `src/pages/llms.txt.ts` |
| 12 | 臉書同步輔助程式 | `scripts/fbsync.py`（自建），規格見 `src/content/_sync/同步說明.md` |
| 13 | 共用區塊 `![[代號]]`（`src/content/_sync/共用區塊/`）在網站上展開；「提到這篇的文章」也計入共用區塊裡的連結 | `src/utils/remark-shared-blocks.ts`（自建）＋ `astro.config.mjs` 排第一的 remark 外掛 ＋ `src/utils/internallinks.ts` 的 `findLinkedMentions` |
| 14 | 關閉 smartypants：`--`、`...` 照原文顯示，不轉成破折號、省略號 | `astro.config.mjs` 的 `smartypants: false` |
| 15 | Docs 支援 wikilink 與「提到這篇的文章」：`[[YYMMDD]]` 若是 docs（含分類資料夾）裡的檔案就連到 `/docs/分類/YYMMDD`；比對引用時用檔名；Docs 頁面加上 LinkedMentions | `src/utils/internallinks.ts`（`findDocPath`、`findLinkedMentions`）、`src/components/LinkedMentions.astro`（`collection` 參數）、`src/layouts/DocumentationLayout.astro` |
| 16 | Docs 清單卡片遵守 `hideCoverImage: true`（不顯示縮圖，只用於分享預覽圖），避免只有少數文章有圖時排版參差 | `src/components/DocumentationCard.astro` |

其他設定值（站名、導覽、社群連結、主題 charcoal、作者「張子龍」等）都在 `src/config.ts`，升級時沿用。

文章與 Docs 底部的「提到這篇的文章」（`postOptions.linkedMentions.enabled: true`，2026-10-27 開啟）配合臉書同步使用；站內搜尋也包含 Docs。

### 臉書同步
- 臉書貼文放 `src/content/docs/分類/YYMMDD.md`（檔名＝發文日期碼，資料夾＝分類：辯論、表達、觀點、閱讀、生活）；圖片在 `src/content/docs/attachments/`；`posts` 留給整理完成的文章。
- Obsidian 新增文章的範本（Astro Composer、Vault CMS 兩個外掛）已精簡成只留必要欄位（2026-10-27）。
- `src/content/_sync/` 放流程說明（同步說明.md）、貼文索引、共用區塊（L 清單／S 系列／T 主題／A AI 精選）、待貼留言；貼文索引也記錄最新的臉書洞察數字（瀏覽、互動、新追蹤、收益）；這個資料夾不會出現在網站上。
- 流程規格：`src/content/_sync/同步說明.md`。

已移除：Cusdis 留言（2026-10-27 作廢，`GiscusComments.astro` 恢復原版，留言開關目前關閉）。

### 肖像圖（About、jci、Judge 共用）
- 原始檔：`src/content/pages/attachments/portrait.svg`（文字檔，可直接編輯原始碼）。
- 建置時自動複製到 `/pages/attachments/portrait.svg`，頁面用 `<img src="/pages/attachments/portrait.svg">` 引用。換圖只要換這一個檔。

### ⚠️ Astro Modular Settings 外掛
- 這個 Obsidian 外掛會用它自己存的設定**整份覆寫** `src/config.ts`。2026-10-27 已把它存的值同步成正確設定（網址、作者、語言、導覽、留言關閉）。
- 之後**選一種方式改設定就好**：手改 `config.ts`，或只用外掛。不要兩邊都改。

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

- `node_modules` 很大且已被 `.gitignore` 忽略——不要 commit。
- 不要刪掉內容類型資料夾（posts / projects / docs / special），就算空的也別刪，否則建置 ENOENT 失敗。
- 改 CSS「沒效果」時，先確認是看**線上**還是**本地**：線上要 push＋等 Cloudflare 建置成功＋瀏覽器 `Ctrl/Cmd+Shift+R`；本地 `pnpm dev` 存檔即時更新。

---

## 六、更新主題的方式

**不要直接執行 `pnpm run update`。** 官方指令會用新版覆蓋所有框架檔案，只保留 `src/content` 和幾張圖，上面第三節的客製會全部消失。

建議做法：開新對話，把這份 README 貼給 Claude，說「更新主題」。流程是：
1. 以新版為底，用三方合併（舊原版／你的版本／新原版）把第三節的客製逐項套回去。
2. 在雲端建置，確認講義頁、About、互動工具、客製項目都正常。
3. 把變更寫回這個資料夾，由 Obsidian Git 同步上線。
4. 更新這份 README 的版本號與客製表。

想自己判斷要不要更新：看原版的 commit 紀錄 https://github.com/davidvkimball/astro-modular/commits 。沒有你需要的新功能或安全修正，就不必常更新。

---

## 七、未來開新對話怎麼快速跟上

1. **把這份文件貼給 Claude**（最快）。
2. 視問題額外貼上相關檔案：樣式 → `src/styles/global.css`；設定 → `src/config.ts`；排序/置頂 → `src/utils/markdown.ts`、`src/content.config.ts`。
3. 想知道到底改了哪些：在專案資料夾執行 `git log --stat`。
