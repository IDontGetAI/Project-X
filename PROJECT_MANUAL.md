# Knowledge Hub 项目手册

## 设计目标

这个系统服务于长期、多学科、可迁移的学习工作流。核心目标不是堆出复杂结构，而是建立一套几年尺度上仍能运行的本地知识基础设施。

## 分层职责

- 文件系统主库：`02_library/` 保存实体资料，便于备份、迁移和跨工具访问。
- Obsidian 笔记层：`03_vault/` 管理 MOC、概念、方法、问题、项目和日常记录。
- Zotero 元数据层：管理作者、年份、出版信息、标签、批注、阅读状态和引用。
- Codex 自动化层：维护规则、模板、脚本、审计和批处理流程。

## 目录原则

- 顶层目录少而稳定。
- `02_library/<subject>/<branch>/<source_type>/` 是实体资料标准路径。
- `subject_main` 与 `subject_branch` 取自 `00_system/taxonomy/subjects.yaml`。
- `source_type` 固定为 `books`、`papers`、`courses`、`reference`。
- 项目、状态、优先级、地区、时期等变化较快的信息放到 metadata、标签或笔记正文。

## 维护节奏

### 每日

- 清理当天新增资料的最小 intake。
- 至少为一条重要资料建立或补齐 source note。
- 在 daily note 中记录输入、理解、问题和下一步。

### 每周

- 清理 `01_inbox/`。
- 补齐 `zotero_key`、作者、年份和阅读状态。
- 检查最近新增资料是否已接入 MOC。
- 跑一次 `audit_system.py`。

### 每月

- 检查目录是否失控，是否出现标签爆炸、孤儿笔记或无效链接。
- 检查模板与脚本是否仍贴合当前工作流。

## 常见反模式

- 跳过 inbox，直接把文件扔进 `02_library/`。
- 把状态、项目名或优先级写进目录。
- 为一两个资料临时新增分支。
- 在 Zotero 中保存附件副本，而不是 linked attachment。
- 创建 source note 后长期不补 `zotero_key`、作者和年份。

## 推荐下一步

先用 `02_library/philosophy/yixue/10_books/谷继明 - 周易导读（2019）.pdf` 跑通完整闭环：Zotero 条目、source note、项目笔记、MOC 回链、审计通过。一个完整样例比大量空模板更有价值。
