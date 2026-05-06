# Knowledge Hub 使用说明

这份说明面向“如何真正开始写这个知识库”。如果 `README.md` 告诉你系统有哪些部件，`PROJECT_MANUAL.md` 告诉你长期维护原则，那么这份文档就是日常操作手册：今天打开项目后，从哪里开始、资料怎么进来、笔记怎么写、Zotero 怎么衔接、什么时候让 Codex 帮你。

## 1. 先抓住一个核心模型

Knowledge Hub 不是一个单纯的文件夹，也不是一个单纯的 Obsidian vault。它由四层组成：

- `02_library/` 是实体资料主库，保存 PDF、书籍、课程、参考文件等真实文件。
- `03_vault/` 是 Obsidian 知识层，保存 MOC、source note、concept note、method note、question note、project note、daily note。
- Zotero 是文献元数据层，保存作者、年份、出版信息、引用、阅读状态和批注。
- `00_system/` 是规则和自动化层，保存分类法、命名规则、模板、脚本和维护清单。

最重要的一句话是：路径只放稳定维度，变化信息放 metadata、标签或正文。

稳定维度包括：

- 学科：例如 `philosophy`、`mathematics`、`artificial-intelligence`。
- 分支：例如 `yixue`、`analysis`、`machine-learning`。
- 资料类型：`books`、`papers`、`courses`、`reference`。

变化信息包括：

- 当前是否在读。
- 是否重要。
- 属于哪个项目。
- 下一步要不要精读。
- 是否已经输出成文章。

这些变化信息不要写进目录名，也不要写进实体文件名。这样几年后系统仍然不容易变乱。

## 2. 每次打开项目时先去哪里

日常入口建议固定为三个地方：

1. 项目根目录：`E:\BaiduSyncdisk\Project X\knowledge-hub`
2. Obsidian 首页：`03_vault/00_dashboard/Home.md`
3. 当前正在推进的项目笔记：例如 `03_vault/06_project-notes/yixue-introduction.md`

在命令行里先进入项目：

```powershell
cd "E:\BaiduSyncdisk\Project X\knowledge-hub"
```

如果你只是想写笔记，打开 Obsidian vault：

```text
E:\BaiduSyncdisk\Project X\knowledge-hub\03_vault
```

建议把 `03_vault/00_dashboard/Home.md` 当作 Obsidian 的首页。它不是内容仓库，而是导航台。

## 3. 目录怎么理解

### `00_system/`：系统规则

这里放规则，不放学习内容。

常用文件：

- `00_system/taxonomy/subjects.yaml`：所有合法学科和分支。
- `00_system/conventions/workflow.md`：资料进入系统的标准流程。
- `00_system/conventions/file-naming.md`：实体资料命名规则。
- `00_system/conventions/note-properties.md`：笔记 frontmatter 字段规则。
- `00_system/conventions/zotero-workflow.md`：Zotero 与本地文件库如何配合。
- `00_system/templates/`：系统模板。
- `00_system/scripts/`：自动化脚本。
- `00_system/checklists/`：周、月、季度维护清单。

### `01_inbox/`：所有新资料的入口

新资料不要直接放进 `02_library/`。先放这里。

- `01_inbox/10_new/`：刚拿到、还没处理的新资料。
- `01_inbox/20_triage/`：正在判断分类和去重的资料。
- `01_inbox/30_needs-metadata/`：作者、年份、标题等信息还不清楚的资料。
- `01_inbox/40_duplicates/`：重复资料。
- `01_inbox/90_rejected/`：明确不保留的资料。

### `02_library/`：实体资料主库

标准路径是：

```text
02_library/<subject_main>/<subject_branch>/<source_type_directory>/
```

例子：

```text
02_library/philosophy/yixue/10_books/谷继明 - 周易导读（2019）.pdf
```

注意：脚本参数里的 `source_type` 使用 `books`、`papers`、`courses`、`reference`，但实体目录名会映射成：

- `books` -> `10_books`
- `papers` -> `20_papers`
- `courses` -> `30_courses`
- `reference` -> `40_reference`

