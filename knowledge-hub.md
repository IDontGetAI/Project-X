# Knowledge Hub 使用指南

这个知识库的核心流程可以记成一句话：

`文件先进入 inbox，再进 library；Zotero 管条目和批注；Obsidian 管笔记和知识网络；Codex 管规则、模板和脚本。`

## 第一次使用

1. 用 Obsidian 打开 `03_vault/`。
2. 从 `03_vault/00_dashboard/Home.md` 进入各学科 MOC。
3. 阅读 `README.md`、`PROJECT_MANUAL.md` 和 `00_system/conventions/workflow.md`。
4. 确认 Zotero 使用 linked attachment 指向 `02_library/`。

## 日常新增资料

1. 把新文件放入 `01_inbox/10_new/`。
2. 判断学科、分支和资料类型。
3. 使用 `intake_file.py --dry-run` 检查目标路径。
4. 确认无误后正式入库。
5. 在 Zotero 创建父条目并挂载 linked attachment。
6. 使用 `new_source_note.py` 创建 source note。
7. 将 source note 回链到对应 MOC。

## 笔记类型

- source note：单份资料的结构化阅读笔记。
- concept note：跨资料反复出现、值得独立维护的概念。
- method note：可复用的方法、证明、算法、流程或阅读策略。
- question note：值得持续追踪的问题。
- project note：阶段性学习、写作或研究项目。
- daily note：每日输入、理解、问题和下一步。

## 常用命令

```powershell
python 00_system/scripts/audit_system.py
python 00_system/scripts/intake_file.py --src "E:\Downloads\paper.pdf" --subject-main artificial-intelligence --subject-branch machine-learning --source-type papers --title "Attention Is All You Need" --author "Vaswani" --year 2017 --dry-run
python 00_system/scripts/new_source_note.py --title "Attention Is All You Need" --subject-main artificial-intelligence --subject-branch machine-learning --zotero-key ABCD1234 --source-type papers
```

## 最小维护节奏

- 每日：处理少量 inbox，补一条 source note 或 daily note。
- 每周：清理 inbox，运行 `audit_system.py`，把新增笔记接入 MOC。
- 每月：检查 taxonomy、模板、备份和目录结构是否仍可维护。

当前最值得跑通的样例是《周易导读》：它已经在 `02_library/philosophy/yixue/10_books/` 中，下一步是建立 Zotero 条目和 source note。
