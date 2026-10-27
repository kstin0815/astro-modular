// 共用區塊：把文章裡的 ![[代號]] 換成 src/content/_sync/共用區塊/代號.md 的內容（去掉檔頭）（臉書同步用，見 src/content/_sync/同步說明.md）。
// 必須排在 remarkPlugins 的第一個，讓換進來的 [[wikilink]] 之後照常被處理。
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { visit } from 'unist-util-visit';

const SHARED_DIR = join(process.cwd(), 'src/content/_sync/共用區塊');
const EMBED = /!\[\[([^\]|]+)\]\]/g;

export function expandSharedBlocks(text: string): string {
  return text.replace(EMBED, (whole, name) => {
    const file = join(SHARED_DIR, `${String(name).trim()}.md`);
    if (!existsSync(file)) return whole;
    return readFileSync(file, 'utf-8').replace(/\r\n/g, '\n').replace(/^---\n[\s\S]*?\n---\n/, '').trim();
  });
}

export function remarkSharedBlocks() {
  return (tree: any) => {
    visit(tree, 'text', (node: any) => {
      if (typeof node.value === 'string' && node.value.includes('![[')) {
        node.value = expandSharedBlocks(node.value);
      }
    });
  };
}