### `03_vault/`：Obsidian 笔记库

这里写知识，不存放实体资料。

- `00_dashboard/`：首页和仪表盘。
- `01_moc/`：Map of Content，每个学科的导航页。
- `02_source-notes/`：针对一本书、一篇论文、一门课、一份资料的笔记。
- `03_concept-notes/`：概念笔记。
- `04_method-notes/`：方法、技术、分析框架笔记。
- `05_question-notes/`：问题笔记。
- `06_project-notes/`：专题或写作项目笔记。
- `07_daily/`：日记、工作日志、当天处理记录。
- `08_templates/`：Obsidian 中直接复制使用的模板。
- `09_assets/`：图片、附件等笔记资产。
- `10_bases/`：Obsidian Bases 说明。

### `04_outputs/`：阶段性输出

这里放文章、讲稿、教学材料、总结等已经面向输出的东西。

如果你写的是“理解一个概念”，放 `03_vault/03_concept-notes/`。

如果你写的是“一篇准备发布或交付的文章”，放 `04_outputs/essays/`。

### `90_archive/`：归档区

旧项目、旧材料、低频使用材料可以归档到这里。不要把“不知道放哪”的东西丢进 archive，先放 inbox 或 `00_general`。

## 4. 一条资料从进入到沉淀的完整流程

这是最重要的闭环：

1. 把新文件放入 `01_inbox/10_new/`。
2. 判断它是不是重复资料。
3. 补齐作者、年份、标题。
4. 判断 `subject_main`、`subject_branch`、`source_type`。
5. 用 `intake_file.py --dry-run` 预览目标路径。
6. 确认无误后运行不带 `--dry-run` 的入库命令。
7. 在 Zotero 创建父条目。
8. 在 Zotero 中添加 linked attachment，指向 `02_library/` 里的真实文件。
9. 用 `new_source_note.py` 创建 source note。
10. 在 source note 中写 3 到 5 条核心内容。
11. 把 source note 链接到对应学科 MOC 或项目笔记。
12. 如果有值得长期复用的概念、方法或问题，再拆成 concept note、method note、question note。

不要一开始就追求每一步都完美。最小闭环是：资料入库、Zotero 有条目、source note 有 key、MOC 或项目笔记能找到它。

## 5. 如何给资料分类

分类只回答三个问题：

### 问题一：它属于哪个学科

合法学科来自 `00_system/taxonomy/subjects.yaml`。当前主学科包括：

- `mathematics`
- `physics`
- `computer-science`
- `artificial-intelligence`
- `psychology`
- `economics`
- `philosophy`
- `history`
- `social-science`
- `interdisciplinary`

不要临时创造学科名。比如不要写 `ai`，应该用 `artificial-intelligence`。

### 问题二：它属于哪个分支

分支也必须来自 `subjects.yaml`。

例子：

- 易学：`philosophy` / `yixue`
- 机器学习：`artificial-intelligence` / `machine-learning`
- 数学分析：`mathematics` / `analysis`
- 认知心理学：`psychology` / `cognitive`

如果暂时判断不了分支，放该学科的 `general`。在目录里它会表现为 `00_general`。

### 问题三：它是什么资料类型

只用这四种：

- `books`：书籍、专著、教材。
- `papers`：论文、预印本、学术文章。
- `courses`：课程视频、讲义、课程资料。
- `reference`：词条、网页、手册、数据表、政策文件、工具文档等参考材料。

不要新建 `articles`、`notes`、`slides` 之类的资料类型。除非你准备修改规则和脚本，否则保持四类稳定。

## 6. 实体文件怎么命名

目录名使用英文 slug，实体资料文件名可以保留中文。

命名规则：

- 论文：`年份 - 第一作者 - 短标题.pdf`
- 书籍：`作者 - 书名（年份）.pdf`
- 课程：`机构 - 课程名 - 年份.ext`
- 参考资料：`来源 - 标题（年份）.ext`

例子：

