# Obsidian 插件说明

本文档根据 `.obsidian/` 当前插件安装与启用情况整理，用来说明本 vault 中每个插件的职责、推荐用法和维护注意事项。

本 vault 的插件原则是：插件服务于知识库闭环，而不是替代知识库规则。核心闭环为：

```text
Zotero 条目 -> 02_library 实体资料 -> source note -> MOC 回链 -> project note / concept note -> audit
```

## 当前状态

### 已启用社区插件

| 插件 | 版本 | 本库用途 | 优先级 |
| --- | --- | --- | --- |
| Calendar | 1.5.10 | 日记入口与日历视图 | 推荐 |
| Dataview | 0.5.68 | 基于 frontmatter 查询 source note、项目、待办和回顾项 | 推荐 |
| Citations | 0.4.5 | 从 Zotero / BibTeX 搜索并插入引用 | 谨慎使用 |
| Excalidraw | 2.22.3 | 绘制概念图、论证图、知识地图 | 可选 |
| Linter | 1.31.2 | 统一笔记格式和 YAML 风格 | 推荐 |
| Style Settings | 1.0.9 | 调整主题和插件样式 | 可选 |
| Zotero Integration | 3.2.1 | 从 Zotero 导入引用、书目、笔记和 PDF 批注 | 推荐 |
| Periodic Notes | 0.0.17 | 管理 daily / weekly / monthly notes | 推荐 |
| QuickAdd | 2.12.0 | 快速创建固定类型笔记和捕获内容 | 推荐 |
| Templater | 2.20.0 | 使用增强模板创建 source note、project note 等 | 推荐 |
| Various Complements | 11.2.0 | 自动补全已有词条、链接和常用术语 | 推荐 |

### 已安装但未启用

| 插件 | 版本 | 建议 |
| --- | --- | --- |
| ZotLit | 1.1.11 | 已安装但未列入 `community-plugins.json`。如果未来希望统一 Zotero 文献笔记工作流，可在 Zotero Integration / Citations / ZotLit 三者中选一个主插件，不建议三者长期并行。 |

### 已启用核心插件

当前已启用的关键核心插件包括：

- File explorer
- Search
- Quick switcher
- Graph view
- Backlinks
- Canvas
- Outgoing links
- Tags view
- Properties
- Page preview
- Daily notes
- Templates
- Note composer
- Command palette
- Bookmarks
- Outline
- Word count
- File recovery
- Sync
- Bases

这些核心插件已经覆盖了导航、属性管理、日记、模板、回链、Bases 视图和同步。社区插件应尽量围绕这些能力补强。

## 插件职责分工

### Zotero 与引用

当前同时安装了 Citations、Zotero Integration 和 ZotLit，其中前两个已启用，ZotLit 未启用。

建议短期方案：

- 以 Zotero Integration 为主，用于导入 Zotero 条目、书目、笔记和 PDF 批注。
- Citations 只用于简单插入 citation key 或引用，不承担文献笔记主流程。
- ZotLit 暂不启用，除非决定切换为 ZotLit 主导的文献笔记流程。

维护注意：

- 不要让三个插件同时生成 source note，否则会产生模板、路径、字段和 citation key 的重复。
- 本项目的 source note 应继续遵守 `00_system/templates/source-note.md` 的 frontmatter。
- Zotero 附件应使用 linked attachment 指向 `02_library/`，不要让插件在 vault 内复制 PDF。

### 模板与快速创建

Templater、QuickAdd、核心 Templates 同时存在。

建议分工：

- Templater：作为主要模板引擎，用于动态创建 source note、concept note、method note、project note、daily note。
- QuickAdd：作为入口按钮或命令面板动作，用于触发固定创建流程。
- 核心 Templates：保留为简单备用，不作为主流程。

推荐建立的 QuickAdd 动作：

- 新建 source note
- 新建 concept note
- 新建 method note
- 新建 question note
- 新建 project note
- 快速捕获到 `01_inbox` 或 daily note

当前 QuickAdd 的 `choices` 为空，说明还没有配置实际捕获动作。建议优先补齐 2 到 3 个最常用动作，不要一次配置过多。

### 日记与周期复盘

Calendar、Periodic Notes、核心 Daily notes 都已启用。

建议分工：

- Daily notes：负责创建每日笔记。
- Calendar：负责从日历视图进入每日笔记。
- Periodic Notes：负责 weekly / monthly / quarterly review。

