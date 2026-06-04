# GitHub 上传指南

## 第一部分：下载并安装 Git

### 方法1：官方网站下载（推荐）

1. 访问 Git 官网：https://git-scm.com/download/win
2. 下载 Windows 版本
3. 运行安装程序，全部使用默认设置即可
4. 安装完成后，重新打开命令提示符

### 方法2：使用包管理器

如果你有 winget 或 chocolatey：

```bash
# 使用 winget
winget install Git.Git

# 或使用 chocolatey
choco install git
```

## 第二部分：配置 Git（只需配置一次）

打开命令提示符，输入：

```bash
# 设置你的用户名（替换成你的GitHub用户名）
git config --global user.name "你的GitHub用户名"

# 设置你的邮箱（替换成你的GitHub邮箱）
git config --global user.email "你的GitHub邮箱"
```

## 第三部分：创建 GitHub 仓库

1. 打开 GitHub 网站：https://github.com
2. 登录你的账号
3. 点击右上角的 "+" → "New repository"
4. 填写信息：
   - Repository name: `pdf-merger`
   - Description: `PDF合并工具`
   - 选择 "Public"（公开）或 "Private"（私有）
   - **不要勾选** "Initialize this repository with a README"
5. 点击 "Create repository"
6. **重要**：复制页面上的仓库地址，类似于：
   ```
   https://github.com/你的用户名/pdf-merger.git
   ```

## 第四部分：上传代码到 GitHub

### 步骤1：打开命令提示符

按 `Win + R`，输入 `cmd`，回车

### 步骤2：进入项目目录

```bash
cd "E:\大厂冲冲冲\北森题库+答案解析\.trae\skills\pdf-merger"
```

### 步骤3：初始化 Git 仓库

```bash
git init
```

### 步骤4：添加所有文件

```bash
git add .
```

### 步骤5：提交代码

```bash
git commit -m "Initial commit: PDF合并工具"
```

### 步骤6：添加远程仓库地址

将下面的 `你的用户名` 替换成你的GitHub用户名：

```bash
git remote add origin https://github.com/你的用户名/pdf-merger.git
```

### 步骤7：上传到 GitHub

```bash
git push -u origin master
```

如果提示要输入用户名和密码，输入你的GitHub用户名和密码（或访问令牌）。

## 第五部分：验证上传成功

1. 打开你的 GitHub 仓库页面
2. 刷新页面，应该能看到所有文件

## 常见问题

### Q: git push 时提示权限错误？
A: 
1. 如果你开启了双重验证，需要使用 Personal Access Token
2. 在 GitHub 上：Settings → Developer settings → Personal access tokens → Generate new token
3. 创建时勾选 "repo" 权限
4. 使用这个 token 代替密码

### Q: 提示 "fatal: remote origin already exists"？
A: 
```bash
git remote set-url origin https://github.com/你的用户名/pdf-merger.git
```

### Q: 如何更新代码？
A: 
```bash
git add .
git commit -m "更新说明"
git push
```

## 快速模板

复制以下命令，按顺序执行（记得替换用户名）：

```bash
cd "E:\大厂冲冲冲\北森题库+答案解析\.trae\skills\pdf-merger"
git init
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/你的用户名/pdf-merger.git
git push -u origin master
```

---

有问题随时问我！
