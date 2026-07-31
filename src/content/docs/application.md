---
title: Application
description: AI協作過程回顧
category: AI
order: 3
version:
lastModified: 2026-07-31
image:
imageAlt:
hideCoverImage: false
hideTOC: false
draft: false
featured: true
aliases:
  - workflow 1
---
## 流程

### ▌與AI對話的後設分析與回饋循環。  
  
最近在跟AI對話的時候，都會習慣加一段「後設分析」的指示在最後。  
  
例如：『我希望同時讓這次的討論也成為「與AI對話」的案例，所以請在每次回應最後，除了正在討論的當前內容之外，也以後設角度整理和分析我們的討論，包含：⑴我的對話和提問以及任務提示和回饋有哪些特點和缺失又能如何加強和彌補，⑵你的回應又有哪些問題有什麼多餘的考量和漏掉的因素及限制，⑶我們又如何能在此次對話和未來的任務加以避免。』  
  
然後，這是剛剛獲得的回應。  
  
它說我回應的優點是「分流輸出」：把不重要的議題擱置、Q2 判定為不重要、Q3 提為關鍵。這是很有效率的協作行為——你沒有讓我重做任何一塊，而是直接指定深挖點。  
  
然後，缺點是：你的推進其實有五步（Q2 降權 → Q3/Q4 連動 → Q3 提為關鍵 → 對應 Q1 提案 → 指出侷限 → 兩個子問題），全部塞在一個沒有斷點的段落裡。我可以解析，但這增加了我誤判權重的機率——例如我差點把 Q1 提案當成你的結論而不是待檢驗的提案。你在貼文裡用編號用得很好，跟我對話時反而不用。  
  
真的是，我明明每次都有清空紀錄，這性格是哪跑出來的？

---

### ▌昨天用 AI 搭了一個「個人網站」。

從以前的`無名`、Blogger，再到後來的 Medium 和`方格子`，我想擁有一個「可以長久存放和經營內容的平台」其實已經很久了。但儘管直到最近，我都還是只在社群平台發表文章。

