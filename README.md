# GitHub Copilot Code Review 测试项目

本项目用于测试 **GitHub Copilot 的代码审查功能**。

## 📚 文档

- **[最佳实践指南](BEST_PRACTICES.md)** ⭐ - 推荐阅读，了解如何高效使用 Copilot 审查
- 示例代码：[example.py](example.py) | [example.js](example.js)

## 🚀 快速开始（3 步）

### 1. 启用 Copilot PR Summaries（推荐）

访问 https://github.com/settings/copilot，启用 **"Pull request summaries"**

✅ 这是最简单有效的方式！

### 2. 推送代码到 GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ai-review-test.git
git push -u origin main
```

### 3. 创建 PR 并使用 Copilot

```bash
# 创建功能分支
git checkout -b feature/test-review
echo "def new_feature(): pass" >> example.py
git add example.py
git commit -m "Add new feature"
git push origin feature/test-review
```

在 GitHub 上创建 PR，然后在评论中输入：
```
@copilot review
```

**就这么简单！** 🎉

## 💡 Copilot 命令参考

在 PR 评论中可以使用：

```
@copilot review                           # 完整代码审查
@copilot 这段代码有什么安全问题？           # 安全检查
@copilot 如何优化性能？                    # 性能建议
@copilot 解释这段代码的逻辑                # 代码解释
```

## 🎯 项目特点

本项目的示例代码故意包含一些常见问题，非常适合测试 Copilot 的审查能力：

### Python 代码 (example.py) 的问题
- ❌ 使用 `range(len())` 反模式
- ❌ 缺少类型提示和错误处理
- ❌ 变量命名使用了内置名称
- ❌ 缺少边界检查

### JavaScript 代码 (example.js) 的问题
- ❌ 硬编码凭证（安全风险）
- ❌ 使用 `var` 和 `==`（不推荐）
- ❌ 缺少错误处理
- ❌ XSS 风险（直接使用 innerHTML）

## 📖 了解更多

- **[BEST_PRACTICES.md](BEST_PRACTICES.md)** - Copilot Code Review 最佳实践
- [GitHub Copilot 文档](https://docs.github.com/en/copilot)
- [Copilot in Pull Requests](https://docs.github.com/en/copilot/github-copilot-chat/copilot-chat-in-github)

---

**开始测试：** 创建一个 PR，在评论中输入 `@copilot review` 试试看！ 🚀