建议路径：

- Daily notes：`07_daily/`
- Weekly review：可放在 `07_daily/weekly/` 或 `06_project-notes/reviews/`
- Monthly review：可放在 `07_daily/monthly/` 或 `06_project-notes/reviews/`

当前 Calendar 未启用 weekly note 显示。如果后续使用 Periodic Notes 管理周记，可以再开启周视图。

### 查询与仪表盘

Dataview 与核心 Bases 都已可用。

建议分工：

- Bases：优先用于基于 Properties 的稳定表格视图，例如 source notes、project notes、review due。
- Dataview：用于更复杂的查询，例如缺字段、过期回顾、按学科统计、按状态聚合。

推荐在 `00_dashboard/Home.md` 或 `10_bases/` 中逐步建立这些视图：

- 缺 `zotero_key` 的 source note
- `status = captured` 且未整理的 source note
- `review_due` 已到期的笔记
- active project notes
- 每个 `subject_main` 的 source note 数量
- 孤立的 concept note 或未接入 MOC 的笔记

### 格式治理

Linter 已启用，但当前大部分规则处于关闭状态，`lintOnSave` 也关闭。

这是合理的保守配置。中文知识库不建议一开始开启激进自动格式化。

建议只逐步启用低风险规则：

- 文末保留一个换行
- 移除行尾空格
- 限制连续空行
- YAML 后保留空行

暂缓启用：

- 自动排序 YAML key
- 自动移动 tags
- 自动改标题大小写
- 自动改中文和英文之间空格

原因是本项目已经有固定 frontmatter 字段顺序，激进规则可能破坏模板一致性。

### 写作、绘图与辅助输入

Excalidraw 适合在这些场景使用：

- 概念之间关系复杂
- 哲学、历史、社会科学需要画论证结构
- AI / 数学 / 物理需要画模型、公式关系或知识地图

Various Complements 适合在笔记增多后提升链接效率，尤其是自动补全已有 source note、concept note 和术语。

Style Settings 只负责阅读体验和主题微调，不参与知识结构。

## 建议的维护策略

### 保持一个主文献工作流

在 Zotero Integration、Citations、ZotLit 之间，必须明确主插件。

当前建议：

```text
Zotero Integration = 主导入插件
Citations = 轻量引用插件
ZotLit = 暂不启用，作为备选
```

如果未来切换到 ZotLit，应先关闭 Zotero Integration 和 Citations 中重叠的导入功能，再迁移模板。

### 优先配置 QuickAdd

当前插件已经装齐，但 QuickAdd 还没有实际 choices。最值得补的是固定创建入口：

1. 新建 source note
2. 新建 project note
3. 新建 daily capture

这三项会明显降低日常维护摩擦。

### 用 Dataview / Bases 暴露问题

不要只靠记忆维护知识库。建议把审计脚本能发现的问题，也尽量在 Obsidian 里可视化：

- 哪些资料还没有 source note
- 哪些 source note 还没有 MOC 回链
- 哪些项目长期 active 但没有下一步
- 哪些笔记仍是 captured 状态

### 避免插件膨胀

当前插件数量已经足够支撑本项目。短期不建议继续安装新的大型插件，除非它能直接服务于以下目标之一：

- Zotero 文献闭环
- source note 创建
- MOC 导航
- metadata 查询
- 周期复盘
- 格式治理

## 推荐优先级

### 立即整理

- 明确 Zotero Integration、Citations、ZotLit 的取舍。
- 配置 QuickAdd 的 2 到 3 个核心动作。
- 确认 Templater 模板目录指向 `08_templates/`。
- 用 Dataview 或 Bases 建立 source note 总览。

### 稳定后再做

- 为 project notes 建立 Bases 视图。
- 为 review due 建立回顾视图。
- 根据真实使用情况微调 Linter。
- 为重要主题建立 Excalidraw 知识地图。

### 暂不建议

- 继续增加新的 Zotero 类插件。
- 开启大量 Linter 自动改写规则。
- 把任务管理完全迁入 Obsidian，除非 project note 已经稳定运行。

## 一句话结论

当前插件安装方向总体正确，已经覆盖了文献、模板、查询、日记、格式、绘图和补全。下一步不需要继续装插件，而是要减少 Zotero 工作流重叠，补齐 QuickAdd 和查询视图，让插件真正服务于本知识库的日常闭环。