——短的放[臉書](https://www.facebook.com/lunglung0815/)，長的放[知乎](https://www.zhihu.com/people/zhang-zi-long-44)。

但，社群平台的缺點，我們都明白：⑴不是自己的，這最直接；⑵不能很好的組織和保存是第二個原因，或許也是最重要的原因——在臉書，我會用「在留言手動附上連結」的方式，土法煉鋼做出「`雙向連結`」來模仿卡片盒筆記（`Zettelkasten`）。但模仿終究是模仿而且臉書的搜尋功能，除了「爛透了」之外，我實在不知道還能有什麼更客氣的說法。

但臉書終究有其優點，或者說，像 [Obsidian](https://obsidian.md/) 這樣的筆記軟體，也有其缺點：沒有「對話感」而終究要不只會留下許多的破碎的片段，要不會為了完成一部所謂傑作而永遠也無法完成。反倒，是臉書和知乎，這樣具備社交屬性的平台，才能剛剛好地，不上不下地，讓我能輕鬆完成一些儘管事後難以進一步加工完善，但也至少是完成了的一些產出。

□

所以，我需要想到一個好的辦法，以「去蕪存菁」：取兩者之長，讓我可以快速完成「作品」，而又保有後續的可延展性；去兩者之短，讓我不會生成即用而也用完即丟的積灰塵，另一個極端的永遠沒法完成而從一開始就是灰塵——我思考工具和方法，也思考更根本的筆記原則，然後發現至少在這個領域，幾乎所有工具都是為了特定理念而生：例如，[Quartz](https://quartz.jzhao.xyz/) 和「[數位花園](https://jzhao.xyz/posts/networked-thought)」或就是 Obsidian 的最廣義和「基進（radical）」的「去中心化」，儘管最後並沒有選擇 Quartz 我還是認真讀了作者的好幾篇筆記，也很喜歡他的這句引用：

> “[One] who works with the door open gets all kinds of interruptions, but [they] also occasionally gets clues as to what the world is and what might be important.” — Richard Hamming

但這對我來說，並不足夠：如果只是要敞開大門，我的臉書可說是最雜草叢生又富有生命力的花園了，但我卻始終無法從中澆灌出什麼。至於 Obsidian，它們更是不斷的翻土卻從來沒有播種，種籽是收集了很多，但最終也都風乾了。

——只是，在觀察這些「將『筆記』視為『花園』甚至直接賦予「植物生長隱喻」的分類時，我忽然被 seedling、budding、evergreen、（pillar）的最後一個並非所有人都接受的概念所吸引……：它讓我想到，evergreen note 也就是「常青筆記」的最初倡導人 [Andy Matuschak](https://andymatuschak.org/) 前兩年寫的一篇名為〈[常青笔记的五年历程](https://zhuanlan.zhihu.com/p/720767259)〉的文章。

在那篇文章中，他提到：

> 在开启我的笔记写作实践后不久，我开始为赞助人撰写月度文章。这为我的写作和思考提供了一个新的环境，比起工作笔记，它的要求更高，内容更为丰富，但相较于那些更为严肃的主要文章，难度又相对较低。在过去的五年里，我在这些月度赞助人文章中累计写作了逾 15 万字。通过这些持续的写作实践，我的写作能力和自信心都得到了显著提升。最初，我需要借助笔记这个「脚手架」来拓展有限的想法。而现在，我已经能够在写作过程中自如地发展新的想法。准备性的笔记似乎变得不那么必要了。如果我能够直接在文章中阐述想法，我自然会选择这样做：[因为这样的作品通常会更加生动、直接，也更加真实](https://sashachapin.substack.com/p/notes-against-note-taking-systems)。

儘管，這看似一個「對過去」的揚棄，我卻更想到，他的另外兩篇，互有關聯但卻沒有被整合的筆記，分別是〈[在写作时创建推测性大纲](https://zhuanlan.zhihu.com/p/446450875)〉以及〈[§ 笔记写作系统](https://zhuanlan.zhihu.com/p/446450875)〉——後者，就是前者的成果，一份由近半百個筆記，所組成的要點大綱。而得益於「`每写一条新笔记时，把它添加到你正在维护的一个或多个大纲中，有必要的话也可以创建新的大纲。非常完整的写作项目会自然从中涌现。`」——比較，他前後「兩篇文章」的想法，我想，我們不難看出答案：之所以，有那麼多的僅僅「萌芽」而無法常青；或僅僅「拾穗」卻無法播種，其根源其實在於「沒有支柱（pillar）作為目標」——只有在那三、五根支柱，所撐起和反哺的天空，這一切的耕耘「gleaning、seedling、budding、evergreen」才或許能有意義。

□

網站，當然「是用 AI」架的。

但不是讓它直接弄好，而是讓 AI 一步步帶著我做。

一來，想順便學點東西，二來，是意外發現還挺簡單和有趣的。首先，網站是用 [Astro Modular](https://astro.build/themes/details/astro-modular/) 架的：Astro Modular 是 [Astro](https://astro.build/) 的一個主題，Astro 則是一個「以內容為中心的」的現代網頁框架：根據AI給我的說法，一個網站就像一本書，你可以自己一個字一個字刻好手工印拓，也可以寫好草稿就丟給工廠去排版印刷。

——而像 Astro 這樣的框架，就是有著自己一套印刷規則的印刷廠，既是生成器也是網頁框架：以「內容為中心」的意思，則是它更適合生成「靜態」的網站，也就是印好後就不管你了，每個讀者拿到的都是同一個一模模一樣樣的那一本書，而不像動態網站那樣，每個讀者只會拿到暫定本，如果不滿意或在上面寫了些什麼，就會有小精靈千里傳音跑回伺服器，然後伺服器再趕快根據他的反饋，印出符合他條件的那一本書。

至於 Astro Modular，則是 Astro 這間印刷廠中，一個特別的版型，或甚至是一套出版流程：以我的例子來說，我是依照 Astro Modular 作者在 [GitHub儲存庫](https://github.com/davidvkimball/astro-modular)的指示，在 Quick Start 直接選擇把網站部署到 Cloudflare——此時，你需要確保幾件事情：⑴有一個 [GitHub](https://github.com/) 帳號、⑵一個 [Cloudflare](https://www.cloudflare.com/) 帳號而能自動在你的 GitHub 複製一個儲存庫，再透過 Cloudflare 部署、生成一個可以公開瀏覽的網址。

然後，視個人情況不同，你可能還會需要安裝：⑶分散式版本控制軟體 [Git](https://git-scm.com/) 把複製在 GitHub 的儲存庫存到本機¹、⑷筆記軟體 [Obsidian](https://obsidian.md/) 用來編輯文件，也就是網頁後台、⑸JavaScript 執行環境 [Node.js](https://nodejs.org/zh-tw/download) 和套件管理器 pnpm：因為 Astro 是用 JavaScript 寫的，所以如果你要在本地預覽網頁就需要安裝它們——但如果你想直接在 GitHub 上編輯，不預覽也不用本機編輯，就其實都不用這些。

`¹ 雖然，按理來說，應該是「GitHub 是用來儲存 Git 的數據庫」才對，但可喜可賀的是我們應該可以不用管那麼多。`

在過程中，我碰到了幾個困難：在透過 Cloudflare 部署時，因為⑴ Astro Modular 要求較新版的 pnpm，但作者並未在文件中指定，導致 Cloudflare 抓了較舊的版本；並且⑵在因應 Astro 7.0 升級時，作者在 config 設定檔新增了一個套件，卻忘了在 json 安裝，導致 Cloudflare 找不到套件而建置失敗——然後，在 Obsidian 打開本地文件時，我又因為⑶沒按照指示打開正確的資料夾而沒有成功觸發設定外掛；接著又因為⑷沒有乖乖填內容，而多次在「網址、描述、作者名稱」等地方空白，導致驗證不過關…。

還好，這些問題都能交給 AI 解決——把 Cloudflare 的 build log 直接貼給 AI 或把整個儲存庫的 config 檔直接貼給它：是的，我甚至只用的是網頁版，而沒有用 Claude Code 或桌面版 Claude Cowork 等花裡胡哨的工具。就這樣浪費 token 的全貼全輸出，也磕磕絆絆的完成了。此外，還做了幾個個人化的調整：⑴用 [Cusdis](https://cusdis.com/) 讓訪客可以匿名提交留言但必須等待審核；⑵增加了文章置頂並刪除了 RSS 和 Atom 訂閱按鈕；⑶調整了字體樣式，像是左右對齊和超連結底線和引文大小等等。最後，就是一邊看對話，回顧整個過程，一邊打出這一篇文章，作為測試和回顧。

---

### ▌每一本書都是一個等待被支解吞噬的架構。

「AI會減損認知能力嗎？」

目前看來，有兩派說法：一派認為會，認為這將導致認知卸載和批判思考能力的下降；但另一派認為「只要你好好用」就不會——潛台詞是：「如果你沒好好用」就有可能還是會。

所以關於「AI會不會減損認知能力」這個問題的答案，或許其實早有結論：會。除非你可以在這個過程中，仍然保有一定程度的思考。但問題是，這其實是很困難的——我是說：你到底要怎麼判斷，自己有沒有「減少思考」呢？

至少對我來說，在與AI對話的過程中，我一直會有一個很詭異的感覺：我感覺我的思考在一方面增加的同時，也在一方面減少了：在思考問題的答案時減少了，不再主動思考可能有哪些解答，而就是把問題丟給AI。甚至是在等待AI回應生成的空檔，還能跑去做其他事情，而完全把問題給拋在腦後，不像以前如果被一個問題困擾，就算在忙其他事情，腦袋裡也還是在不斷高速運轉——某種意義上來說，這或許就是「正念」所追求的最高境界。

但另一方面，我花在思考「問題」的時間，卻很明顯變多了。我會更仔細思考，我的問題到底是什麼？怎麼把模糊的思緒在還沒有想到答案和解決方案之前，就先嘗試著把它描述捕捉出來／以及當然面對AI的回應，我可以依舊保持批判思考的能力，對它的回答挑剔挑出錯誤或哪裡還沒有讓我滿意——不論證，只反駁，就像一直以來我在辯論裡面最喜歡做的事情一樣。但然後想到，建構和解構，卻並不是思考的全部，至少不是辯論所展現的思考的全部。

建構和解構，論證或反駁，最終都還是要被放進「框架」裡檢視：不管我們是要把它理解為「建構、解構、架構」的三分，還是「定義和比較」與「論證和反駁」的兩組四分——在提出問題並批判AI所生成的答案之餘，除了建構的認知被卸載，我們可能還保有組織架構的能力與責任——只要別把AI的答案照單全收。儘管也有人討論，AI所給出的答案，除了即時與扁平之外，更重要的是「不存在任何磨擦」。

就好像那是唯一正確的答案，而使得AI不僅僅是幫你省下自己看書找資料的時間，只不過是跑腿代勞：因為每本書都是一個自成的體系和架構，就像辯論賽的正反方，關鍵不在有正反的立論和辯駁（不僅僅只是彌爾所說，如果沒有經歷激烈而認真的爭論，即便是全面的真理人們也只能以一種偏見的形式接受，而對其理性基礎缺乏理解和感受）——更重要的是，在體系與體系，架構與架構之間，總是存在參差和齟齬而有「磨擦」——事實上就如「定義」其實是一種條件，以及應然對實然的涵攝，建構的因果關係或甚至舉例與類比，也都是每一塊碎片拼圖，能不能被置入一個現成的，或你所主張的框架裡面，然後完成一個整全的圖案。

如何去支解和吞噬既有感受與既成的架構。

---

### ▌最近把跟 AI 協作的框架做了一個大升級。

我最早的 AI 用法很簡單，就是讀書和做筆記。不是請它幫我做筆記，而是讓它讀我的筆記。具體來說，是這樣的：⑴我會把所有相關主題的資料都讀一遍，如果是英文就先丟進免費的 Google AI Studio 請它用 SCQA 摘要全文；⑵然後，我會打一篇落落長的想到哪寫到哪的筆記，再把這個筆記丟給 AI 請它做反向大綱；⑶看著這個我在寫的時候毫無意識的大綱，我再認真沉下氣來好好思考怎麼整理出一個完整的體系架構——就這樣不斷「打碎輸入、重組輸出、擴展再壓縮、再解壓縮」把知識內容反覆錘鍊打磨直到只剩下薄薄一張 A4 紙和上面的簡單樹狀圖和條列式。

但後來紙張越積越多，甚至揉成紙團丟的到處都是，我開始感覺可能需要一個更大的容器和吞吐的裝置，也就是俗濫的所謂第二大腦或個人知識庫。所以嘗試採用了「Claude 桌面版+ Obsidian + MPC」方案，也就是創建一個追蹤進度的 `任務文件.md` 放進 Obsidian，每次討論前先用桌面版和 MPC 的 Combo 叫 AI 讀完文件內容以接續上次的討論進度後再開始。當然其他雜七雜八要給它看的資料也在裡面。總之，就是先看 `任務文件.md` 接續討論進度，有什麼其他要補充哪些的再隨時更新叫它去看——每次討論完再叫它根據結論更新 `任務文件.md` 以及以防萬一我也會要它把每次的討論紀錄，加上摘要用 `YYYY-MM-DD-x.md` 格式全部儲存起來。有時，覺得只看 `任務文件.md` 不夠，就能叫它直接去看之前的紀錄。

但這樣做有一個問題：就是這樣的做法雖然很方便，可以讓我「⑴不用思考每次討論前要整理哪些素材給 AI 讓能它有完整的上下文脈略；⑵也不需要每次都重新給它提示詞和樣本；⑶甚至不用費心整理和記憶結論就能順順地每次從哪裡結束就從哪裡接續下去」。但這依舊都只限於「思考型」的任務——這樣的協作流程，幫我分攤或者說解放了部分思考，而能把更多心力都放在思考或跟它討論更關鍵的問題，但到了真正要把結論給產出時，例如像是現在這篇文字，我依舊只能自己來。

當然，我可以叫 AI 幫我整理結論，也可以跟它討論架構，但這些內容仍然只能給我一個參考，而還是需要我自己進行消化和轉化／而沒辦法像寫程式可以行內聊天編輯的 IDE，例如 Cursor 那樣「一起看著白板」找出有哪邊需要修改，反倒更像是日本的搞笑綜藝節目或機智遊戲挑戰，兩個人在不同房間，一個人用對講機指揮另一個人作業，做到差不多之後再互相交換接手——但我不確定，這意味著我應該學習使用其他工具改變整個協作流程，還是僅僅在最後「要輸出成品時」做一些小小的修正就好了？

於是，當然，我把這問題也拿去問了 AI。

一開始，它推薦了我一套非常愚蠢的方案。它說，它理解「共同看著同一份東西」的即時修改，相較於「我描述→它輸出→我再看→再描述」的輪流交棒模式更流暢，但它依舊困惑『把草稿直接貼進對話、要它在段落層次上動手，再把修改後的版本貼回來——笨是笨了一點，但其實已經比對講機模式好一些。』好一些？我好你個大西瓜。這種做法不只笨，還很慢，而且傳回來的因為每次都是完整修改的版本，光是要搞清楚哪邊有些改就已經夠麻煩。

進一步，它問我，我說的是「寫」本身太麻煩，還是「從結論到成品之間的轉化過程」太模糊？換言之它是在懷疑我是否真的是寫起來太累，還是只是根本沒想清楚就要動筆，而其實在「討論」和「動筆」之間，還需要多一個明確的「結構確認」步驟，讓我在真正開始寫之前就清楚知道每一段要寫什麼——我不否認「跟 AI 對話」是有助於思緒釐清的大致在三個方面：⑴有時，AI 確實能提供明確解答或思考方向；⑵或就算沒有提供解答也能給予刺激；⑶甚至，有時候，光是「用跟他人對話和解釋的形式描述自己的想法」就已經有助於思考，且本來就不一定要真的有一個人——但有些思考還是只能發生在「自己一個人面對把網狀的思維用樹狀的語法以線性展開」如抽絲剝繭又如孤身一人深入險境招安流寇，強迫自己真正去思考概念之間的聯繫和排序，然後才能徹底把握如指臂使。我想，這樣的感受並不特殊，但對大語言模型和它背後所反映收集的人類平均經驗，似乎依舊有一段不小的距離：AI 理解並甚至說出了，這是因為思考需要一個人承擔「不確定」的重量沒辦法外包，因為摩擦感本身就是思考正在發生的證明。但它卻以為我需要的是在思考過程中卡住，不知道兩個概念之間的關係如何連結時，能夠隨時切出來跟它討論，再回去繼續展開。

然而，在卡住的時候，一個人是甚至說不出「我在這裡卡住了，我現在的想法是這樣，但我不確定它和前面那個論點怎麼接」的，他頂多可能可以有一個比較模糊的表達，先暫時填充然後就要繼續往下，沒有這樣的果敢你永遠無法抵達思緒的盡頭。而有了 AI 可能有的幫助頂多是可以請求 AI 針對填充段落直接給出幾種可能發展，近乎觀落陰的把你也不知道你在想什麼的內容給猜出來。但如果 AI 無法理解，也就無法依據這個給出建議：到底是要整個遷移？還是在最後增加一個轉換例如把結論文件用 Cursor 打開？或是從「Claude 桌面版 + Obsidian + MCP」升級成「Claude Code + Obsidian」的混搭？對於這些問題，它先又推薦了我已經用過但覺得沒什麼用的 Obsidian Copilot 才開始指導我裝 Claude Code ——然後才發現根本雞同鴨講，原來 Claude Code 並不能直接實現行內聊天的內嵌編輯，所幸直接叫它上網，才又找到了一個叫 Claudian 的 Obsidian 社區插件。

於是，我現在不只可以在 Obsidian 側邊欄，直接叫出 Claude Code 的對話框針對目前正在寫的文章進行討論，還能選中一段文字，對於我卡住不知道怎麼表達只能暫時用模糊囈語填充，或是懶得展開解釋的段落請它幫我改寫代勞或給予啟發，例如：……。沒錯，我寫這篇時候完全沒有卡住，也沒覺得有什麼我懶得解釋的東西值得展開，除非你覺得「Claude 桌面版 + Obsidian + MCP」被寫成「Claude 桌面版是 Anthropic 官方推出的本地端應用程式，讓 Claude 能透過工具直接存取本機資源；Obsidian 是以 Markdown 純文字檔案為基底的本地知識庫軟體，所有筆記都儲存在自己的電腦裡；MCP（Model Context Protocol，模型上下文協定）則是串起兩者的橋樑——透過這個協定，Claude 桌面版能直接讀取 Obsidian 資料夾中的 `.md` 檔案，讓對話不再缺乏上下文脈絡，每次開啟都能從上次的進度繼續」有任何現實意義。

我是覺得沒有啦，但總之反正就是先這樣子。

最後，不得不吐槽的是：Claude Desktop + MCP 設置有夠麻煩，Claude Code + Claudian 簡單多了。但 AI 還說後者學習成本太高，建議我先用前者，簡直是莫名其妙——但額外發現的好處是，後者必定要綁定付費帳號，前者並不綁定，而且可以好幾個輪流切換，所以也就不跟他計較了！

---

### 【AI知識庫管理：Claude Code vs Desktop】

AI用久，真的有時會讓人想到帶學弟妹——討論不做筆記，每次都要重新上演：「我是誰？我在哪？我們現在要幹嘛！」

所以只好你幫他做好筆記叫他滾回家去讀。

常見做法有幾種：⑴把本來拿來寫程式的整合開發環境像Cursor拿來管理文件；⑵用MCP搭配像Claude桌面版連接個人知識庫；⑶或乾脆就直接用Claude Code接管電腦還能學Skill。

Claude桌面版遷移成本最小，只是讓你能在聊天時直接叫AI去讀你的文件資料夾，但設置麻煩且討論整理儘管順暢真正要動筆時「你描述→它輸出→你看完→再描述」的過程依舊是一種折磨。

Cursor也很直覺但收費令人困惑；Claude Code的終端介面很勸退，搭配Obsidian插件雖然直逼Cursor卻不知為何遠沒有桌面版那麼絲滑。

而且，桌面版還有一個令人意外的隱藏優勢。

——明明要官網登入卻不擋你一直切帳號XD

--

［Claude 桌面版 + MCP］

• Obsidian（筆記管理軟體）
https://obsidian.md
• Local REST API（Obsidian 插件）
https://github.com/coddingtonbear/obsidian-local-rest-api
• Claude Desktop（廢話！）
https://claude.com/download
• Node.js（MCP 執行環境）
https://nodejs.org/zh-tw/download
• Python（執行 mcp-obsidian）
https://www.python.org/downloads
• uv（Python 套件管理工具）
https://github.com/astral-sh/uv
• mcp-obsidian（MCP 伺服器）
https://github.com/MarkusPfundstein/mcp-obsidian

然後去改 Claude Desktop 的 config 檔案。
（要記得 uv tool install mcp-obsidian...）

--

［Claude Code + Claudian］

• Obsidian（筆記管理軟體）
https://obsidian.md
• Git Bash（Claude Code 環境）
https://git-scm.com/install/windows
• Claude Code（廢話！）
https://code.claude.com/docs
• Claudian（Obsidian 插件）
https://github.com/YishenTu/claudian

終端 cd 文件路徑，然後 claude 登錄帳號。

---

### ▌紀錄一下用AI整理筆記的流程。

首先，是閱讀。我以前就喜歡在從頭到尾通讀之前，先看目錄和略讀。因為閱讀速度夠快，所以基本十來分鐘就能掌握大致內容，然後決定要不要仔細看，還是只挑重點段落來看。但英文就沒有辦法了，所以我會用三個階段的指令用AI輔助閱讀：全文和章節摘要，特定章節和段落的詳細摘要。

1. 請以SCQA結構，對全文和各章節進行摘要。
2. 請對「第X章 or XX概念」進行更詳細摘要。
3. 請依原文順序，對「XX節」各段落進行摘要。

其次，是組織。我始終迷戀像是堆積木一樣，把散亂的概念組織成有體系的架構，然後再把架構打散分類重組。而因為這個動作本身就充滿了樂趣，所以我不會讓AI代勞(X)／不會讓它剝奪我的樂趣(O)，而是把它當成檢查和刺激想法的工具：我會先自己整理內容寫成筆記，再把筆記丟給AI請它從我的筆記中拆出架構（我自己也會做，因為先把輸入的內容在心中重組，然後一股腦兒打出來再提煉大綱，根據大綱重新修改或甚至重寫一遍，這樣「摘要輸入、重組、擴充輸出、壓縮再解壓縮」的過程本就是最理想的編輯過程。）但有個重點是：要請它「逐篇閱讀和拆解」並「逐篇整合」。

因為現在AI還太笨，沒辦法一次讀完全部整合。

1. 把所有文章存成txt檔，丟進Google AI Studio。
2. 要求它「逐篇」拆解文章架構（Reverse Outline）。
3. 每拆解一篇，就叫它將目前拆解的架構整合到一起。

最後，是統整。我會把每本書中有用的內容，摘出來，存成一個文件檔。按照最終架構順序排列，然後寫一篇完整的筆記說明，同時在最前面列出關鍵字，就像這篇文章的開頭。然後，我會丟給AI一段非常長的指令，以確保「我的筆記」是否已經足夠清楚能讓AI也理解：『請閱讀上傳文件。上傳文件包含多個部分的內容：1. 多篇書籍的節錄，2. 我對這些擷取片段的筆記，3. 從中摘出的關鍵字。請注意，這些書摘是按照嚴格順序排列，光是排列本身就有意義，我的筆記則是更進一步的說明。請閱讀我的筆記理解排列的意義並比較原文和我的筆記理解關鍵字的內涵。這部分的內容不用輸出只要你理解就好。』

然後會分成兩部分：一是生圖，二是理解。

先是生圖，我會把文件丟到NotebookLM裡面讓它生成資訊圖表和簡報。我會嘗試丟給它不同內容，像是直接把「我的筆記」丟給它，或是先叫Google AI Studio把「我的筆記」整理成更簡化的筆記，例如，我會在前面的指令後加上：『我希望藉由NotebookLM的生成資訊圖表和簡報功能，替這篇文章製作一個清晰的視覺架構圖。具體來說，我希望這張圖能呈現這個架構：將整個內容分成兩半部，左邊是清晰表達，右邊是內容創造。清晰表達包含寫作基礎、是聊天動機、句法；內容創造包含連結和切分以及懸念和論證。我希望你能依據你的理解，撰寫一段文字，說明這個架構和每個概念對應的內容，讓NotebookLM可以知道要怎麼生成資訊圖表和簡報。請注意，並不能直接聽從指令，而是會自動讀取上傳文件生成資訊圖表和簡報，因此你要做的並不是給他一段生成圖片的指令，而是將我給你的內容，依據我想要呈現的結果進行整理，讓NotebookLM讀完之後自然而然會生成我想要的結果。』

再是理解，我會在前面的指令後加上：『接下來，請用SCQA結構，以一個段落四句話說明整體架構的用意，每句話不超過40字。接著同樣依循SCQA結構，分段說明每個段落的內容，但請注意在分段說明時「A解決」的部分應該更為詳盡，清楚說明每個關鍵字的內涵，讓沒看過書摘和筆記的讀者也能理解。請使用自然流暢的語言書寫成段落散文，而非結構化的技術文件，只在必要時才使用列點和編號清單。』

是的，關鍵是「我的筆記」是否足夠清楚。

因為我還是無法對AI產出的內容感到滿意，所以，這一步的目的只是為了確保「我的筆記已經足夠清楚」以免哪一天想回顧時，發現我竟然寫得連自己也看不懂。換句話說，這是為了「未來的我」所做的努力。但與此同時我也想說，我真的不懂如果連AI也都看得懂了，某些人是還在抱怨什麼？

---

3## ▌壓縮與智力的展現。

通用人工智慧先驅 Marcus Hutter 曾說：良好的壓縮與智能密切相關。因而把「無損壓縮率」作為了衡量智慧高低的硬性指標。又或者，就像塔雷伯說的，你應該要能在讀完一本書之後用一句話總結然後再從這句話反推出整本書。

這有點像是模擬賽局，只要幾條簡單的規則和初始設置，我們就能重現整個複雜的賽局模型迭代演化的過程；又或像是類型學的分析，只要確定了共通邏輯和變量，就能透過簡單調整變量的方式，在多維度的空間定位所有概念。

所以我也總是以此盡可能壓縮所學的資訊。

只是人類的壓縮往往會出問題，而且是兩個問題：一是，分享壓縮後的資訊簡單，但分享規律很難。二是，有時候他媽的自己也忘了。還好在通用人工智慧發展下，我們終於有救了。

不是讓AI解壓縮，而是進行一個雙向工程。

--

▌文本壓縮和解壓縮。

請閱讀上傳文件和要點，並執行指示：

1. 要點我是對上傳文件的壓縮和重新整理。
2. 但對沒讀過文件的人來說可能太過精簡。
3. 所以我需要你根據文件內容進行解壓縮。

解壓縮原則：

1. 對象是沒讀過文件只能讀要點和簡介的人。
2. 請提供一個整合的框架說明文件核心內容。
3. 解釋概念之間聯繫並補充要點簡化的內容。
4. 請記住不是你要寫一份對文件的整體總結。
5. 而是針對要點不足寫一份完整的補充說明。
6. 以「說明和介紹並補充要點」的口吻說明。

請特別注意：

1. 請完全遵循要點架構而非文件進行擴寫。
2. 請只根據文件擴寫不要有任何你的詮釋。
3. 請想像是以文件素材和要點架構寫文章。

▌解壓縮的成效檢查。

很好，我們來檢查一下成果：

1. 假設你只讀過要點和簡介。
2. 從這個視角評估你的簡介。
	- 是否能讓讀者準確理解文件的核心內容？
	- 是否彌補了要點可能存在的簡化或遺漏？
3. 明確指出簡介的不足之處。
4. 基於反思修改並完善簡介。

請注意：

1. 簡介應當是連貫的說明文而非更長的要點。
2. 不應逐項解釋要點內容而要提供整體視角。
3. 但應該符合要點的架構幫助讀者理解要點。
4. 請記得這些讀者沒有機會讀到文件的內容。
5. 不應對沒機會讀到文件的人提到文件存在。

---

3## ▌紀錄一下用AI整理筆記的流程。

首先，是閱讀。我以前就喜歡在從頭到尾通讀之前，先看目錄和略讀。因為閱讀速度夠快，所以基本十來分鐘就能掌握大致內容，然後決定要不要仔細看，還是只挑重點段落來看。但英文就沒有辦法了，所以我會用三個階段的指令用AI輔助閱讀：全文和章節摘要，特定章節和段落的詳細摘要。

1. 請以SCQA結構，對全文和各章節進行摘要。
2. 請對「第X章 or XX概念」進行更詳細摘要。
3. 請依原文順序，對「XX節」各段落進行摘要。

其次，是組織。我始終迷戀像是堆積木一樣，把散亂的概念組織成有體系的架構，然後再把架構打散分類重組。而因為這個動作本身就充滿了樂趣，所以我不會讓AI代勞(X)／不會讓它剝奪我的樂趣(O)，而是把它當成檢查和刺激想法的工具：我會先自己整理內容寫成筆記，再把筆記丟給AI請它從我的筆記中拆出架構（我自己也會做，因為先把輸入的內容在心中重組，然後一股腦兒打出來再提煉大綱，根據大綱重新修改或甚至重寫一遍，這樣「摘要輸入、重組、擴充輸出、壓縮再解壓縮」的過程本就是最理想的編輯過程。）但有個重點是：要請它「逐篇閱讀和拆解」並「逐篇整合」。

因為現在AI還太笨，沒辦法一次讀完全部整合。

1. 把所有文章存成txt檔，丟進Google AI Studio。
2. 要求它「逐篇」拆解文章架構（Reverse Outline）。
3. 每拆解一篇，就叫它將目前拆解的架構整合到一起。

最後，是統整。我會把每本書中有用的內容，摘出來，存成一個文件檔。按照最終架構順序排列，然後寫一篇完整的筆記說明，同時在最前面列出關鍵字，就像這篇文章的開頭。然後，我會丟給AI一段非常長的指令，以確保「我的筆記」是否已經足夠清楚能讓AI也理解：『請閱讀上傳文件。上傳文件包含多個部分的內容：1. 多篇書籍的節錄，2. 我對這些擷取片段的筆記，3. 從中摘出的關鍵字。請注意，這些書摘是按照嚴格順序排列，光是排列本身就有意義，我的筆記則是更進一步的說明。請閱讀我的筆記理解排列的意義並比較原文和我的筆記理解關鍵字的內涵。這部分的內容不用輸出只要你理解就好。』

然後會分成兩部分：一是生圖，二是理解。

先是生圖，我會把文件丟到NotebookLM裡面讓它生成資訊圖表和簡報。我會嘗試丟給它不同內容，像是直接把「我的筆記」丟給它，或是先叫Google AI Studio把「我的筆記」整理成更簡化的筆記，例如，我會在前面的指令後加上：『我希望藉由NotebookLM的生成資訊圖表和簡報功能，替這篇文章製作一個清晰的視覺架構圖。具體來說，我希望這張圖能呈現這個架構：將整個內容分成兩半部，左邊是清晰表達，右邊是內容創造。清晰表達包含寫作基礎、是聊天動機、句法；內容創造包含連結和切分以及懸念和論證。我希望你能依據你的理解，撰寫一段文字，說明這個架構和每個概念對應的內容，讓NotebookLM可以知道要怎麼生成資訊圖表和簡報。請注意，並不能直接聽從指令，而是會自動讀取上傳文件生成資訊圖表和簡報，因此你要做的並不是給他一段生成圖片的指令，而是將我給你的內容，依據我想要呈現的結果進行整理，讓NotebookLM讀完之後自然而然會生成我想要的結果。』

再是理解，我會在前面的指令後加上：『接下來，請用SCQA結構，以一個段落四句話說明整體架構的用意，每句話不超過40字。接著同樣依循SCQA結構，分段說明每個段落的內容，但請注意在分段說明時「A解決」的部分應該更為詳盡，清楚說明每個關鍵字的內涵，讓沒看過書摘和筆記的讀者也能理解。請使用自然流暢的語言書寫成段落散文，而非結構化的技術文件，只在必要時才使用列點和編號清單。』

是的，關鍵是「我的筆記」是否足夠清楚。

因為我還是無法對AI產出的內容感到滿意，所以，這一步的目的只是為了確保「我的筆記已經足夠清楚」以免哪一天想回顧時，發現我竟然寫得連自己也看不懂。換句話說，這是為了「未來的我」所做的努力。但與此同時我也想說，我真的不懂如果連AI也都看得懂了，某些人是還在抱怨什麼？

---

### 「怎麼用AI提升寫作效率？」

▌一、讓AI當編輯，我寫它改。

最開始，沒加提示詞，效果很差。
試了網路說的角色和情境，依舊不滿意。

最後索性，把整套自媒體寫作課丟給它，
讓它好好學當作提示詞，結果還算可以。

但就只能寫那種風格的東西了。

▌二、讓AI當作者，我請它寫。

然後試著直接叫AI寫，慘不忍睹。

ChatGPT 愛瞎掰，DeepSeek 愛秀文彩，
Kimi 還有 Gemini 都有夠呆…，
只有 Claude 勉強還可用。

再清楚的角色、情境、目標、受眾…，
甚至，直接擬大綱給參考，也都一樣。

最後只好祭出大絕：別寫了，摘要吧！

比如寫心得，我直接給它整本書，再給出明確大綱和方向，讓它摘要和評價。看似有起色，但反覆檢查幾遍之後，我還是無法接受和信任它的品質。說到這不得不說：很多人擔心AI會取代人類，在我看來根本只是他們要求太低。

（就算偶有亮點，也需要品味去篩選。）

▌三、讓AI當讀者，我寫給它看。

最後是目前為止最滿意，也最意外的。不要它改，也不要它寫，甚至不要它模仿和摘要，只要求它扮演一個讀者告訴我：它讀到了什麼？如果它沒懂，我就回去檢討重改自我反省…。

因為只有笨蛋，才會在溝通出問題時，都覺得是別人沒搞懂或沒有講清楚，而從來不會反省是不是自己的問題，就像在網路上的多數人。

以及我相信網路上的大多數人都比AI還笨；
如果連AI都看不懂，很明顯他們也不會懂。

---

 ▌與AI對話的後設分析與回饋循環。260731
 
▌昨天用 AI 搭了一個「個人網站」。260629
https://www.facebook.com/lunglung0815/posts/27908753328717707

▌每一本書都是一個等待被支解吞噬的架構。260605
https://www.facebook.com/lunglung0815/posts/27617238604535849

▌最近把跟 AI 協作的框架做了一個大升級。260224
https://www.facebook.com/lunglung0815/posts/26459135733679481

【AI知識庫管理：Claude Code vs Desktop】260224
https://www.facebook.com/lunglung0815/posts/26457358860523835

▌紀錄一下用AI整理筆記的流程。251222
https://www.facebook.com/lunglung0815/posts/25895347226725004

▌壓縮與智力的展現。250325
https://www.facebook.com/lunglung0815/posts/9878870012132648

「怎麼用AI提升寫作效率？」250211
https://www.facebook.com/lunglung0815/posts/9615793015107017

---

## 案例

### ▌用AI做了一個視覺化的戰場工具。

https://tzulungchang.com/argument_mapping

一些前提的知識：所有論點，都要有論證。如果沒立住，或被擊倒，就沒資格進行比較。口說無憑，或在樣本上以偏概全，而在資料上空口說白話或在推論上草率歸因使論證出了問題，而就有可能面臨質疑和削弱，甚至被擊倒——當然，通常來說，要「證明一件事情有可能」遠比「證明不可能」簡單的多，所以除非在「因果關係」上出了大問題，例如倒果為因或複合結果或交互作用，或甚至是反效果，不然再多不充分和不必要或不必然和不唯一也都只能削弱可能，而不能徹底擊倒，除非你能從「比較」的角度，提出替代政策或相應弊害，而徹底「擊倒一個論點」而非論證。

但即便「論證本身」沒問題，我們也還要思考兩件事情：⑴它的成立程度有多少呢？很有可能為真？還是，也不是沒有可能為真？⑵它所討論的對象，又真的是我們一開始所關心的嗎？還是有人魚目混珠或指鹿為馬呢？以及，這些看似個別獨立的論點，有沒有可能其實是同一個論點的子論點？只有考慮了這兩個問題之後，我們才能放心把一個成功立住而沒被擊倒的論點放入名為「戰場」的棋盤之中，以帶著「類別」和「分數」的旗子之姿。

首先，論證和反駁；然後，定義與合題；接著，可以被放入戰場之中。

在「argument_mapping」的工具中，我們有幾個操作可以選擇：⑴我們可以選中，在正反論點區中，既已成立並且合題的論點，編輯它們的類別和名稱並加減分數，分數就是我們判斷論點的成立強度，類別是通分和排序的前提；然後，儲存或刪除，或點選其他地方取消選擇；或如果候選區沒有你要的論點，也可以點擊上方新增論點並同樣儲存，或點擊空排自動取消；⑵再來，選中的論點可以自由拖拉進戰場橫列，但要注意第一個論點一旦進去之後之後就會鎖定只有同類論點可以進來，不管是己方論點或對方論點亦然；當然，你可以拖放到其他格，或是雙擊兩下讓它自動歸位回到論點區——已經在戰場中的論點不能更改類別和名稱，但可以調整數值，以反映畢竟辯論賽是動態的競技活動，儘管已經進入了「整理」階段也沒人規定你不能回去繼續打攻防，去強化或削弱己方與對方的論點；⑶在分類與結算之外，我們還可以拖曳橫列的順序，因為雖然地圖是共時性的呈現，我們瞬見就能一目了然掌握戰場全局，但是辯論畢竟是口語的歷時性活動，在將地圖轉化為口語時，呈現之順序仍然至關重要而應以拖曳排序的方式註記；⑷而與「排序」同樣重要的是「打平」，這裡的打平不只是內容意義的，對方打我一拳而我也打對方一拳，所以這兩個論點各自被削弱四四六六算了，或是它有一個正面利益，我有一個弊害也就是反面利益，也倆倆抵銷算了。在「整理比較」的打平，更多的是像排序一樣，是一種影響表達接收的呈現技巧，在認知心理學上稱為認知減負或在完形心理學上成為圖底關係：讓不重要的或許是真的打平也可以只是捨棄不管的部分，從觀眾和評審的認知中消失化為灰色的背景；點一下變灰，點一下就變回來；⑸最後，是加權，在「戰場工具」中，我們除了可以拖曳排序改變橫列的順序，你還可以拖拉分界改變橫列的高度，而對應「座標、均衡、弱勢」和「風險、急迫、手段目的、獨立依賴、不可承受、最後一搏」等加權手法，就如同結算時其實也包含了「明確、中性」以及「專屬、外掛、彈性」等細部計算，然後自動計算加權後的總面積而分出勝負——更進一步，我們其實也可以從定義再著手，不只是不合題的不能討論也包含不重要的不用討論：因為概念的非屬核心而也是以偏概全或是反映背後價值膚淺的捨本逐末。只不過，這些就是無法呈現在「戰場工具」中的遺珠了。就如同，合題與計分和類別的判斷只能交由先驗的，在放入論點區之前就已完成；⑹在比較之外的最後，為了方便操作，還有新增橫列，以及取消加權的功能，而全部重置則是把新增的橫列以及加全和打平全部重置，並把論點歸回論點區——但新增儲存的論點不會消失。

---

### ▌八本英文辯論的教材和給AI的提示。

我的想法是這樣的：延續我之前看比賽的觀察所得的直覺，我覺得確實應該要以「核心議題」為核心去展開去講正反方論點或整體的戰局策略和設計。所以像是核心議題有哪些，反方可以在哪些地方攻擊又有哪些策略選擇，然後能形成一個整體的大局觀概念——例如，《Finding Your Voice》認為正方核心議題有「根屬性(現況)、惡害(需要)、優勢、制度(合題性)、解決力」總共五個，而反方針對合題以外的四個攻擊稱為 “on-case” 的論證，針對「合題性、弊害、相抗計畫、哲學批判」的攻擊，則稱為 “off-case” 的論證；並且，反方根據策略選擇，有「捍衛現況、相抗計畫、哲學批判」三種不同的策略選擇：儘管「合題性」和「弊害」屬於 “off-case”，但依舊是捍衛現況的反方可以選擇。

不過，這只是一種觀點，另一種觀點可能認為，還有不提弊害的純粹反對策略，或是對現況進行小幅修正即可——《Strategic Debate》甚至更進一步區分「直接反駁→捍衛現況→質疑解決→提出弊害→相抗計畫」以程度區分正方瑕疵大小以區辨反方策略；以及也區分正方策略，除了「傳統方案」之外（但因為年代較早，所以反而多了「顯著」）還有「比較優勢、標準、淨效益」等辯案類型。類似的，《Burden of Proof》則認為「核心議題」還應該包含「標準」：不只有淨效益和容易混淆的成本效益分析，還有目標標準，也因此反方除了前述策略之外，還能挑戰「顯著」和「標準」。

反過來說，除了反方策略的擴展，這裡也顯示了正方立論，應該要注意的部分：不能只有提出現況惡害，還要有衡量標準和顯著——《Finding Your Voice》其實也有提到「比較優勢」辯案，只是更著重於 1 AC 也就是一辯申論的立論稿撰寫，而這個也可以回應到我觀察到的，對於論點的分點問題（每個核心議題一個論點？每個需要性一個論點？每個利益一個論點？）以及前面說的攻防層次混亂平行並列的問題（區分清楚策略也就知道是在攻擊哪裡和哪裡被攻擊）

再往後，《Finding Your Voice》和《On That Point!》都有提到如何權衡利弊大小的標準，例如「風險、急迫、規模、性質」和「程度、性質、風險、持續、優先考量、獨立 vs 依賴、不可承受、最後一搏」等等。此外，在《Argumentation and Debate》和《Discovering the World Through Debate》還都討論了，除了政策性命題以外的命題類型，後者更是提到了因果事實和價值以及政策之間的關聯，我想既是對整體架構的補充，也是對利弊如何權衡和爭奪標準的補充。

而除了這幾本外文的辯論教科書以外，華語辯論也有自己的發展，例如張哲耀的損益九比和上位與惡害的區分，或是我以《Winning Debates》的「論證地圖」所整理的，在攻防階段結束之後對攻防結果進行評估和「通分、排序、加權」的技巧——請注意，台灣奧瑞岡所說的「損益比」已經不同於美國政策辯論，並非成本效益分析，而是獨立發展出的辯論觀念（但卻望文生義的被認為是「優勢」的替代而被放進了「核心議題」之中稱為：需要性、根屬性、解決力、損益比。）

根據我個人經驗，一個三小時的課程，大概講三個單元，一個單元 2-3 個要點，每個要點搭配 2-4 個觀念或技巧，這樣其實就差不多了。

--

［Hahn &  Hobeika. Finding Your Voice.］

＋－＋Basics of Policy Debate
｜　｜The Policy Debate Squad
｜　 ＋The Topic Process
｜
＋－＋Arguments
｜　｜Evidence
｜　＋Responsibilities
｜
＋－＋Speaking and Flowing
｜　｜Speeches
｜　＋Cross-Examination
｜
＋－＋The 1AC
｜　｜The Negative Strategy
｜　｜Stock Issues 
｜　｜Topicality
｜　｜Disadvantages
｜　｜Counterplans
｜　＋Kritiks
｜
＋－＋Judging the Debate
　　｜Your First Tournament
　　＋“Oh Shit” List

［Wood & Goodnight.Strategic Debate.］

＋－＋Fundamentals
｜　｜Research
｜　｜Affirmative
｜　＋Negative
｜
＋－┌Competitive Presentation
｜　└Refutation and Rebuttal
｜
＋－＋Lincoln-Douglas Debate
　　｜Forensic Tournaments
　　＋Communicative Persuasion

［Crossman, M. Burden of Proof.］

＋－＋Inductive Arguments 
｜　｜Fallacies
｜　＋Parliamentary Debate
｜
＋－＋Research
｜　｜Propositions of Fact and Value
｜　＋Propositions of Policy
｜
＋－＋Forensics
　　｜Refutation
　　｜Presentinig Your Argument 
　　＋Advanced Strategies

［Meany & Shuster. On That Point!］

＋－＋Parliamentary Debating
｜　｜Taking Notes
｜　｜Topics and Topic Interpretation
｜　｜Case Construction
｜　＋Arguing Against the Case
｜
＋－＋Argument Analysis
｜　｜Research and Evidence
｜　｜Disadvantages
｜　｜Counterplans
｜　＋Critiques
｜
＋－┌Points of Information
｜　└Rebuttals and Humor
｜
＋－┌Judging Debates
　　└Tournament Administration

［Discovering the World Through Debate.］

＋－＋Debate in Public Spheres
｜　｜The Structure of Argument
｜　｜Claims and Propositions
｜　｜Evidence
｜　｜Warrants
｜　＋The Quality of Arguments
｜
＋－＋The Karl Popper Debate Format
｜　｜Claims of Cause and Effect
｜　｜Claims of Value
｜　｜Claims of Policy
｜　＋Refutation and Rebuttals
｜
＋－＋Research 
　　｜Cross-Examination
　　｜Arrangement, Style, and Delivery
　　｜Judging Debates
　　｜Debating in an International Setting 
　　＋Debate Club in the School Community

［Freeley. Argumentation and Debate.］

＋－┌Critical Thinking
｜　└Applied and Academic Debate
｜
＋－＋Stating the Controversy
｜　｜Analyzing the Controversy
｜　｜Exploring the Controversy 
｜　｜Evidence
｜　｜Tests of Evidence
｜　｜The Structure of Reasoning
｜　｜Types of Reasoning
｜　＋Obstacles to Clear Thinking
｜
＋－＋Requirements of the Case
｜　｜Building the Affirmative Case
｜　＋Building the Negative Case
｜
＋－＋Refutation
｜　｜Presenting the Case: Composition
｜　＋Presenting the Case: Delivery
｜
＋－＋Evaluating the Debate
　　｜Academic Debate Formats and CX
　　＋Applied Parliamentary Debate

［Snider, A. The Code of the Debater.］

＋－＋Policy Debate
｜　｜Affirmative Case
｜　｜Attacks the Case
｜　｜Disadvantage	 
｜　｜Counterplan
｜　｜Critique	 
｜　｜Topicality	
｜　＋Debate Steps
｜
＋－＋Speaking
｜　｜Flowing
｜　｜Organizing Arguments
｜　｜Preparing as a Team
｜　｜Cross-Examination
｜　｜Research
｜　｜Evidence
｜　｜Briefing
｜　｜Rebuttals
｜　＋Adapting to Judges
｜
＋－＋The Better Debater?
　　｜How the Decision Gets Made
　　｜Cross-Application of Ideas
　　＋Evolving Arguments

［Johnson, S. Winning Debates.］

＋－＋A Philosophy of Debating
｜　｜Arguments and Argumentation
｜　＋Stasis and Structure
｜
＋－＋Basic Strategy and Skills
｜　｜The Speakers and Speeches
｜　＋Decision Making and Strategy
｜
＋－┌The Paradoxes of Debating
｜　└Advanced Tactics
｜
＋－＋Adjudicating Debates

---

### 【腦/心/眼：清單×對比×轉折×反轉×類比】

┏修正┳偏／落點＝否定選言：MECE＋場景
┃　　┃　［不合題、未全稱、非本質］
┃　　┣混／概念＝對比┳性質：概念對比＋猜想落空
┃　　┃　　　　　　　┗規模：舉輕明重＋預設反駁
┃　　┗缺／條件＝敘事┳ABT：有A沒X也沒B→不充分
┃　　　　　　　　　　┗歸謬反證：真A應B卻沒B!?
┃　［反面定義、例外證明、情感用詞、對立成因］
┗置換┳換框／標準：類比、延伸需求、時間場景個人
　　　┗權衡／因果：利弊互現(相反相對or辯證思考)

我想了一下，覺得這還是太複雜了。有沒有可能我們更簡單一點，像是：看到覺得討論太偏頗不管是定義未全稱還是舉例以偏概全總之就都是用MECE舉出其他類型並搭配具體場景說明；而如果是想要強調或釐清某個特定概念的特定內涵就是用概念對比找出相似卻不同或不同卻相似的概念予以對比反襯，如果重點不在概念不同而是關注差異並打算舉輕明重就用明確不同但程度差異遠大於人們以為的對比——而其實也可以理解成性質對比和規模對比，但總之是有特定概念要澄清，而舉出相對的在概念需要釐清或程度上要被提醒的概念加以比較；相反的，如果是針對條件而不想要找出相對概念，就能從敘事著手以ABT或歸謬反證，從句法上的角度來說其實就是對稱句和事理句，而也是理所當然因為前兩者就是休謨所說相似關係的對照而後者則是因果關係的阻礙成功和預期落空並加以解釋。然後ABT和歸謬反證都自然有場景和情境，概念對比和舉輕明重沒有，而可能需要主動用場景加以對比凸顯概念的差異——但也有另一種作法是直接類比，不從概念的切分著手而是直接以類比引入一個既成的理解框架，然後取代原本的理解：相對的，切分則是藉由釐清定義，對舊的理解進行確切修正。並且除此之外還有另一種非從定義而是從因果切入的對比起手式是利弊互現的魚與熊掌不可兼得的相反相對和如人飲水冷暖自知的辯證思考。

--

【給AI的指示與回饋和素材】

請閱讀以下說明，學習「以駁代論」的立論流程：

第一步，不質疑對手的因果論證，而是從「質」和「量」質疑落差：要不，從根本上對方論證的對象不符合定義而指鹿為馬根本不合題；要不，即便合題但對方的論證在程度範圍上並未全稱命題或論證強度要求而也還是沒有完成論證——對於前者，最常見的做法除了「直接指出落差」之外，是以「2×2矩陣」對比正確的和錯誤的定義，然後指出對手定義條件的缺失；對於後者，最常見的做法則是以「MECE」列出概念指涉的範圍，然後指出對手遺漏了哪些類型。

而如果，沒辦法直接在定義上，單向的使對手論證無法抵達終點，我們就必須回到因果層以「削弱（不必然or不唯一）、拉平、反轉」硬打攻防拆解對手論證，或是雙向的打出「雙方各自滿足部份條件」的僵局進行缺失性比較各說各話——然後，能宣稱各自的案例都沒有代表性而不重要（沒有代表性有兩種可能：一是統計意義的沒有代表性的以偏概全而無法證成普遍因果關係，二是不屬於核心定義而不具備討論和認知上的重要性；前者屬於「硬打攻防」的削弱部份，後者才是回到定義）——此時，就需要進入「誰的定義」（滿足了不同條件的）更加本質，亦即哪個條件才是定義的核心？

第三步，把問題從事實接近價值，因為「誰的定義更貼近本質」其實是不可能在事實層爭出輸贏，而必須進到價值層討論言說的意義：為了做到這件事情，在情感上我們必須找到衝擊點和錯開受力點，並進一步深挖情緒感受；而在形式上，我們必須以連結和類比錯開一步以反常合道驚艷觀眾——而有的時候做不到這兩者，我們可能回去以言說指引行動，或將言說視為行動，然後往後延伸定義背後的價值和意義。

更進一步，我們還能把這一套用在自己身上：想像對手可能如何指出我們論證的落差，然後以Lakatos《證明與反駁》的流程處理：怪物排除、例外排除、怪物調整、引理合併——第一層的怪物排除，即是用定義切割拆解命題字詞指出落差，而例外則是概念本質層的以偏概全而因此沒有代表性和不重要；但如果發現無論如何都無法擺脫，我們將會進入怪物調整和引理合併，而有機會挖掘找出題目背後更有價值可以討論而卻被隱藏的關鍵。

而反過來，在表達時，已經藉由構思，完成「以駁代論」的流程，而想要以精簡的短文表達，我們可以在最開始的時候就以「概念對比」的方式，指出我方證確定義和對方錯誤定義「很像，但卻不同」的地方，以釐清或澄清的態度偷渡我們的定義；或是，更進一步用「舉輕明重」的方式找一個類似對方定義和案例，但對其論證要求更輕微，而依舊落空的例子，來說明即便承認對方的論證結論也依舊無法滿足應有的論證門檻和要求——以及在指出條件缺失的時候，也可以用「敘事轉折」的ABT，指出如果只滿足對方的條件而缺失關鍵條件Ｘ時會發生什麼事情；或對方未滿足條件並不明顯，或該條件的必要性其實沒那麼普遍直觀時，以「歸謬反證」將滿足條件應有的結果提出來，而指出對方論證怎麼只停留在Ａ點，而沒能達到Ｂ點？在這裡，還有兩組常見的，可以搭配使用的技巧：第一組是幫切分製造出彩效果，例如用「反面定義」和「例外證明」讓觀眾感受我們的定義更加觸及被忽略本質——福爾摩斯的狗沒有叫是兼具兩者，但有時光是反面切入，不從正面定義而是反面排除也能意外出彩；或是在歸謬和轉折時以「延伸需求」指出對方論證所貼合的標準或結論只是手段而非真正目標，然後甚至能指出對手在因果論證本末倒置甚至適得其反，或至少讓我們在僵局時找到一個簡單的比較出路。第二組是「利弊互現」以幫助我們更好的在因果層達成僵局：可以是「相反相對」說明都可取而卻對立的價值總是伴隨發生魚與熊掌難以兼得，也可以是「辯證思考」指出同一件事情如人飲水冷暖自知，有時我們以為的好處也許恰恰是它的壞處。然後，切分與出彩各任選一，再連結類比和深挖而給出鮮明的意象和情緒：nostalgic、emotional、visual。

--

起手式要熟悉是個正確但放錯重點的詮釋。「cerebral、emotional、visual」其實可以簡化成：腦、心、眼——雖然，我們這套寫作流程，是以「以駁代論」展開，但真要說核心原則其實是「腦、心、眼」，因為辯論或許是心法，但它們才是寫作真正的律法。這也影響到輸出結構：cerebral，其實是反常合道：要有常識、要有轉折、還要合乎道理。所以，現在說「共識起手、轉折立異」並沒有錯，但問題是接下來不是切分展現——四式不只是起手，而就是同時肩負了起手與轉折，而切分的結構式用來給予「合乎道理」基礎的基石：至於為什麼？在「分類即證明」和否定選言等文章我有詳細說明——在這裡，加入 visual 是強化抽象概念為具體場景和比喻讓讀者有畫面感而更好理解或甚至直觀被衝擊。受力點和衝擊點，前者確實可選但只是「澄清的句式」可有可無，但不要擔起多餘的論證責任要在心裡既得；而衝擊點深挖，其實應該在選擇 visual 時一起考慮，並且，相對於「切分」是分離概念，深挖的時候除了情境選擇往往也會用到類比——不一定是要大幅跨界的類比，因為事實上世界上沒有兩個相同的事物和情境，所有比較類同都必然是一種類比，在這裡選擇類比是基於切分之上，綜合考慮 emotional 而也同時達成反常合道的效果。

所以，總的來說，「以駁代論」是以切割定義為出發的辯論技術，然後我們結合了「腦、心、眼」寫作表達律法，已完成短文寫作。「以駁代論」的基礎是對戰場的三層劃分和 Lakatos 的四步處理法以及對手定義出問題的三種類型，然後以類型搭配不同切分結構而再包裝以四式起手，還有兩組配件——綜上共同達成 cerebral 的反常合道，然後從受力點與衝擊點選擇 visual 和 emotional 以意象呈現切分，或以類比加強合道。

--

⒈因果：打攻防
　⑴口說無憑
　⑵硬打攻防／削弱、拉平、反轉
　⑶各說各話＝缺失比較＝以偏概全1：不普遍

⒉定義：切戰場
　⑴指鹿為馬：不合題→拆解(落差)
　• 以偏概全2：不全稱
　⑵捨本逐末1：不重要／沒代表性→切分(條件)

⒊標準：做比較
　⑴捨本逐末2：從事實切進價值／言說行動
　• 受力點：澄清立場不單多餘的論證責任
　⑵反常合道→連結(類比)
　⑶衝擊點：切換角色→深挖

--

因果┳削弱┳不充分／不必然
┃　┃　　┗不必要┳論點：不唯一
┃　┃　　　　　　┃政策：能替代
┃　┃　　　　　　┗判準：歸謬or拉平
┃　┃
┃　┗擊倒┳ABT＝有A沒X也沒B!?
┃　　　　┗對立成因┳有弊害or反效果
┃　　　　　　　　　┗┳倒果為因
┃　　　　　　　　　　┃共同原因
┃　　　　　　　　　　┗調節效果
┃
定義┳┳切割：怪物排除or例外排除
　　┃┗受身：怪物調整or引理合併
　　┃
　　┗┳落點┳MECE：故事-隱喻-命名＋否定選言
　　　┃　　┗光譜or階段(2+1塌縮)or自反堆疊
　　　┃概念┳質：概念對比＋猜想落空
　　　┃　　┃量：舉輕明重＋預設反駁
　　　┃　　┗2×2矩陣：三要素兩轉折
　　　┗條件┳ABT＝X是必要條件。
　　　　　　┗歸謬反證＝B沒X的結果。

[反面定義/延伸需求/例外證明]
[利弊互現-相反相對-辯證思考]

--

［概念對比］『事有必至，理有固然。惟天下之靜者，乃能見微而知著。月暈而風，礎潤而雨，人人知之。人事之推移，理勢之相因，其疏闊而難知，變化而不可測者，孰與天地陰陽之事，而賢者有不知，其故何也？好惡亂其中，而利害奪其外也！』

［舉輕明重］『信義行於君子，而刑戮施於小人。刑入於死者，乃罪大惡極，此又小人之尤甚者也。寧以義死，不苟幸生，而視死如歸，此又君子之尤難者也。方唐太宗之六年，錄大辟囚三百餘人，縱使還家，約其自歸以就死，是君子之難能，期小人之尤者以必能也。其囚及期，而卒自歸無後者，是君子之所難，而小人之所易也，此豈近於人情哉？』

［ABT］『世有伯樂，然後有千里馬。千里馬常有，而伯樂不常有。故雖有名馬，衹辱於奴隸人之手，駢死於槽櫪之間，不以千里稱也。馬之千里者，一食或盡粟一石，食馬者，不知其能千里而食也。是馬也，雖有千里之能，食不飽，力不足，才美不外見，且欲與常馬等不可得，安求其能千里也？』

［歸謬反證］『世皆稱孟嘗君能得士，士以故歸之，而卒賴其力，以脫於虎豹之秦。嗟乎！孟嘗君特雞鳴狗盜之雄耳，豈足以言得士？不然，擅齊之強，得一士焉，宜可以南面而制秦，尚何取雞鳴狗盜之力哉？夫雞鳴狗盜之出其門，此士之所以不至也。』

--

• 克拉克，精简写作，后浪。

在前面几章中，你已经学习了短文写作中几个特别有用的手法。你学会了如何使你的句子和段落保持平衡或不平衡，学会了在写作中调整节奏，学会切中重点。你知道两个语言要素或故事要素就可以将世界一分为二，而三个元素又能将它再次融合。不论文章是二元结构还是三元结构，你都可以用平行结构让它更具可读性、更令人印象深刻。你甚至可以改写文章的最后几个字来给读者一个惊喜。而“软硬词”的选择和节奏的变换可以让文章富有变化。

• Bloom, A. Finding Your Comic Genius.

So, it has a perfect balloon pop: it’s cerebral, emotional, nostalgic, extremely visual,and ends on a funny-sounding word. Wow. Also, there couldn’t have been a better choice of drawing than Leonardo da Vinci’s painting of The Last Supper. It’s iconic, relevant to Christmas and, since there are thirteen people seated at the table, it clearly would have taken Rich a lot of time to create.

--

• Graham, P. Charisma / Power. 2017.

People who are powerful but uncharismatic will tend to be disliked. Their power makes them a target for criticism that they don't have the charisma to disarm. That was Hillary Clinton's problem. It also tends to be a problem for any CEO who is more of a builder than a schmoozer. And yet the builder-type CEO is (like Hillary) probably the best person for the job.

• Graham, P. The Shape of the Essay Field. 2025.

An essay has to tell people something they don't already know. But there are three different reasons people might not know something, and they yield three very different kinds of essays. One reason people won't know something is if it's not important to know. That doesn't mean it will make a bad essay. For example, you might write a good essay about a particular model of car. Readers would learn something from it. It would add to their picture of the world. For a handful of readers it might even spur some kind of epiphany. But unless this is a very unusual car it's not critical for everyone to know about it. If something isn't important to know, there's no answer to the question of why people don't know it. Not knowing random facts is the default. But if you're going to write about things that are important to know, you have to ask why your readers don't already know them. Is it because they're inexperienced, or because they're obtuse? So the three reasons readers might not already know what you tell them are (a) that it's not important, (b) that they're obtuse, or (c) that they're inexperienced. The reason I did this breakdown was to get at the following fact, which might have seemed controversial if I'd led with it, but should be obvious now. If you're writing for smart people about important things, you're writing for the young.

---

### ▌「探索」的前方：小竅門 vs 笨功夫？

最近開始，有意識在區分兩種寫作：⒈一種是已經知道要寫什麼，而或許可以說是專注表達的寫作；⒉另一種是還沒想好要寫什麼，但卻不一定是「探索性」的寫作——「探索」的前提，應該是目標不明，但即便同樣是「還沒想好要寫什麼」卻也還有程度區別：⑴已經有模糊感受只是不知道該如何用言語去捕捉，這類似但依舊不同於「已經知道要寫什麼」因為前者更像取景構圖又或涉及少許元素擺放，但後者是連鏡頭對焦都還沒完成；⑵而即便已經摸清感受，或有清楚的等待分類的概念單元，如何加以排列和分類統整，也是在寫之前還沒有想法——儘管，也許光是為了找到這些類別和單元或例子就已經絞盡腦汁。

最後，才是：⑶真正的「探索性」寫作，也就是像現在這篇文字所呈現的，但也是我不打算多加展開的——我只有兩點想要加以說明：①即便是「不知內容目的地」的探索性寫作，也不代表在形式上不能有所要求。畢竟未知的僅僅是內容，而非形式／以及形式從來不是要在內容確定之後才能選擇，就如詩歌格律與詞牌或我選擇以結構化的切分和列舉展開。②而在框架之上，所遵循的是「清單、光譜、條件、變量、關係」去建構和尋找反例以檢驗假設是否成立：是否口說無憑？是否以偏概全？是否指鹿為馬？是否捨本逐末？然後或切分或連結或找尋衝擊點與錯開受力點而完成以駁代論。

至於「⑵對象已經清晰」的寫作，我現在最常用的做法，反倒是在跟AI對話的過程中逐漸形成：➊把框架和素材丟進去，然後不斷反覆迭代糾正和調整，直到實在受不了再從直覺模糊的選一個起點開始堆積木——有點像是，從全局綜觀忽然投入局部，然後潛意識中隱隱還有著一個形象但也還不甚確定（⑴剛剛這算是從模糊感受加以捕捉，而不只是堆積木了）所以最後往往還是需要第三次加工：➋這時候可能就回到專注表達的寫作了。但有趣的是，實際幾次這樣操作下來，我反而會選擇再最後接一個「⑶真正的探索性的寫作」來強迫自己拉出一個更遠的距離——就像這樣，把本來沒想到的東西（我本來只想到兩種不同的寫作，還有模糊感受與分類排序，以及隱隱約約想到探索和Lakatos跟和AI對話之後的整理）或有模糊方向的路給走完。

然後，也許是時候來討論「⒈已經知道要寫什麼」的寫作，有什麼更進一步的形式和表達技巧／或至少是初步堆好的積木了。但很可惜我還沒有想好：不只是「對於內容本身」還沒有想好，就連「應該要如何想好」也還沒有——我是說到底是要：ⅰ從最笨的地方下手，然後只在兩端用力？ⅱ還是在顯性的理論與手熟的實踐之間補上可傳授也好應用的小竅門？

所以就讓我們以這不上不下的方式結尾吧！

--

【轉折的類型與對切分的加工和成立】

⒈「轉折」有四種：⑴預期落空，往前推翻前提，這是「歸謬反證」。王安石（偷塞）真正得士宜可南面制秦結果不只沒有還反倒要仰賴雞鳴狗盜之徒，反證得出孟嘗君並非真能得士——甚至，倒轉因果指出恰恰是雞鳴狗盜出其門，此士之所以不至也；⑵預期落空，往後補原因，這是反證法的一種變體。蘇洵的事有必至理有固然，但為何風雨之事人盡皆之，人事之推移賢者有不知？原來是因為好惡亂其中而利害奪其外；⑶有意外事件，且阻礙成功導致結果落空，並說明為何如此，這是ABT。韓愈說「有千里馬沒伯樂，千里馬也只能辱於奴隸人之手」屬之；⑷有意外事件但阻礙失敗，並且這個「意外事件」是對手提出的論述，就構成「預設反駁」。歐陽修的「即便是君子也難能」屬之——並再強調，更何況死刑犯是小人之尤，而再達成舉輕明重。

⒉「切分」有三種：⑴以MECE切分面向，歐陽修的君子與小人、黃執中死亡時間的變與不變、Paul Graham 的三種讀者、Chris Hayes 的三種注意力，都是這樣的例子——並且，因為MECE的切分一定成立，所以往往不用說明成立原因，而會直接往後「①以命名比喻和場景」加工，例如雞尾酒會和變與不變的情景，例如山姆大叔和吃角子老虎機以及蝴蝶風扇和提線木偶／或者，作為「②否證選言」的基礎，以進行雙刀法和殘餘法，例如 Paul Graham 論證「文章應該為了年輕人而寫」；⑵對「條件」進行切分，有時是「①直接抓出關鍵條件」像王安石和韓愈都是，只是王安石以該條件偷渡為條件句後項，並以此歸謬反證；韓愈則是以意外事件的充分（沒有伯樂有千里馬也白聊）證明「僅有天資」的不充分，而證明了「還有際遇」這個條件；有時是，以「②兩兩概念」對比，例如天地陰陽和人情理勢，看似是MECE切分，但更關鍵在於找出兩者背後不同條件：天地之事的生成與判斷都不會受到利害好惡影響。另一個例子是，黃執中談表達，提出「為什麼有人私下溝通很有趣但公開表達就熄火？」然後剖析各種差異，並得出因為公開表達有明確目的——在這裡，溝通和表達就並不是MECE的區分，而只是眾多相關概念中兩個最像的，並且這個轉折就像君子和小人的區分，是為了預設反駁對手的論述而非證成切分，黃執中也沒有用「但公開表達就熄火？」證成切分合理而是從後續的關鍵條件找出（但後面的關鍵條件則是以窮舉否定所殘餘，是用上了MECE和否定選言）；還有時是以「③2×2矩陣」釐清並定位所有條件，然後類似MECE呈現切分，或以三要素兩轉折的方式呈現並證成切分。例如，將矩陣中兩兩對比，然後說A和B很像但不是B，A也和C很像但不是C，可見真正的條件應該是哪兩個變量，而定位出了A、B、C；⑶不切面向也不切條件，也沒有進行概念對比或矩陣定位，而是直接指出某個具體的子概念，或指涉的外延，不符合我們討論的範圍。常見做法是搭配預設反駁承認對方論述，但主張對方論述落空——這也是對切分的加工，而不以轉折證成切分。

所以，實際的搭配應該是：⑴以「2×2矩陣」或MECE列舉並加工，或「命名、比喻、場景」的具體（三種注意力）或「否定選言」的論證（Paul Graham、表達熄火）；⑵「概念對比」並以預期落空展現差異再往後補原因也就是核心的條件變量的反證法變體（蘇洵、溝通vs表達）；⑶以對方主張或直接反轉開頭，然後把條件偷渡而預期落空推翻前提的「歸謬反證」（王安石），或提出明確阻礙成功導致結果落空之條件的ABT（韓愈），或單純指出對方論證落差或鋪陳概念對比之後再以差異展現有意外事件但阻礙失敗的「預設反駁」（歐陽修、注意力vs資訊）。

--

【藉由糾正AI而專注表達的寫作】

不管是王安石還是韓愈，其實也都在切「真正的士vs雞鳴狗盜」和「千里馬vs常馬」——韓愈沒有明說，但他用整個「A有千里之能／B食不飽力不足／T才美不外見」所要證明的，恰恰是千里馬與普通馬的差異，不只在天資，還在際遇。只是反過來就變成了想要（從普通馬）變成為千里馬，光有天資還不夠，還要有際遇；王安石則是儘管說了如果孟嘗君得到的是「真正的士」那麼擅齊之強宜可南面制秦，而毋須借助雞鳴狗盜之力，但他卻既沒有明說為什麼雞鳴狗盜不算真正的士，也沒有說為什麼真正的士不會投靠孟嘗君，而是在最後用「對立成因」的修辭，從實際上說雞鳴狗盜在功能上是趕跑真正的士而又無法達成真正的士所能達成的南面而制秦的目標，儘管沒有從概念上說回答問題，但也給出了某種程度的解答。

反過來說，蘇洵和歐陽修的「說明」本身就是利用切分：蘇洵先切了「天地陰陽vs人情理勢」再問它們：應該沒差為何有差？然後給出解釋；歐陽修說了「君子vs小人」的不同以回應就算真的如期而歸也是君子之尤難，並進一步舉輕明種強調況且死囚還是小人之尤甚者。換句話說，兩者都是對切分的加工，但王安石漢韓愈一個是側面證明「用以區別隱含切分的條件」確實都至關重要，一個是根本沒證明而就直接拿去歸謬了。

因此，如果把整個「切分」和「轉折」的套路對應起來，應該是這樣的：⑴MECE搭配①具象填充，或②否定選言；⑵2×2矩陣搭配①三要素兩轉折，或②在XY座標軸上呈現變化或衝突；⑶概念對比搭配①懸念解答直接以「沒結果說明緣由」說明差異，或②預設反駁先承認對方論述再以「有意外但沒影響」搭配舉輕明重，以及③經典敘事以「有意外且有影響」同樣直說主張但隱藏比較對象而以意外之有影響證明條件的必要；最後④還是從對手論述出發但以「沒結果推翻前提」偷渡條件為後件並歸謬反證——換句話說，是以立論或反駁為起手及直接呈現或隱藏切分為兩個變量。

--

• Case, N. How To Explain Things Real Good. 2022.

Explaining stuff is a skill. When training skills, people usually think about Theory versus Practice. Theory is easy to share, but hard to apply to day-to-day work. Practice is easy to apply, but hard to share –– for example, I can't talk you into being able to ride a bike. But I think there's something in the middle: Tricks! (or Heuristics, Rules-of-Thumb, whatever you call it.) Tricks are easy to share, but also easy to apply!

• 韩东，最笨的和最玄的，2022。

我最看重的是习诗者的两种能力。一种是最笨的，笨到什么程度？比如说他喜欢一首诗，非常着迷，他就抄写，就去背诵。这是一种很笨的学习方法，有点像古人读私塾，你不理解《论语》，还没有理解文字背后的意思，就已经先背下来了。渐渐地你懂了，理解其义了，那个背诵的底子就出来了。不管理不理解都已经深入了他的骨髓，就像基本功一样，或者像描红练习，就是这样的一种概念。还有一种能力是指向最玄的东西，比如思考为什么要写作，人为什么要活在世上，写作和真理是一种什么关系，这两种能力或者倾向，最笨的和最玄的，我觉得对写诗而言都非常重要，大家大可在这两个极端上用力。至于在最玄的和最实的之间有一个很大的区域，比如讨论诗是什么，现代性或者后现代，人文精神抑或口语还是意象、修辞这些，我觉得没有多大的意义，或者意义和上面提到的两点相比是等而下之的。

--

＋切分＋性質對比＝Ａ和Ｂ有什麼不同？
｜　　｜
｜　　＋操作條件┌MECE、2×2矩陣、XY座標
｜　　　　　　　└否定選言、三要素兩轉折
｜
＋意外＋反常識＋定義：反面定義or例外證明
　　　｜　　　｜因果：對立成因
　　　｜　　　＋標準：辯證思考
　　　｜
　　　＋故事＋⑴懸念解答＝沒結果說明緣由
　　　　　　｜⑵經典敘事＝有意外且有影響　
　　　　　　｜⑶歸謬反證＝沒結果推翻前提
　　　　　　＋⑷預設反駁＝有意外但沒影響

--

［概念對比＋懸念解答］

• Graham, P. Keep Your Identity Small. 2009.

`#對比和說明`

As a rule, any mention of religion on an online forum degenerates into a religious argument. Why? Why does this happen with religion and not with Javascript or baking or other topics people talk about on forums? What's different about religion is that people don't feel they need to have any particular expertise to have opinions about it. All they need is strongly held beliefs, and anyone can have those. No thread about Javascript will grow as fast as one about religion, because people feel they have to be over some threshold of expertise to post comments about that. But on religion everyone's an expert.

`#連結和猜想`

Then it struck me: this is the problem with politics too. Politics, like religion, is a topic where there's no threshold of expertise for expressing an opinion. All you need is strong convictions. Do religion and politics have something in common that explains this similarity? One possible explanation is that they deal with questions that have no definite answers, so there's no back pressure on people's opinions. Since no one can be proven wrong, every opinion is equally valid, and sensing this, everyone lets fly with theirs.

`#落空和解答`

But this isn't true. There are certainly some political questions that have definite answers, like how much a new government policy will cost. But the more precise political questions suffer the same fate as the vaguer ones. I think what religion and politics have in common is that they become part of people's identity, and people can never have a fruitful argument about something that's part of their identity. By definition they're partisan.

［文vs氣：不知道有什麼差。］

『轍生好為文，思之至深，以為文者，氣之所形，然文不可以學而能，氣可以養而致。孟子曰：「我善養吾浩然之氣。」今觀其文章，寬厚宏博，充乎天地之間，稱其氣之小大。太史公行天下，周覽四海名山大川，與燕、趙間豪俊交遊，故其文踈蕩，頗有奇氣。此二子者，豈嘗執筆學為如此之文哉？其氣充乎其中而溢乎其貌，動乎其言而見乎其文，而不自知也。』

［事vs理：應該沒差卻有差？］

『事有必至，理有固然。惟天下之靜者，乃能見微而知著。月暈而風，礎潤而雨，人人知之。人事之推移，理勢之相因，其疏闊而難知，變化而不可測者，孰與天地陰陽之事，而賢者有不知，其故何也？好惡亂其中，而利害奪其外也！』

［理學vs詩：應該有差卻沒差？］

『上谷一郡多理學，猶有靜修先生遺風焉，而馬子旻徠以詩著。夫理學與詩判而不一也久矣，儒者斥詩爲末技，比於雕虫之屬，而太白嘲誚魯儒，備極醜詆，途殊者議異，理固然歟。旻徠制行醇謹，無夸毗之習，所著養正諸書，皆理學篤論，而詩格大雅，卓然成家，則又何故？予謂世俗所謂理學與詩皆非也。』

--

［反面定義＋懸念解答］

『古之所謂豪傑之士者，必有過人之節。人情有所不能忍者，匹夫見辱，拔劍而起，挺身而鬥，此不足為勇也。天下有大勇者，卒然臨之而不驚，無故加之而不怒，此其所挾持者甚大，而其志甚遠也。』

［對立成因＋經典敘事］
→只有「有千里之能」不夠。

『世有伯樂，然後有千里馬。千里馬常有，而伯樂不常有。故雖有名馬，衹辱於奴隸人之手，駢死於槽櫪之間，不以千里稱也。馬之千里者，一食或盡粟一石，食馬者，不知其能千里而食也。是馬也，雖有千里之能，食不飽，力不足，才美不外見，且欲與常馬等不可得，安求其能千里也？』

［歸謬反證＋對立成因］
→沒有「南面而制秦」不行。

『世皆稱孟嘗君能得士，士以故歸之，而卒賴其力，以脫於虎豹之秦。嗟乎！孟嘗君特雞鳴狗盜之雄耳，豈足以言得士？不然，擅齊之強，得一士焉，宜可以南面而制秦，尚何取雞鳴狗盜之力哉？夫雞鳴狗盜之出其門，此士之所以不至也。』

［預設反駁＋舉輕明重］

『信義行於君子，而刑戮施於小人。刑入於死者，乃罪大惡極，此又小人之尤甚者也。寧以義死，不苟幸生，而視死如歸，此又君子之尤難者也。方唐太宗之六年，錄大辟囚三百餘人，縱使還家，約其自歸以就死，是君子之難能，期小人之尤者以必能也。其囚及期，而卒自歸無後者，是君子之所難，而小人之所易也，此豈近於人情哉？』

--

［MECE＝修身、施事、見言］

『草木鳥獸之為物，眾人之為人，其為生雖異，而為死則同，一歸於腐壞澌盡泯滅而已。而眾人之中，有聖賢者，固亦生且死於其間，而獨異於草木、鳥獸、眾人者，雖死而不朽，逾遠而彌存也。其所以為聖賢者，修之於身，施之於事，見之於言，是三者所以能不朽而存也。修於身者，無所不獲；施於事者，有得有不得焉；其見於言者，則又有能有不能也。施於事矣，不見於言可也。自詩、書、史記所傳，其人豈必皆能言之士哉？修於身矣，而不施於事，不見於言，亦可也。孔子弟子，有能政事者矣，有能言語者矣。若顏回者，在陋巷曲肱饑臥而已，其群居則默然終日如愚人。然自當時群弟子皆推尊之，以為不敢望而及。而後世更百千歲，亦未有能及之者。其不朽而存者，固不待施於事，況於言乎？』

• Graham, P. The Shape of the Essay Field. 2025.

An essay has to tell people something they don't already know. But there are three different reasons people might not know something, and they yield three very different kinds of essays. One reason people won't know something is if it's not important to know. That doesn't mean it will make a bad essay. For example, you might write a good essay about a particular model of car. Readers would learn something from it. It would add to their picture of the world. For a handful of readers it might even spur some kind of epiphany. But unless this is a very unusual car it's not critical for everyone to know about it. If something isn't important to know, there's no answer to the question of why people don't know it. Not knowing random facts is the default. But if you're going to write about things that are important to know, you have to ask why your readers don't already know them. Is it because they're inexperienced, or because they're obtuse? So the three reasons readers might not already know what you tell them are (a) that it's not important, (b) that they're obtuse, or (c) that they're inexperienced. The reason I did this breakdown was to get at the following fact, which might have seemed controversial if I'd led with it, but should be obvious now. If you're writing for smart people about important things, you're writing for the young.

［2×2矩陣］

• Graham, P. The Four Quadrants of Conformism. 2020.

One of the most revealing ways to classify people is by the degree and aggressiveness of their conformism. Imagine a Cartesian coordinate system whose horizontal axis runs from conventional-minded on the left to independent-minded on the right, and whose vertical axis runs from passive at the bottom to aggressive at the top. The resulting four quadrants define four types of people. Starting in the upper left and going counter-clockwise: aggressively conventional-minded, passively conventional-minded, passively independent-minded, and aggressively independent-minded.

• 黃燦然，語言的分寸感，1999。

『這裏就有了一個微妙的差別。布羅茨基和希尼的評論採用了隱喻式寫作，與艾略特拉開了距離，其結果是：艾略特深刻而平鋪直敘，他們則深刻而刁鑽；但是，就評論作為具有獨立欣賞價值的獨立裁體而言，他們與艾略特同屬一類。另一方面，弗洛斯特和沃爾科特也是採用隱喻式寫作，也是刁鑽得無以復加，很接近布羅茨基和希尼的言說方式，但是實際上他們不屬一類。這就是嚴格意義上的詩人批評家與寫評論或寫散文的詩人之間的微妙差別。』

• 伍德，伍爾芙的神秘靈交，1999。

『在她的批評中，比喻的語言成為一種以自己的口音與小說對話的方式，唯有這種方式可以尊重小說終極的不可描述性。批評家便是用比喻來避免以成人的簡明來欺凌小說。因為這種語言是一種強大的猶豫。其強大在於伍爾夫比喻的活力和獨創，其猶豫在於它承認，在批評中純粹總結的語言是不存在的。批評永遠不能提供一個成功的總結，因為它共用批評對象的語言。你總是透過書思考，而不是做關於書的思考。』

• Graham, P. Charisma / Power. 2017.

People who are powerful but uncharismatic will tend to be disliked. Their power makes them a target for criticism that they don't have the charisma to disarm. That was Hillary Clinton's problem. It also tends to be a problem for any CEO who is more of a builder than a schmoozer. And yet the builder-type CEO is (like Hillary) probably the best person for the job.

［XY座標］

• Graham, P. General and Surprising. 2017.

The most valuable insights are both general and surprising. F = ma for example. But general and surprising is a hard combination to achieve. That territory tends to be picked clean, precisely because those insights are so valuable. Ordinarily, the best that people can do is one without the other: either surprising without being general (e.g. gossip), or general without being surprising (e.g. platitudes). Where things get interesting is the moderately valuable insights. You get those from small additions of whichever quality was missing. The more common case is a small addition of generality: a piece of gossip that's more than just gossip, because it teaches something interesting about the world. But another less common approach is to focus on the most general ideas and see if you can find something new to say about them. Because these start out so general, you only need a small delta of novelty to produce a useful insight.

--

［Williams, J. M. Lessons in Clarity and Grace.］

＋清晰＋－＋行動
｜　　｜　｜角色
｜　　｜　｜銜接和連貫
｜　　｜　＋強調
｜　　｜
｜　　＋形式的清晰┌動機
｜　　　　　　　　└整體連貫
｜
＋優雅＋簡潔
　　　｜條理
　　　＋典雅

--

［汤质，高手的黑箱，bilibili课堂］

＋論證：圖爾敏模型
｜動機：SCQA
｜連貫：何帆三招
＋銜接：自我設問

--

［Bloom, A. Finding Your Comic Genius.］

＋三連擊＋意外：(腦) Cerebral
｜　　　｜情感：(心) Emotional
｜　　　＋具體：(眼) Visual
｜
＋細節＋強調＋The Seesaw Theory
　　　｜　　｜Balloon Pops
　　　｜　　＋Word Smuggling
　　　｜
　　　＋典雅：Nice-sounding Word

---

### ▌在注意力經濟時代和AI討論拆書和學辯論。

=title：The Sirens' Call=
=model：Opus 4.8=

「有時候我會想，或許AI才應該付我學費？」

--

我發現幾個更重要的問題想跟你討論，但我先把之前的討論做個收束。

1.1. 先說「該怎麼定位這本書和我們的討論？」我覺得可以粗略地用「內容vs表達」和「辯論vs辯題」來當矩陣定位：(1)對「注意力經濟的重新理解」當然是內容並能在特定辯題派上用場；(2)而拆解書中的論證架構和形式及分析表達技巧也當然是學表達，但不是「專屬辯論」的表達；(3)至於「辯論」作為一種注意力體制，儘管是對辯論本身的討論，但不好說是內容還形式（畢竟「體制」更像一種形式而不是內容，所以區分還是用「內容vs表達」比較好）——(4)而也許也存在專屬辯論的表達，有可能是「基於形式而來的表達技巧」或「與表達有關的特殊形式」但無論如何都是以表達為目的，就姑且還是能算做「學辯論的表達」。

2.1. 然後，關於WHY，如果先不管到底是「為什麼我們要拆這本書」還是「為什麼要讀這本書」而就回到本書的內容本身，我覺得可能就是(1)「注意力經濟的本質是將注意力作為有別於石油的資源開採」此一解答所回推的問題；或是第一章涉及的幾個用來鋪陳和吸引讀者注意的元素：像是第一節「(2)以海妖到警鈴和個人經驗所鋪陳的當代注意力危機的背景」；或第二節「(3)對網路社群平台和手機的擔憂是否一種老生常談的杞人憂天？」或更直接的「(4)我們還需要又一本討論注意力經濟的書嗎？」

2.2. 這邊我不確定，還要跟你討論——同樣的關於WHAT，我也有一個不確定的地方：那就是在全書架構的拆解上，我們知道第一章是建立問題並埋下異化伏筆、第二章分析注意力類型並沿著「吃角子老虎機」和「山姆大叔」的命名展開，但問題是：(1)第三章以「奧德修斯自己沒有摀住耳朵」倒轉問題，從被迫轉向主動探討主體空虛的邪惡根源，真的僅僅只是「吃角子老虎機」的需求面，而不是兩種機制一起討論嗎？當然，從第四章討論社會關注的空虛來看，有可能前者討論的是個體的無聊，後者討論的是認可的空虛，但我不確定是不是真的是這樣？同樣，(2)第五章討論「異化」又真的是有別於「山姆大叔」而回到吃角子老虎機嗎？還是也是兩者共通的診斷？最後，(3)第六章我覺得不是「異化的歷史化、結構化」而是重新審視注意力經濟，指出為什麼當今注意力經濟時代的本質不是資訊而是注意力，以及恰恰是資訊的過載導致了注意力時代——(4)另外，第七章的「注意力體制」我覺得其實好像沒有暗示解方，至少和第八章是脫鉤的（不過喬姆斯基對廣告和電視簡潔性的討論倒是更說明前面講的，也許「注意力體制」的討論更關乎形式，而不只是內容。）

3.1. 再來，是你深挖各章的內容。(1)第一章我們討論過了是一個四段架構：「立論、預設反駁、切分、引入理論」這裡你的理解沒問題，但你提到幾個新發現的技巧，只有「新東西vs壞東西」的對位是有意義的：讓問題變得更加清晰——但並不是把兩個被混為一談的問題重新拆開，而只是指出（預設的）反對者可能質疑作者是不是也陷入把新東西都當成壞東西的道德恐慌心態？還是說，網路和手機真的是壞東西？這只是「把問題更精確成對立選項」的技巧——但這同時也是，所有辯論比賽成立的前提：把爭論「辯論命題化」。(2)至於手機只是症狀不是成因，以及媒體控制大眾的因果翻轉，這不是什麼特別的技巧，只是任何（針對因果關係進行重新建構的）新觀點在提出時必然會有的現象。(3)這裡真正重要的，還是「資訊vs注意力」的切分，並以此回應預設的反駁：注意力是生命的本質，然而注意力經濟正使每一個人成為可被攫取的資源——就像我們用「矩陣」定位和切分相鄰概念一樣，以及第二章劃分三種注意力機制：先排除第一種，展開討論後兩者（並加以命名）這都才是辯論更核心的技巧——(4)但除了山姆大叔和吃角子老虎機的「具象比喻命名」之外，你提到了以「雞尾酒會」的場景，說明三種注意力機制的運作，這確實是個我遺漏的技巧，但我不覺得這是陌生化，而更像僅僅是場景化：把習以為常不加以區辨的事情說清楚，但沒有到驚奇和不可思議的程度。(5)另外，遞進排序很重要，這是金字塔原理除了每一層之間要MECE之外，還要有邏輯聯繫的第二個原則。但有沒有先寫在標題並不重要，我們沒有要寫書。

3.2. 至於後面幾章，你提到的幾個發現都很有用和正確，但有幾個地方我還是要提醒：(1)第三章「同素材的二次開採」要結合倒轉問題一起看：奧德修斯的故事，其實就也只是「具象比喻命名」的技巧，之所以能二次開採是因為倒轉了問題，這才是新的技巧。(2)第三章討論個體無聊並非與生俱來時，用「跨文化反例擊破一個被當成普世的東西」並不是「不唯一」而是與它並列的另一個挑戰推論相關性的工具：不充分／不必然與不必要／不唯一。兩者其實都是廣義的「提出反例」，只是前者質疑代表性不足，後者質疑確認偏誤（支持的連結不唯一或提出的解釋不唯一）——你之前誤以為拆這本書的WHY是「能從中學到關於表達形式的技巧」我說這不唯一，就是在說「解釋不唯一」（這只是我們拆的第一本書，而你在沒有我提點的情況下沒意識到可以學形式，不代表「這本書的主要價值」就是學形式——也許每本書都有這個價值，那麼這本書的WHY就不應該特別強調這一點）——但也有的時候是提出案例支持的因果關係不唯一，或定義與標準的條件不必要；(3)此外，解釋不唯一，也涉及我說這本書的HOW可能是「資訊vs注意力」的引申：不只是在辯論上我們在提出資訊之前得先抓到聽眾注意力，而還有只提出資訊，而沒有詮釋（新觀點）毫無意義，因此「新資訊vs新觀點」才是值得注意的切分——此時的「詮釋」就也要記得可能面臨解釋不唯一的挑戰；(4)再來，第四章的剝奪證明份量，是所謂「例外證明」的技巧，就像福爾摩斯的狗沒有叫；至於第四章和第五章「借已警覺的陡峭曲線（碳排放）去傳染」和「借已接受的框架（馬克思異化）映射新現象」其實就都是類比而已——其他的，像是「量化、流行歌例證、歷史起點」就都只是找例子證明而已。比較值得一提的是塔利班的例子，有點「舉輕明重」的意味，這和「例外證明」一樣是很特別的舉例技巧。

4.1. 但我覺得真正重要的問題是：(1)我們從書中拆出了這許多技巧，但我們自己的整理，要怎麼用上這些技巧呢？如果沒有辦法，這是不是說，我們的學習和應用是脫鉤的？(2)更進一步來說，如果我們能從書中拆出這些技巧，那麼我們「拆出這些技巧的技巧」又是不是也值得分析和拆解？它們可能是什麼而我沒有意識到？或其實就是同一套技巧的不同層次和對象的使用？(3)以及最後，結合形式與內容，如果按照作者的說法，在現今「注意力體制已然失落」的現在，這些技巧又如何能幫助我們呢？畢竟，不管是辯論或更廣義的表達形式的技術，其本質上也都是一種爭取注意力的技術對吧？就如作者將「林肯-道格拉斯」的辯論視為注意力體制的典範。

--

＋１海妖／警報／手機
｜
＋２＋自願性
｜　｜非自願：角子老虎－＞３無聊：分心／閒適
｜　＋社會性：山姆大叔－＞４關注：注意≠認可
｜
＋－＋５異化：勞動≒注意力＋　　　＋非商業性
　　｜６稀缺：資訊／注意力｜－＞８｜替代市場
　　＋７制度：注意力＋說服＋　　　＋政府監管

---

### ▌2026第2屆青雲盃：辯題講座與AI協作。

我正在準備一個講座，主題是以「富有／貧窮 更容易暴露人性之惡」為例，說明價值辯論的準備方式，以及我對這個題目的想法。換句話說，既要以小見大，展現整體的概覽；也要足夠具體特定，深入展開我對題目的獨特觀點。我目前的想法是把講座分成三個部分：⒈先講我對題目的思考，⒉再講我所使用到的方法，⒊最後補充方法背後的理論知識。具體來說，「⒊理論」是價值辯論的整體框架和流程，主要分成四個層次：⑴在因果現象上各說各話，以歸納窮舉或推論與資料和數據案例避免以及指責對方口說無憑；⑵或進一步舉出反例以削弱和拉平等攻防手法，甚至反轉判準與因果擊倒對手論證，而互有拆解或指責對方以偏概全；⑶在定義或概念上進行切分，而能應對反例並自圓其說，同時指責對手指鹿為馬；⑷以言說行動指出切分背後的意義，並指責對手捨本逐末，沒有抓到真正的本質。但在「⒉方法」上，我會直接從概念切分開始，分成三個步驟：拆解、切分、連結。首先，拆解預設對手最可能的論證方向，然後拆解題目字詞，使對手的論證失效落空。例如，正方說「富有更容易暴露人性之惡」，不爭論富有會不會真得導致惡行，而是直接切割即便財富催生惡行，但富有也更能掩蓋惡行，被執行但掩蓋了的惡行，還算是「暴露」嗎？或同樣不質疑論證，而正方是如何比較出「更容易」？以及富有導致的到底是「人性」之惡，還是人性被異化的結果？甚至，驅動惡行的是「富有」本身，還是感覺不夠富有的匱乏感？每一個追問都不是在反駁正方論證，而是讓正方論證無法抵達所要抵達的目標。接著，在拆解的基礎上，以視覺化工具（特別是2×2矩陣）對概念條件進行切分並找出相鄰概念使其結構性位置得以呈現。例如，用「遮蔽×歸因」把富有和貧窮各自定位：富有反而會遮蔽惡行，但對方也可以主張，富有控制了其他變量使惡行毫無藉口——於是陷入僵局，往下連結：與切分相反，切分是把對方論證從辯題上偏離，連結則是藉由小小的偏移讓己方論證內容更深刻且更貼近辯題本質。例如，反方可以說，貧窮暴露人性之惡，真正揭示的不只是惡的純粹，更是善的脆弱：原來再多努力和教育薰陶，只要面對真正的災難來臨，我們都會被打回原形，而把「暴露人性之惡」從「惡被看見」轉向了「善的崩塌」——然後，從偏移位置繼續往下挖掘，例如，可以進一步捕捉背後的情緒根源：正方偏移後揭示的是惡的無解和根深柢固，背後是對他人的恐懼。反方的恐懼則是未知，甚至是自己，恐懼不知何時到來的滑落，與不得不面對的自我——但請注意，「恐懼」「揭示了什麼」只是這個題目的具體展開，不是方法本身的固定公式。連結的核心始終是：偏移以貼合辯題本質，然後從那個位置繼續深挖。請閱讀上述說明，嘗試還原我的講座大綱，然後總結我的思考方法，並用別的題目實踐這個方法給我看看你的理解。

---
### ▌七個模板：AI協作筆記。

• SCQA：背景-衝突-問題-解決。
• 新認識、新觀點、新行動。
• 命名、場景、比喻、挑戰。
• 暗門密碼：暗門-對象-框架-密碼。
• 視覺化、做定義、重框架。
• PAS變體：問題-解決-成功。
• WHAT、HOW、WHY。

好的，我會幫您回顧這次的協作。

我們的任務目標非常明確：撰寫一篇「利用模板解釋模板」的文章。為了達成這個目標，我們採取了極為嚴謹的兩階段協作：首先是素材的深度積累與修正，其次是架構的編排與寫作。在任務之初，您制定了極為嚴格的溝通規範，要求我先說明對任務目標和進行方式的理解，並表示您會逐個講解模板內容，確保我完全理解後，再討論如何撰寫文章。您特別強調：「不要使用要點清單，使用流暢的段落式散文。」這條指令貫穿了我們的協作全程，確保我們的對話不是零散的資訊拼湊，而是具有邏輯深度的文本構建。

--

在第一階段的素材積累中，我們先探討了黃執中關於「哲理辯」的內容，確立了「新認識、新觀點、新行動」與「命名、場景、比喻、挑戰」兩組基礎模板。針對我的理解，您給予了極具洞察力的修正，指出它們在寫作光譜上的不同定位：前者是內容的戰略骨架，負責邏輯推演與認知重塑；後者則是表達上的戰術血肉，負責具象化敘事與情感昇華。同時，您也修正了我對操作順序的理解，強調「比喻」往往伴隨「命名」先行，用以幫助讀者理解被切分的概念（對應新認識），而「場景」則是概念確立後所展現的新世界觀（對應新觀點）。您還特別提醒，雖然在「新認識」中切分常用於重新定義，但模板案例顯示，切分也能用於區分討論面向和釐清討論條件，以進行更好的分類討論。此外，您也在此時建立了一個重要的互動規範：即每次討論新內容前，都要先列出已討論過的模板清單，確保我們是「逐步更新」而不遺忘舊知識。

接著，我們進入第二篇關於寫作課程的文章，這裡引入了「WHAT-HOW-WHY」與「問題、解決、成功」模板。您特別指出，這篇文章本身就是「用模板解釋模板（後設）」的範例，但強調我們的目標是要將所有的模板進行有機整合，而非僅僅停留在以單一模板講解單一模板的層級。此外，您提醒我注意「問題、解決、成功」其實是經典銷售文案 PAS 的變體，但在此階段，我們尚未對「WHAT-HOW-WHY」模板做深入討論。

真正的轉折出現在第三篇文章，這篇關於拆書的文章帶來了「暗門密碼」與「SCQA」。正是在這裡，您對「WHAT-HOW-WHY」進行了關鍵擴充，指出「WHAT」不應只停留在定義，還包含概念的延伸、闡釋、細化與舉例，並可藉由「是什麼-不是什麼-像是什麼」的正反框架和類比來界定；「HOW」則不只羅列步驟，還可藉由「用法-訣竅-誤區-更正」來進行實戰指導。在後續的回饋中，您對模板間的關聯進行了細緻梳理：您指出「XX的暗門」之於 SCQA，就如同一個好的「WHY」是壓縮了背景和衝突的 SCQA 結構；而「關鍵轉向」本質上是一種「新認識」或「重框架」（您特別指示我先忽略重框架，留待後續解釋）；「暗門密碼」則是精彩的「命名」；「真正的對話對象」類似於「挑戰」但更具針對性。正是在這裡，您對「WHAT-HOW-WHY」進行了關鍵擴充，指出「WHAT」不應只停留在定義，還包含概念的延伸、闡釋、細化與舉例，並可藉由「是什麼-不是什麼-像是什麼」的正反框架來界定；「HOW」則不只羅列步驟，還可藉由「用法-訣竅-誤區-更正」來進行實戰指導。

最後，您提供了關於「視覺化、做定義、重框架」的筆記。這是一個複合性的技巧包，您詳細列出了具體工具，涵蓋視覺化的 2×2 矩陣、XY 軸與文氏圖；做定義的 MECE 與各種定義技巧；重框架的對比（性質對比、屬加種差、具象法、類比換框、利弊互現）和金句（1213法、1221法、否定法、擴字法）以及換框法（連接詞、情感用詞變化、先後正反、換角色/硬組合/小見大）——並特別補充了關於「利弊互現」的三篇參考文章。針對這部分，您再次給予了負面排除指令，要求我忽略文中關於「定義即權力」的個人感悟，專注於這些具體工藝，將其視為生產「新認識」的工廠。至此，我們完成了所有工具的準備與定義校準。

--

進入第二階段的寫作時，我們採取了「大結構套小結構」的策略，以「SCQA (T1)」作為宏觀架構。在「背景」之後，您要求將「衝突」細分為兩層：環境上的分眾導致缺乏共同背景，以及目標上我們不只想解決既有問題，更想帶給讀者啟發。這順勢引出了「問題」：在無法依賴共同背景時，該如何將觀點「灌輸」給讀者？這裡您特別強調使用「灌輸」一詞，以便在「解答」中進行翻轉：我們不要灌輸，而是要提供「濾鏡」。

在展開核心「解答」的過程中，文章內容變得極為豐富且多層次。我們先運用「新認識、新觀點、新行動 (T2)」模板，引入馬督工關於「自媒體的目標是做定義與做模型」和後現代哲學家「理論工具箱」的觀點，來增強理論厚度。接著利用「命名、場景、比喻、挑戰 (T3)」模板，將表達重新定義為「打造濾鏡」，並以「手上的槌子」為比喻，形象地展示了從「找釘子」到「給槌子」的轉變。依照您的指示，我們提出了一個具體的場景——「讀者碰到事情時，會想要知道作者怎麼看？」——這比單純的讚美更能展示擁有新框架後的影響力。隨後，為了深入探討創作者的痛點，我們運用「暗門密碼 (T4)」與「視覺化、做定義、重框架 (T5)」模板，利用 2×2 矩陣與文氏圖的「不可能三角」鎖定「有想法但受困於效率」的創作者，再透過「1221法」進行重框架，推導出「形式即內容」這個暗門密碼，強調模板是刺激思考的容器。最後，文章以「問題、解決、成功 (T6)」作為轉場，將讀者從理論帶向實踐，並最終以「WHAT-HOW-WHY (T7)」的格式，逐一詳解了這套工具箱中的每一個模板，完美實現了「用模板解釋模板」的寫作目標。

---

### ▌懂再多道理，還是過不好這一生？

⒈ 最近有種「見山又是山」的喜悅。

⒉ 前陣子，看到一個很驚豔的拆書prompt，作者是李继刚——最早知道他，還是2024年的漢語新解，然後就被他Lisp偽代碼風格的提示詞給驚到了覺得也太酷了吧！但很快，AI的迅猛發展，就把這些奇技淫巧給遠遠拋下——不要說Lisp偽代碼這種炫技式的壓縮表達，就連常見的「角色-任務-約束」也都不怎麼需要了。

⒊ 但不管是壓縮，還是結構化表達，都給了我很大的啟發：相較於，從AI那兒獲得的，我總覺得在與AI的互動過程中，我才獲得了更多。

⒋ 這個拆書prompt，他沒有取名字，就叫它暗門密碼吧。它的架構很簡單：XX的暗門、真正的對話對象，關鍵轉向，暗門密碼。舉例來說，其中一個範例是王陽明的《傳習錄》，第一段就是「《`#傳習錄`》的暗門」——

那個讓王陽明不得不說的的問題：

「為什麼我明明知道，卻做不到？」

這是每個人心中最隱密的痛苦──你知道應該孝順，卻對父母不耐煩；你知道應該誠實，卻還是說了謊；你知道什麼是對的，卻總是做錯的。這種「知」與「行」的撕裂，正是王陽明要治癒的病。

`#真正的對話對象`

不是那些來求學的弟子，不是那些飽讀詩書的士大夫。而是那個在龍場的寒夜裡，在生死邊緣徘徊的自己。是那個曾經追隨朱熹，格物格到吐血，卻還是找不到「理」的王守仁。他真正在對話的，是每一個被「應該」壓垮的靈魂──那些背負聖賢教誨，卻在現實中步履維艱的人。

`#關鍵轉向`

整部書完成了一個石破天驚的轉向：

• 從「向外求理」到「向內求心」
• 從「知了才能行」到「知行本是一體」
• 從「學做聖人」到「發現自己是聖人」

最震撼的轉向：

「你找不到理，是因為理就在你心裡」。

`#暗門密碼`

「知行合一」

這四個字不是在說「知道了就要去做」這麼簡單。王陽明真正要說的是：真正的「知」，就是「行」的開始；真正的「行」，就是「知」的完成。你之所以做不到，不是因為你「知道了卻不去行」，而是因為你從來沒有真正知道。

⒌ 然而，當我把prompt拿來自己玩的時候，卻發現怎麼樣都少了一個味道。於是，一個不爽乾脆把它的幾個示例，全部丟給AI要它總結其中規律，然後按照這個格式輸出──這是小樣本學習Few-shot的作法，就像有些結構化提示詞也會加入執行步驟的Chain-of-Thought一樣。

⒍ 沒想到結果意外的好！於是更進一步，我試著想要總結：這四個步驟的拆書策略其實也就是SCQA的變形。從「背景-衝突-問題-解決」變成了「問題-衝突-背景-解決」──那個讓王陽明不得不說的的問題當然是問題，然後鋪排各種衝突；接著，以更直接的人物（真正的對話對象）呈現背景引起共鳴，然後重構認知並以新認知所得的新觀點，去重新展望這個世界──新認識+新觀點，或者重框架+做定義，所以總結成「問題+衝突-共鳴-重構-洞察/命名」卻發現歪得比原本只是少了一點味道的prompt還差了十萬八千里。而質問AI的結果，它給自己的辯護是，這樣的總結，對AI來說並不單單是從具體變抽象而丟失了原有的脈絡，甚至會進一步暗示它完全不同的語境──然後想到，這對人類來說，又何嘗也不是如此呢？

⒎ 總是想要不斷不斷的，總結出更深刻或至少更普適的原理原則。不斷的整合架構，刨除細節或只屬於特定情境脈絡的枝節，而妄想有某種純粹的以不變應萬變的絕招──就像張三丰教張無忌太極劍時，問他忘了多少，或是獨孤九劍的無招勝有招──但或許真正的武學高手從來不是如此，不是真的要費心去把學會的劍招給忘了，然後無招勝有招。而是能不拘泥於每一招或甚至是隨時都能夠想出新招。特別是在這個，一切堅固的都煙消雲散的AI時代，不用去總結什麼也不用去練什麼，隨時想到需要什麼，就叫AI幫你生一招就好。

⒏ 換句話說，真正要練的是小無相功。

⒐ 所以現在即便是隨意跟AI聊天，也會自然而然使用結構化的表達：先在最開始說明任務的性質，然後交代背景脈絡和我考慮的原則和希望用上的方法或技巧，最後是執行步驟。並且也更習慣給予明確的標準／或是對結果大致的想像儘管可能在這之前毫無概念，以及在一次又一次的重複中，越來越習慣和擅長使用簡單的語言描述我希望AI能整握（也就是我所掌握）的技能，甚至是臨時起意的排列組合。例如在SCQA之後加上WHAT和HOW／把WHY換成SCQA，然後各以正反「是什麼-不是什麼-像是什麼」和「用法-訣竅-誤區-更正」並列的格式呈現。簡單的主題句，清單，和排列組裝。

──還有隨時的延伸、闡釋、細化、舉例。

---

▌用AI做了一個視覺化的戰場工具。260714
https://www.facebook.com/lunglung0815/posts/28067967209462984

▌八本英文辯論的教材和給AI的提示。260712
https://www.facebook.com/lunglung0815/posts/28053023520957353

【腦/心/眼：清單×對比×轉折×反轉×類比】260710
https://www.facebook.com/lunglung0815/posts/28031444119781960

▌「探索」的前方：小竅門 vs 笨功夫？260625
https://www.facebook.com/lunglung0815/posts/27865561329703574

▌在注意力經濟時代和AI討論拆書和學辯論。260618
https://www.facebook.com/lunglung0815/posts/27783348681258173

▌2026第2屆青雲盃：辯題講座與AI協作。260404
https://www.facebook.com/lunglung0815/posts/26874057732187277

▌七個模板：AI協作筆記。260106
https://www.facebook.com/lunglung0815/posts/26011560548437004

▌懂再多道理，還是過不好這一生？260105
https://www.facebook.com/lunglung0815/posts/25996058483320544