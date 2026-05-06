# Git 提交与推送规范

这份文档定义本项目中 `git add`、`git commit`、`git push` 的使用规范。目标不是增加流程负担，而是让版本历史清楚、回滚安全、协作省心。

## 1. 先记住三个原则

### 原则一：一次提交只表达一个主要意图

一个 commit 最好只回答一个问题：

- 我新增了什么？
- 我整理了什么？
- 我修复了什么？
- 我调整了什么结构？

不要把规则修改、笔记内容、图片资源、实验文件和临时清理全塞进同一个 commit，除非它们本来就是同一件事的一部分。

### 原则二：先看清范围，再暂存

在执行 `git add` 之前，先确认：

- 哪些文件真的要进这次提交。
- 哪些文件只是临时产物。
- 哪些文件是还没整理好的内容。

推荐先看状态：

```powershell
git status --short
```

如果范围不清楚，不要直接 `git add -A`。

### 原则三：本地提交和远程推送是两步

- `git commit` 是把变更写进本地历史。
- `git push` 是把本地历史发到 GitHub。

也就是说，提交成功不等于已经上传。推送前要确认当前分支和远程目标。

## 2. `git add` 规范

`git add` 的作用是把你想提交的内容放进暂存区。它不是“顺手一把全塞进去”的按钮，而是决定“这次提交到底包含什么”的关口。

### 推荐做法

优先按文件或目录精确暂存：

```powershell
git add README.md
git add PROJECT_MANUAL.md
git add 00_system/conventions/git-workflow.md
git add 03_vault/06_project-notes/yixue-introduction.md
```

如果一类改动都在同一个目录，也可以按目录暂存：

```powershell
git add 03_vault/02_source-notes/philosophy/yixue
git add 00_system/conventions
```

暂存后立刻检查：

```powershell
git status --short
git diff --cached --stat
```

### 什么时候可以用 `git add -A`

只有在你明确知道“当前工作区的所有变化都应该进入同一次提交”时，才使用：

```powershell
git add -A
```

典型适用场景：

- 一次完整的规则整理。
- 一次明确范围的内容迁移。
- 你已经看过 `git status`，确认所有改动都要提交。

### 不推荐的做法

- 不看状态直接 `git add -A`
- 把未整理好的截图、缓存、实验文件一起加进去
- 自己也说不清这次到底加了什么

## 3. `git commit` 规范

`git commit` 的作用是把暂存区内容保存为一个本地版本节点。

### 提交前检查

在 commit 之前，至少看这三样：

```powershell
git status --short
git diff --cached --stat
git diff --cached
```

你不一定每次都要逐行细看，但至少要知道：

- 这次提交了哪些文件
- 改动量大概多大
- 有没有明显误加的内容

### 提交信息格式

推荐使用：

```text
动作 + 对象
```

例如：

- `Add source notes for linear algebra lecture 1`
- `Refine knowledge hub usage guide`
- `Document Git workflow conventions`
- `Update philosophy MOC links`
- `Add branch for dynamical systems`
- `Clean up inbox duplicates`

### 常用动作词

- `Add`：新增内容
- `Update`：更新已有内容
- `Refine`：优化表达或结构
- `Document`：补充说明文档
- `Reorganize`：重组目录或内容
- `Fix`：修复错误
- `Remove`：删除不再需要的内容

### 推荐示例

```powershell
git commit -m "Document Git workflow conventions"
git commit -m "Add source notes for linear algebra lecture 1"
git commit -m "Refine knowledge hub usage guide"
```

### 不推荐的提交信息

- `update`
- `fix`
- `misc`
- `changes`
- `tmp`

这些信息以后几乎没有回看价值。

## 4. `git push` 规范

`git push` 的作用是把本地 commit 上传到远程仓库。

### 推送前检查

先确认当前分支：

```powershell
git branch --show-current
```

再看最近提交：

```powershell
git log --oneline -3
```

确认没问题后再推：

```powershell
git push origin main
```

如果是第一次把本地分支和远程分支绑定，可以使用：

```powershell
git push -u origin main
```

### 推送后的确认

推送完成后，建议再看一次状态：

```powershell
git status --short
```

如果工作区是空的，说明本地没有遗留未提交改动。

如果你想确认远端头部是否一致，可以看：

