# Copilot Auto Review - 配置指南

本 workflow 支持在 PR 和 Main 分支提交时自动触发 GitHub Copilot 代码审查。

## 📋 快速配置

### 1. 基础配置（已完成）

文件已创建在正确位置：
- ✅ `.github/workflows/copilot-review.yml` - 主 workflow 文件
- ✅ `.github/copilot-review-config.conf` - 详细配置说明

### 2. 触发条件

#### 自动触发：

**PR 触发**
- 新 PR 创建时 (`opened`)
- PR 有新提交时 (`synchronize`)
- PR 重新打开时 (`reopened`)
- 目标分支：`main`, `master`, `develop`

**Main 分支触发**
- 直接推送到 `main` 或 `master` 分支时
- 合并 PR 到 main 分支时

**手动触发**
- GitHub 网站：Actions → Copilot Auto Review → Run workflow
- 可选择审查范围和目标分支

### 3. 可配置项

在 `.github/workflows/copilot-review.yml` 的 `env:` 部分修改：

```yaml
env:
  # 审查详细程度: basic | detailed | comprehensive
  REVIEW_DETAIL_LEVEL: 'detailed'
  
  # 功能开关
  ENABLE_SECURITY_CHECK: 'true'      # 安全检查
  ENABLE_PERFORMANCE_CHECK: 'true'   # 性能分析
  ENABLE_QUALITY_CHECK: 'true'       # 代码质量
  ENABLE_BEST_PRACTICES: 'true'      # 最佳实践
  
  # 文件过滤
  FILE_EXTENSIONS: '*.py,*.js,*.ts,*.java,*.go,*.rb'
  MIN_CHANGED_FILES: '0'             # 最小变更文件数
  
  # 附加功能
  ADD_REVIEW_LABEL: 'true'           # 添加标签
  CUSTOM_REVIEW_MESSAGE: ''          # 自定义消息
```

## 🎯 使用场景

### 场景 1: PR 代码审查
1. 创建功能分支
2. 提交代码
3. 创建 PR
4. **自动触发** - Workflow 自动在 PR 中添加 `@copilot` 审查请求
5. Copilot 回复审查结果

### 场景 2: Main 分支监控
1. PR 合并到 main
2. **自动触发** - Workflow 创建一个 issue
3. Issue 中包含 `@copilot` 审查请求
4. Copilot 审查此次 commit

### 场景 3: 手动触发
1. 进入 Actions 标签
2. 选择 "Copilot Auto Review" workflow
3. 点击 "Run workflow"
4. 选择审查范围和目标分支
5. 运行

## 🔧 自定义配置

### 修改审查重点

只关注安全问题：
```yaml
env:
  ENABLE_SECURITY_CHECK: 'true'
  ENABLE_PERFORMANCE_CHECK: 'false'
  ENABLE_QUALITY_CHECK: 'false'
  ENABLE_BEST_PRACTICES: 'false'
```

### 修改触发分支

添加更多分支：
```yaml
on:
  pull_request:
    branches:
      - main
      - master
      - develop
      - staging      # 添加新分支
      - release/*    # 支持通配符
```

### 修改文件类型过滤

只审查 Python 和 JavaScript：
```yaml
env:
  FILE_EXTENSIONS: '*.py,*.js'
```

### 添加自定义消息

```yaml
env:
  CUSTOM_REVIEW_MESSAGE: '请特别关注数据库查询的性能和安全性'
```

## 📊 工作流程

### PR 审查流程
```
PR 创建/更新
    ↓
检出代码
    ↓
获取变更文件
    ↓
检查是否需要审查（文件数量）
    ↓
构建审查消息
    ↓
添加标签（可选）
    ↓
发送 @copilot 评论到 PR
    ↓
等待 Copilot 响应
```

### Main 分支审查流程
```
Push 到 main
    ↓
检出代码
    ↓
获取 commit 信息
    ↓
获取变更文件
    ↓
创建审查 Issue
    ↓
在 Issue 中 @copilot
    ↓
等待 Copilot 响应
```

## 🏷️ 标签说明

Workflow 会自动添加以下标签（需要先在仓库中创建）：

- `copilot-review` - 所有 Copilot 审查
- `main-branch` - Main 分支的审查
- `automated` - 自动化创建的 issue
- `manual-trigger` - 手动触发的审查

创建标签：
1. 进入仓库 Issues 标签
2. 点击 "Labels"
3. 点击 "New label"
4. 创建上述标签

## 🚀 部署步骤

```bash
# 1. 提交配置文件
git add .github/
git commit -m "Add Copilot auto review workflow with configurable options"
git push origin main

# 2. 验证 workflow 已启用
# 访问: https://github.com/YOUR_USERNAME/ai-review-test/actions

# 3. 测试 PR 触发
git checkout -b test/workflow-trigger
echo "# Test file" > test.py
git add test.py
git commit -m "Test: trigger Copilot review"
git push origin test/workflow-trigger
# 在 GitHub 创建 PR

# 4. 测试 Main 分支触发
# 合并上述 PR，观察是否创建审查 issue

# 5. 测试手动触发
# GitHub → Actions → Copilot Auto Review → Run workflow
```

## 🔍 监控和调试

### 查看 Workflow 运行情况
1. 进入仓库 Actions 标签
2. 选择相应的 workflow 运行
3. 查看日志输出

### 常见问题

**Q: Copilot 没有响应**
- 确保 GitHub Copilot 订阅已激活
- 检查 `@copilot` 是否正确输入
- 可能需要等待几分钟

**Q: Workflow 没有触发**
- 检查分支名是否匹配
- 检查 workflow 文件语法
- 查看 Actions 标签是否有错误

**Q: 无法添加评论或创建 issue**
- 检查 `permissions` 配置
- 确保 `GITHUB_TOKEN` 有足够权限

**Q: 过滤规则不生效**
- 检查文件扩展名格式
- 查看 workflow 日志中的变更文件列表

## 📚 进阶配置

### 使用 Repository Variables

将配置移到 GitHub UI 中：

1. Settings → Secrets and variables → Actions → Variables
2. 添加变量，例如：
   - `COPILOT_REVIEW_LEVEL` = `comprehensive`
   - `ENABLE_SECURITY_CHECK` = `true`

3. 在 workflow 中使用：
```yaml
env:
  REVIEW_DETAIL_LEVEL: ${{ vars.COPILOT_REVIEW_LEVEL }}
  ENABLE_SECURITY_CHECK: ${{ vars.ENABLE_SECURITY_CHECK }}
```

### 使用 Environments

为不同环境设置不同配置：

1. Settings → Environments → New environment
2. 创建 `production` 和 `development` 环境
3. 为每个环境设置不同的变量

### 添加通知

集成 Slack/Discord 通知：

```yaml
- name: Notify on review
  if: always()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

## 🎓 最佳实践

1. **渐进式启用** - 先在测试分支验证，再应用到主分支
2. **合理设置阈值** - 避免过于频繁的审查
3. **自定义消息** - 根据项目特点定制审查重点
4. **标签管理** - 使用标签分类和跟踪审查
5. **定期检查** - 查看审查历史，优化配置

---

更多信息请参考：
- [配置文件详解](.github/copilot-review-config.conf)
- [GitHub Actions 文档](https://docs.github.com/actions)
- [GitHub Copilot 文档](https://docs.github.com/copilot)
