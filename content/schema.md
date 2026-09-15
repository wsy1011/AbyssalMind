# Abyssal Mind 内容数据结构

内容文件位于 `content/`，采用 UTF-8 JSON。日期统一使用 `YYYY-MM-DD`；正文内容后续可迁移到 Markdown 文件，JSON 保留索引和元信息。

## Article

```json
{
  "id": "unique-slug",
  "type": "research | signal | technology | data | policy | case-study",
  "status": "draft | published | archived",
  "title": "文章标题",
  "dek": "一到两句话的摘要",
  "language": "zh-CN",
  "publishedAt": "2026-09-15",
  "updatedAt": "2026-09-15",
  "author": "Abyssal Mind Editorial",
  "domains": ["transport", "energy", "shipping", "economy"],
  "topics": ["electric-vessels"],
  "regions": ["China"],
  "tags": ["battery", "operations"],`r`n  "image": {"src": "assets/images/unique-slug.webp", "alt": "描述插图内容", "credit": "来源或作者"},
  "takeaways": ["核心结论"],
  "whyItMatters": "对研究和产业实践的意义",
  "source": {"title": "原始来源标题", "url": "https://example.org", "kind": "paper"},
  "readingTime": 8,
  "featured": false,
  "body": "articles/unique-slug.md"
}
```

## Topic

专题包含持续更新的文章集合，并记录专题的定义、时间线和开放问题。`articleIds` 引用 `articles.json` 中的文章 `id`。

## Resource

资源包含数据集、方法、报告、政策文件、工具和课程。每条资源保留原始链接、机构、发布日期和适用领域。

## 编辑规则

- `source.url` 必须指向可核查的原始来源。
- 事实、作者解释和推测性判断在文章正文中分开表达。
- `updatedAt` 只在内容实际修改后更新。
- 未完成内容使用 `draft`，不会出现在公开列表。