```powershell
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

两边哈希一致，就说明远端已经和本地对齐。

## 5. 推荐工作流

这是本项目里最稳妥的一套日常节奏：

1. 修改内容
2. `git status --short`
3. `git add <明确文件或目录>`
4. `git diff --cached --stat`
5. `git commit -m "动作 + 对象"`
6. `git push origin main`

标准示例：

```powershell
git status --short
git add README.md PROJECT_MANUAL.md 00_system/conventions/git-workflow.md
git diff --cached --stat
git commit -m "Document Git workflow conventions"
git push origin main
```

## 6. 适合本项目的提交拆分方式

这个知识库的改动大致分四类，推荐拆开：

### 规则类

包括：

- `00_system/conventions/`
- `00_system/templates/`
- `00_system/scripts/`
- `README.md`
- `PROJECT_MANUAL.md`
- `USAGE_GUIDE.md`

推荐提交示例：

```text
Document Git workflow conventions
Refine knowledge hub usage guide
Update source note template rules
```

### 内容类

包括：

- `03_vault/02_source-notes/`
- `03_vault/03_concept-notes/`
- `03_vault/04_method-notes/`
- `03_vault/06_project-notes/`
- `03_vault/07_daily/`
- `03_vault/01_moc/`

推荐提交示例：

```text
Add source notes for Zhouyi reading
Update philosophy MOC for yixue project
Refine project notes for knowledge hub setup
```

### 资源类

包括：

- 图片
- 截图
- 图表
- 课程讲义附件
- source note 下的 `assets/`

推荐提交示例：

```text
Add figures for linear algebra lecture 1
Add reference images for philosophy notes
```

### 结构类

包括：

- 大规模目录迁移
- branch 扩展
- 批量重命名
- taxonomy 结构调整

推荐提交示例：

```text
Add branch for dynamical systems
Reorganize philosophy source note structure
```

## 7. 常见场景用法

### 场景一：只改了说明文档

```powershell
git status --short
git add README.md PROJECT_MANUAL.md USAGE_GUIDE.md
git commit -m "Refine knowledge hub documentation"
git push origin main
```

### 场景二：新增一组 source notes

```powershell
git status --short
git add 03_vault/02_source-notes/mathematics/algebra/linear-algebra
git commit -m "Add source notes for linear algebra lecture 1"
git push origin main
```

### 场景三：规则和内容都改了

更推荐拆成两次提交：

```powershell
git add 00_system/conventions/git-workflow.md PROJECT_MANUAL.md
git commit -m "Document Git workflow conventions"

git add 03_vault/06_project-notes/yixue-introduction.md
git commit -m "Refine yixue project note"

git push origin main
```

### 场景四：你不确定哪些文件该提交

先不要 `git add -A`。先看：

```powershell
git status --short
```

然后逐个判断。必要时只加最明确的几项。

## 8. 常见错误

### 错误一：提交前不看状态

后果：

- 容易把不相关文件一起提交
- 事后很难解释这个 commit 在做什么

### 错误二：一个 commit 混太多东西

后果：

- 以后难以回滚
- 以后难以理解历史
- 以后很难从历史里找到某类变化

### 错误三：提交信息太含糊

后果：

- 一周后你自己都看不懂
- 协作者更看不懂

### 错误四：commit 了但没 push

后果：

- 本地有历史，GitHub 上却没有
- 你以为上传了，其实还在自己电脑里

## 9. 一句话总结

`git add` 决定范围，`git commit` 记录意图，`git push` 发布结果。

只要每次都做到“先看状态、再精确暂存、提交信息说人话、推送前确认分支”，这个项目的 Git 历史就会一直很清楚。

## 10. 如何在每次 Git 时调用这份规范

本项目提供了三种直接可用的入口：

### 主动检查入口

运行：

```powershell
& ".\00_system\scripts\git-safe.ps1"
```

它会显示：

- 当前分支
- 工作区状态
- 已暂存改动摘要
- 最近提交
- 推荐的下一步 Git 顺序

如果你只是想快速查看而不暂停，可以运行：

```powershell
& ".\00_system\scripts\git-safe.ps1" -NoPause
```

### 本地自动护栏

运行一次：

```powershell
& ".\00_system\scripts\enable-git-guardrails.ps1"
```

它会为当前仓库设置两项本地 Git 配置：

- `core.hooksPath = .githooks`
- `commit.template = 00_system/templates/git-commit-template.txt`

启用后：

- 每次 `git push` 前都会显示一段本项目的 pre-push 检查提醒。
- 每次 `git commit` 都会自动带出提交信息模板。

### 推荐使用方式

每次准备提交时：

```powershell
& ".\00_system\scripts\git-safe.ps1"
git add <明确文件或目录>
git diff --cached --stat
git commit
git push origin main
```

这样你不是靠记忆执行规范，而是把规范变成了实际入口。