```text
2017 - Vaswani - Attention Is All You Need.pdf
谷继明 - 周易导读（2019）.pdf
MIT - Introduction to Algorithms - 2020.pdf
Stanford Encyclopedia of Philosophy - Causation（2024）.html
```

文件名不要写：

- `待读`
- `重要`
- `项目A`
- `精读版`
- `final`
- `已整理`

这些都属于状态或项目归属，应该放到 Zotero 标签、Obsidian frontmatter、项目笔记或正文里。

## 7. 常用脚本怎么用

所有命令都在项目目录运行：

```powershell
cd "E:\BaiduSyncdisk\Project X\knowledge-hub"
```

### 系统审计

每周至少跑一次：

```powershell
python 00_system/scripts/audit_system.py
```

如果系统 Python 不可用：

```powershell
.\run-audit.ps1
```

或者使用 Codex bundled Python：

```powershell
& "C:\Users\ExpiiD\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" 00_system/scripts/audit_system.py
```

审计会检查：

- inbox 是否有未归类文件。
- 是否出现主词表之外的 branch 目录。
- source note 是否缺少 `zotero_key`。
- 是否有明显空白或占位未填的笔记。
- library 和 source note 是否明显失衡。

### 入库文件

先 dry-run：

```powershell
python 00_system/scripts/intake_file.py --src "E:\Downloads\paper.pdf" --subject-main artificial-intelligence --subject-branch machine-learning --source-type papers --title "Attention Is All You Need" --author "Vaswani" --year 2017 --dry-run
```

确认目标路径正确后，再执行正式移动：

```powershell
python 00_system/scripts/intake_file.py --src "E:\Downloads\paper.pdf" --subject-main artificial-intelligence --subject-branch machine-learning --source-type papers --title "Attention Is All You Need" --author "Vaswani" --year 2017
```

入库脚本会根据资料类型生成规范文件名，并移动到对应 `02_library/` 路径。

### 创建 source note

```powershell
python 00_system/scripts/new_source_note.py --title "Attention Is All You Need" --subject-main artificial-intelligence --subject-branch machine-learning --zotero-key ABCD1234 --source-type papers
```

如果中文标题自动生成的文件名不理想，可以指定英文或拼音文件名：

```powershell
python 00_system/scripts/new_source_note.py --title "周易导读" --subject-main philosophy --subject-branch yixue --zotero-key ABCD1234 --source-type books --filename "gu-jiming-zhouyi-daodu-2019"
```

### 新增分支

只有在现有分支确实不够用时才新增。先 dry-run：

```powershell
python 00_system/scripts/add_branch.py --subject-main mathematics --branch-name dynamical-systems --branch-code MATH-DYN --dry-run
```

确认后再去掉 `--dry-run`。

新增分支不是“建一个文件夹”这么简单。它会影响 taxonomy、library、source notes、concept notes、method notes 等多个位置，所以要谨慎。

## 8. Zotero 应该怎么配合

Zotero 不做实体文件主库，`02_library/` 才是实体文件主库。

推荐方式：

1. 在 Zotero 中创建父条目。
2. 补齐作者、年份、标题、出版信息。
3. 给父条目添加 child attachment。
4. attachment 使用 linked attachment，指向 `02_library/` 中的真实文件。
5. 在 Obsidian source note 的 `zotero_key` 字段填写 Zotero key。

Zotero 负责：

- 作者。
- 年份。
- 出版信息。
- 引用格式。
- 阅读状态。
- 文献标签。
- PDF 批注。

Obsidian 负责：

- 这份资料对我有什么用。
- 它讲了什么。
- 它和哪些概念、问题、项目有关。
- 我下一步要读什么、写什么、比较什么。

一个实用判断：如果信息是“文献事实”，放 Zotero；如果信息是“我的理解和组织”，放 Obsidian。

## 9. 笔记类型怎么选

### Source note：一份资料的入口

适合：

- 一本书。
- 一篇论文。
- 一门课。
- 一份报告。
- 一个网页参考资料。

路径：

```text
03_vault/02_source-notes/<subject_main>/<subject_branch>/
```

