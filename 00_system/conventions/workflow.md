# 标准工作流

## 1. 新文件进入 inbox

- 所有新资料先进入 `01_inbox/10_new/`。
- 不跳过 inbox 直接进入 `02_library/`。

## 2. 去重

- 检查 inbox、`02_library/` 和 Zotero 是否已有同一资料。
- 重复文件移到 `01_inbox/40_duplicates/`。
- 不保留的文件移到 `01_inbox/90_rejected/`。

## 3. 命名与分类

- 按 `file-naming.md` 重命名。
- 判断 `subject_main`、`subject_branch`、`source_type`。
- 不确定分支时先放到对应学科的 `00_general/`。

## 4. 入库

- 目标路径：`02_library/<subject>/<branch>/<type>/`。
- 建议用 `intake_file.py --dry-run` 先检查目标路径。

## 5. Zotero 与笔记

- 在 Zotero 创建父条目，并使用 linked attachment 指向 `02_library/` 中的真实文件。
- 在 `03_vault/02_source-notes/` 创建 source note。
- 将 source note 回链到对应 MOC 或项目笔记。
