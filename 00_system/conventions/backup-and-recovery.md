# 备份与恢复

## 必须备份

- `00_system/`
- `01_inbox/`
- `02_library/`
- `03_vault/`
- `04_outputs/`
- `90_archive/`
- 根目录说明文档

## 建议

- 至少保留本地副本和异地副本。
- 定期验证备份可以恢复，而不只是确认文件存在。
- 文档、模板和脚本建议纳入 Git；大 PDF 可用同步盘或其他备份策略。

## 恢复顺序

1. 恢复根目录说明文档和 `00_system/`。
2. 恢复 `02_library/`。
3. 恢复 `03_vault/`。
4. 恢复 `04_outputs/` 和 `90_archive/`。
5. 打开 Obsidian 与 Zotero，运行 `audit_system.py`。
