# GitHub Copilot 自动审查触发选项

## ✅ 方案 1：启用 GitHub Copilot Pull Request Summaries（推荐）

**最简单直接的方法，GitHub 原生支持**

### 个人账户启用：
1. 访问 GitHub 个人设置：https://github.com/settings/copilot
2. 向下滚动到 **"Copilot in GitHub.com"** 部分
3. 找到并启用：
   - ✅ **"Pull request summaries"** - 自动生成 PR 摘要
   - ✅ **"Copilot in the CLI"** - 命令行支持（可选）

### 组织账户启用：
1. 访问组织设置：`https://github.com/organizations/YOUR_ORG/settings/copilot`
2. 找到 **"Policies"** 或 **"Features"** 部分
3. 启用：
   - ✅ **"Copilot pull request summaries"**
   - ✅ **"Allow Copilot to review code"**

### 效果：
- 📝 每次创建或更新 PR 时，Copilot 自动生成摘要
- 🤖 在 PR 描述中自动添加代码变更说明
- 🔍 可以点击 Copilot 按钮获取更详细的分析

---

## ✅ 方案 2：使用 GitHub Actions 自动触发（已配置）

**通过工作流自动化，每次 PR 时自动请求审查**

我已经为您创建了 `.github/workflows/copilot-review.yml`

### 工作原理：
- 当 PR 创建、更新或重新打开时自动触发
- 自动在 PR 中添加 `@copilot review` 评论
- 无需手动输入命令

### 启用步骤：
```bash
# 提交 workflow 文件
git add .github/workflows/copilot-review.yml
git commit -m "Add GitHub Actions workflow for auto Copilot review"
git push origin main
```

### 自定义审查内容：
编辑 `.github/workflows/copilot-review.yml` 文件中的 `body` 部分：
```javascript
body: '@copilot review this PR for:\n- Security vulnerabilities\n- Code quality issues\n- Performance problems\n- Best practices violations'
```

---

## ✅ 方案 3：使用 Pull Request 模板（已配置）

**在 PR 创建时自动包含 Copilot 审查请求**

我已经为您创建了 `.github/pull_request_template.md`

### 工作原理：
- 创建新 PR 时，GitHub 自动使用这个模板
- 模板中已包含 `@copilot` 审查请求
- 创建 PR 后立即触发审查

### 启用步骤：
```bash
# 提交模板文件
git add .github/pull_request_template.md
git commit -m "Add PR template with auto Copilot review request"
git push origin main
```

### 效果：
每次创建 PR 时，描述中自动包含：
```
@copilot 请审查这个 PR，重点关注：
- 代码质量和可维护性
- 潜在的安全问题
- 性能优化建议
- 是否符合最佳实践
```

---

## ✅ 方案 4：使用 CODEOWNERS + 分支保护

**结合代码所有权和审查要求**

### 步骤 1：创建 CODEOWNERS 文件
```bash
# 创建 .github/CODEOWNERS
cat > .github/CODEOWNERS << 'EOF'
# 代码所有者配置
# 所有 Python 文件需要审查
*.py @your-team-name

# 所有 JavaScript 文件需要审查
*.js @your-team-name

# 关键文件需要额外审查
/src/security/* @security-team
EOF
```

### 步骤 2：配置分支保护规则
1. 进入仓库 **Settings** → **Branches**
2. 添加 branch protection rule for `main`
3. 启用：
   - ✅ **"Require a pull request before merging"**
   - ✅ **"Require approvals"**
   - ✅ **"Require status checks to pass"**

这样可以确保每个 PR 都经过审查。

---

## ✅ 方案 5：使用 GitHub CLI 或 API 自动化

**通过脚本或 CI/CD 集成**

### 示例脚本：
```bash
#!/bin/bash
# auto-copilot-review.sh

PR_NUMBER=$1
REPO_OWNER="your-username"
REPO_NAME="ai-review-test"

# 使用 GitHub CLI 添加评论
gh pr comment $PR_NUMBER \
  --repo "$REPO_OWNER/$REPO_NAME" \
  --body "@copilot review this PR comprehensively"

echo "Copilot review requested for PR #$PR_NUMBER"
```

### 在 CI/CD 中使用：
```yaml
# 在你的 .github/workflows 中
- name: Auto request Copilot review
  run: |
    gh pr comment ${{ github.event.pull_request.number }} \
      --body "@copilot review this PR"
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## 📊 方案对比

| 方案 | 难度 | 自动化程度 | 维护成本 | 推荐度 |
|------|------|-----------|----------|--------|
| **1. PR Summaries** | ⭐ 极简单 | ⭐⭐⭐⭐⭐ | 无 | ⭐⭐⭐⭐⭐ |
| **2. GitHub Actions** | ⭐⭐ 简单 | ⭐⭐⭐⭐⭐ | 低 | ⭐⭐⭐⭐ |
| **3. PR Template** | ⭐ 极简单 | ⭐⭐⭐⭐ | 无 | ⭐⭐⭐⭐ |
| **4. CODEOWNERS** | ⭐⭐⭐ 中等 | ⭐⭐⭐ | 中 | ⭐⭐⭐ |
| **5. CLI/API** | ⭐⭐⭐⭐ 复杂 | ⭐⭐⭐⭐⭐ | 高 | ⭐⭐ |

---

## 🎯 推荐组合

**最佳实践：方案 1 + 方案 2 + 方案 3**

1. ✅ **启用 PR Summaries**（设置一次就好）
2. ✅ **部署 GitHub Actions workflow**（自动化触发）
3. ✅ **使用 PR Template**（确保覆盖率）

这样可以确保：
- 所有 PR 都自动获得 Copilot 摘要
- 自动触发详细的代码审查
- 即使自动化失败，模板也能作为后备方案

---

## 🚀 立即开始

推送已配置的文件到 GitHub：

```bash
# 提交所有配置文件
git add .github/
git commit -m "Configure auto Copilot review with Actions and PR template"
git push origin main

# 创建测试 PR
git checkout -b test/auto-review
echo "# Test auto review" >> test.md
git add test.md
git commit -m "Test auto Copilot review"
git push origin test/auto-review

# 在 GitHub 上创建 PR，观察自动审查效果
```

然后访问 GitHub 设置页面启用 **Copilot Pull Request Summaries**！
