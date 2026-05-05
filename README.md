# Knowledge Hub

Knowledge Hub 是一个面向长期学习的本地知识库。它把实体资料、Obsidian 笔记、Zotero 元数据和 Codex 自动化分开维护，目标是让资料进入系统的路径清晰、目录结构稳定、维护成本可控。

## 根目录

- `00_system/`：系统规则、主词表、模板、脚本和维护清单。
- `01_inbox/`：新资料入口，完成去重、命名和分类后再入库。
- `02_library/`：实体资料主库，按 `学科 / 分支 / 资料类型` 落盘。
- `03_vault/`：Obsidian 笔记库，包含 MOC、source notes、concept notes、method notes、question notes、project notes 和 daily notes。
- `04_outputs/`：写作、讲稿、教学、总结等阶段性输出。
- `90_archive/`：旧项目、旧产出和低频使用材料。
- `AGENTS.md`：Codex 在本项目中的工作协议。
- `PROJECT_MANUAL.md`：长期维护手册。

## 标准流程

1. 新资料进入 `01_inbox/10_new/`。
2. 去重，重复文件移到 `01_inbox/40_duplicates/`，明确不需要的移到 `01_inbox/90_rejected/`。
3. 按规则重命名，并补齐基础 metadata。
4. 判断 `subject_main`、`subject_branch`、`source_type`。
5. 移动到 `02_library/<subject>/<branch>/<type>/`。
6. 在 Zotero 创建父条目，使用 linked attachment 指向 `02_library/` 中的真实文件。
7. 在 `03_vault/02_source-notes/` 创建 source note，并回链到对应 MOC。
8. 需要时再抽取 concept note、method note 或 question note。

## 常用命令

```powershell
python 00_system/scripts/audit_system.py
python 00_system/scripts/new_source_note.py --title "周易导读" --subject-main philosophy --subject-branch yixue --source-type books --zotero-key YOURKEY
python 00_system/scripts/intake_file.py --src "E:\temp\book.pdf" --subject-main philosophy --subject-branch yixue --source-type books --title "周易导读" --author "谷继明" --year 2019 --dry-run
```

如果系统 `python` 不可用，可以直接运行：

```powershell
.\run-audit.ps1
```

也可以使用 Codex bundled Python：

```powershell
& "C:\Users\ExpiiD\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" 00_system/scripts/audit_system.py
```

## 维护原则

- 路径只表达稳定维度；状态、优先级、项目归属等放入 metadata、标签或笔记正文。
- 先维护规则和脚本，再维护具体内容。
- 每周至少运行一次 `audit_system.py` 并完成 `00_system/checklists/weekly-review.md`。
