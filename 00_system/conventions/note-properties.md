# 笔记属性规范

字段名是系统接口的一部分，不要随意改名。

| 字段 | 适用笔记 | 要求 | 说明 |
| --- | --- | --- | --- |
| `type` | 全部 | 必填 | `source-note` / `concept-note` / `method-note` / `question-note` / `project-note` / `daily-note` |
| `subject_main` | 学科相关笔记 | 必填 | 取自 `subjects.yaml` |
| `subject_branch` | 学科相关笔记 | 必填 | 取自对应学科分支 |
| `source_type` | source note | 必填 | `books` / `papers` / `courses` / `reference` |
| `status` | 多数笔记 | 必填 | `draft` / `captured` / `reading` / `active` / `stable` / `archived` |
| `zotero_key` | source note | 必填 | Zotero 条目 key |
| `authors` | source note | 推荐 | YAML 列表 |
| `year` | source note | 推荐 | 出版年份 |
| `priority` | source/question note | 可选 | `high` / `medium` / `low` |
| `review_due` | source note | 可选 | `YYYY-MM-DD` |
| `project_status` | project note | 必填 | `planning` / `active` / `paused` / `done` / `archived` |
| `date` | daily note | 必填 | `YYYY-MM-DD` |

不要为个别场景临时创造字段；先检查是否能用现有字段、标签或正文表达。