source note 至少应该包含：

- `type: source-note`
- `subject_main`
- `subject_branch`
- `source_type`
- `status`
- `zotero_key`
- 核心内容 3 到 5 条
- 关联笔记或 MOC 链接

写法建议：

- 不要把整本书机械摘抄进去。
- 先写“这份资料解决什么问题”。
- 再写“对我当前项目或知识网络有什么用”。
- 有疑问就明确写到“我的问题”里。

### Concept note：一个概念的稳定解释

适合：

- “阴阳”
- “贝叶斯推断”
- “注意力机制”
- “交易成本”
- “范畴错误”

concept note 要写自己的最小可用定义。不要只复制百科。

推荐结构：

- 定义：一句话说清。
- 边界：它不是什么。
- 混淆：容易和什么概念混。
- 来源：来自哪些 source notes。
- 关联：链接相关概念和问题。

### Method note：一个方法或分析框架

适合：

- “如何读一篇论文”
- “文本细读法”
- “贝叶斯建模流程”
- “因果识别策略”
- “易学象数分析路径”

method note 应该写成以后能复用的流程或判断框架。

### Question note：一个尚未解决的问题

适合：

- “《周易》的经传关系应如何入门？”
- “注意力机制到底替代了什么？”
- “为什么某个理论在两个领域有不同含义？”

question note 的价值在于把模糊卡点变成可追踪对象。一个好问题可以连接多个 source note 和 concept note。

### Project note：一个阶段性目标

适合：

- “易学导论”
- “机器学习论文阅读计划”
- “写一篇关于某主题的综述”
- “准备一组课程讲稿”

project note 不只是清单，它是一个工作台。

它应该包含：

- 目标。
- 范围。
- 输入资料。
- 当前进展。
- 下一步。
- 可能的输出物。

### Daily note：当天工作日志

适合：

- 今天处理了哪些资料。
- 今天理解了什么。
- 今天卡在哪里。
- 明天最小下一步是什么。

daily note 不需要优雅。它的任务是降低重新进入项目的成本。

## 10. MOC 应该怎么写

MOC 是 Map of Content，也就是某个学科或专题的导航页。它不是资料清单的垃圾桶，而是结构化入口。

一个好的 MOC 应该回答：

- 这个领域我目前有哪些入口？
- 重要资料在哪里？
- 核心概念有哪些？
- 当前项目有哪些？
- 哪些问题还没解决？
- 下一步应该读什么或写什么？

不要把每个 source note 都机械塞进 MOC。优先链接：

- 对领域理解有组织作用的资料。
- 当前项目正在用的资料。
- 能支撑概念网络的资料。
- 你会反复回来的资料。

如果某份资料只是暂时存档，可以只保留 source note，不急着进 MOC。

## 11. 推荐的日常写作流程

### 15 分钟快速维护

适合忙的时候：

1. 打开 `03_vault/00_dashboard/Home.md`。
2. 检查 `01_inbox/10_new/` 是否有新资料。
3. 只处理 1 个文件。
4. 创建或补齐 1 个 source note。
5. 在项目笔记或 MOC 加 1 条链接。
6. 写下明天的最小下一步。

### 45 分钟学习推进

适合正常学习日：

1. 打开当前 project note。
2. 选择 1 份 source note 或 1 个问题。
3. 阅读资料的一小段，不追求读完。
4. 在 source note 中写 3 到 5 条理解。
5. 拆出 1 个 concept note 或 question note。
6. 更新 project note 的“当前进展”和“下一步”。

### 90 分钟深度整理

适合周末或集中整理：

1. 跑 `audit_system.py`。
2. 清理 inbox。
3. 修复缺失的 Zotero key 或空白笔记。
4. 整理一个学科 MOC。
5. 把多个 source notes 中重复出现的概念合并成 concept note。
6. 选择一个输出方向，放入 `04_outputs/`。

## 12. 如何让 Codex 高效帮你

你可以把 Codex 当成知识库维护伙伴，而不只是代码助手。

有效请求示例：

