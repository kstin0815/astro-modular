import type { APIRoute } from "astro";
import { siteConfig } from "../config";

export const GET: APIRoute = async () => {
  const siteUrl = (import.meta.env.SITE || siteConfig.site).replace(/\/?$/, "/");

  const llmsTxt = `# ${siteConfig.title}

> ${siteConfig.description}

這是張子龍（LungLung0815）的個人網站與知識庫。張子龍是華語辯論的教練與評審，自 2007 年參與校園辯論至今。

## 內容

- 筆記（${siteUrl}docs/）：臉書長文的備份，主題以辯論（教學、評判、理論與辯論史）、寫作與表達、閱讀與個人思考為主，依年份分類。每篇的網址是發文日期（例如 /docs/261025 是 2026-10-25 的文章），並附臉書原文連結。
- 文章（${siteUrl}posts/）：整理完成的文章。
- 每篇文章底部的「相關文章」是作者整理的延伸閱讀：「前後篇」是同一系列的前作與續作，其餘區塊是相關主題或聯想；「提到這篇的文章」是自動反查的引用。要理解作者對某個主題的完整想法，可以沿著這些連結閱讀。
- 關於（${siteUrl}about/）

## 網站資訊

- 網址：${siteUrl}
- 作者：${siteConfig.author}
- 語言：繁體中文（${siteConfig.language}）
- RSS：${siteUrl}rss.xml
- 網站地圖：${siteUrl}sitemap.xml
`;

  return new Response(llmsTxt, {
    headers: {
      "Content-Type": "text/plain",
      "Cache-Control": "public, max-age=86400", // Cache for 24 hours
    },
  });
};