```text
请检查 inbox 里有哪些资料还没入库，并按当前 taxonomy 给我建议分类。
```

```text
请根据 02_library/philosophy/yixue/10_books/ 里的资料，帮我创建对应 source note 草稿。
```

```text
请审计这个知识库，指出最影响使用效率的 5 个问题，并帮我修复能自动修复的部分。
```

```text
请把 Philosophy MOC 整理成更适合易学入门项目使用的导航页。
```

```text
请根据这份 source note，拆出 3 个 concept notes 和 2 个 question notes。
```

```text
请帮我把今天处理过的内容整理成 daily note。
```

给 Codex 的请求越具体越好。最好包含：

- 处理对象：哪个目录、哪个文件、哪个项目。
- 目标：入库、整理、写 source note、更新 MOC、审计。
- 约束：不要新增分支、先 dry-run、不要覆盖已有笔记。

如果你不确定怎么问，可以直接说：

```text
我现在不知道下一步怎么推进，请你先检查项目状态，再给我一个最小可执行计划，并帮我完成第一步。
```

## 13. 新手最容易卡住的地方

### 卡点一：不知道放哪个分支

先放对应学科的 `general`，也就是目录里的 `00_general`。

不要为了一个文件新增分支。等某个主题积累了多份资料、多条笔记、多个问题，再考虑新增分支。

### 卡点二：source note 不知道写什么

只写四句也可以：

- 这份资料讨论什么？
- 它最重要的观点是什么？
- 它和我当前项目有什么关系？
- 我还有什么问题？

source note 的第一版只需要能让未来的你知道“为什么留它”。

### 卡点三：想把所有东西整理完再开始学

不要这么做。知识库不是装修完才入住的房子，它更像厨房：边做饭边收拾，反而最知道刀该放哪。

优先跑通一个完整闭环，而不是填满所有空目录。

### 卡点四：Zotero 和 Obsidian 重复记录

用这个判断：

- 客观文献信息放 Zotero。
- 主观理解和知识连接放 Obsidian。
- 实体文件放 `02_library/`。

### 卡点五：MOC 变成超长链接列表

MOC 只放导航价值高的链接。普通资料可以留在 source note 层，不必全部进入 MOC。

## 14. 当前项目的建议起步路线

这个仓库里已经有一个很好的样例起点：

```text
02_library/philosophy/yixue/10_books/谷继明 - 周易导读（2019）.pdf
03_vault/06_project-notes/yixue-introduction.md
```

建议先把“易学导论”跑通：

1. 在 Zotero 中为《周易导读》创建条目。
2. 使用 linked attachment 指向 `02_library/philosophy/yixue/10_books/谷继明 - 周易导读（2019）.pdf`。
3. 获取 Zotero key。
4. 创建 source note：

```powershell
python 00_system/scripts/new_source_note.py --title "谷继明 - 周易导读（2019）" --subject-main philosophy --subject-branch yixue --source-type books --zotero-key YOURKEY --filename "gu-jiming-zhouyi-daodu-2019"
```

5. 在 source note 里写 3 到 5 条核心内容。
6. 把 source note 链接到 `03_vault/06_project-notes/yixue-introduction.md`。
7. 把重要入口链接到 `03_vault/01_moc/philosophy/Philosophy MOC.md`。
8. 跑审计：

```powershell
python 00_system/scripts/audit_system.py
```

当前审计提示 `philosophy` 的 library 文件数和 source note 数失衡，所以这个起步路线正好能修复最明显的系统缺口。

## 15. 每周维护清单

每周找一个固定时间做一次即可。

1. 运行：

```powershell
python 00_system/scripts/audit_system.py
```

2. 清空或推进 `01_inbox/10_new/`。
3. 检查 `01_inbox/30_needs-metadata/` 是否有长期卡住的资料。
4. 给最近新增的重要资料补 Zotero key。
5. 给最近新增的重要 source note 回链到 MOC 或 project note。
6. 看 `03_vault/05_question-notes/` 是否有可以推进或关闭的问题。
7. 更新当前 project note 的“当前进展”和“下一步”。
8. 如果某个主题已经沉淀出成果，考虑放到 `04_outputs/`。

## 16. 什么时候修改系统结构

只有在这些情况出现时，才考虑改结构：

- 某个新分支已经有多份资料，并且长期会增长。
- 现有四种 source type 无法表达一类稳定资料。
- 某个模板反复让你填无用字段。
- 审计脚本反复报同类问题，但不是内容问题，而是规则不适配。

修改结构的顺序：

1. 先修改 `00_system/` 中的规则文档。
2. 再修改脚本或 taxonomy。
3. 再生成或移动目录。
4. 最后修改具体内容。
5. 跑审计确认没有破坏系统约束。

不要先手动建一堆目录，再回头补规则。那样很容易变成一座自我增殖的小迷宫，迷宫很酷，但找资料时会想捶桌。

## 17. 遇到新技术时怎么办

新技术出现时，不要先问“我要不要立刻全面迁移”，先问“它会增强哪一层”。

一个实用判断是：

- 如果它增强检索、总结、链接、批注、自动化，可以先小范围接入。
- 如果它要求你改写全部目录、笔记格式或资料存储方式，就先停一下。
- 如果它不能稳定导出数据，或者退出成本很高，要特别谨慎。

推荐做法：

1. 先拿一个小专题试用，而不是整个知识库一起迁。
2. 保持 `02_library/` 不动，把新工具当外围能力。
3. 尽量继续让笔记保留在 Markdown。
4. 如果要改字段、模板或 taxonomy，先改 `00_system/` 规则。
5. 试用结束后，判断它是“长期适配层”还是“一次性新鲜玩具”。

可替换的通常是：

- 插件。
- 自动化脚本。
- 某种 AI 整理流程。
- 某种阅读或标注工具。

不应轻易替换的是：

- `02_library/` 作为实体主库的地位。
- `03_vault/` 作为知识组织层的职责。
- taxonomy 作为稳定分类依据的角色。
- “路径表达稳定维度，变化信息写在 metadata/正文里”的原则。

如果你以后想系统性评估一项新工具，可以回看 [PROJECT_MANUAL.md](PROJECT_MANUAL.md) 里的“防过时原则”。

## 18. 最小可行习惯

如果你只想记住一套最小习惯，就记这个：

1. 新资料先放 `01_inbox/10_new/`。
2. 不确定分支就放 `general`。
3. 入库前先 dry-run。
4. 每份重要资料至少有一个 source note。
5. source note 必须有 `zotero_key`，如果暂时没有，就把“补 Zotero key”写成待办。
6. 重要 source note 至少链接到一个 MOC 或 project note。
7. 每周跑一次 `audit_system.py`。

只要这七件事做到，知识库就会稳稳长起来。

## 19. 快速参考

常用路径：

```text
00_system/taxonomy/subjects.yaml
00_system/conventions/workflow.md
00_system/conventions/file-naming.md
00_system/conventions/note-properties.md
00_system/conventions/zotero-workflow.md
01_inbox/10_new/
02_library/
03_vault/00_dashboard/Home.md
03_vault/01_moc/
03_vault/02_source-notes/
03_vault/06_project-notes/
03_vault/08_templates/
04_outputs/
```

常用命令：

```powershell
cd "E:\BaiduSyncdisk\Project X\knowledge-hub"
python 00_system/scripts/audit_system.py
python 00_system/scripts/intake_file.py --src "E:\Downloads\paper.pdf" --subject-main artificial-intelligence --subject-branch machine-learning --source-type papers --title "Attention Is All You Need" --author "Vaswani" --year 2017 --dry-run
python 00_system/scripts/new_source_note.py --title "Attention Is All You Need" --subject-main artificial-intelligence --subject-branch machine-learning --zotero-key ABCD1234 --source-type papers
```

最重要的判断：

```text
文件在哪里？02_library
文献信息在哪里？Zotero
我的理解在哪里？03_vault
规则在哪里？00_system
临时入口在哪里？01_inbox
成果在哪里？04_outputs
```
