# PDF Merger Tool

一个简单易用的PDF合并工具，支持按模式匹配和排序。

## 功能特点

- 支持按文件名模式匹配PDF文件
- 自动按文件名排序
- 支持指定输出目录
- 命令行参数简单易用
- 跨平台支持（Windows、Mac、Linux）

## 安装依赖

```bash
pip install pypdf
```

## 使用方法

### 基本用法

```bash
# 合并当前目录下所有PDF
python skill.py -o merged.pdf

# 合并指定模式的PDF
python skill.py -p "*.pdf" -o merged.pdf
```

### 参数说明

- `-d, --directory`: PDF文件所在目录（默认为当前目录）
- `-o, --output`: 输出的PDF文件名（必填）
- `-p, --pattern`: 文件名匹配模式（默认为 "*.pdf"）
- `-s, --sort`: 按文件名排序（默认为True）
- `--no-sort`: 不排序

### 使用示例

```bash
# 示例1：合并当前目录所有PDF
python skill.py -o all_pdfs.pdf

# 示例2：合并特定模式的文件
python skill.py -p "北森套题*.pdf" -o 北森套题合集.pdf

# 示例3：指定目录
python skill.py -d "D:\文档" -p "*.pdf" -o merged.pdf

# 示例4：不排序
python skill.py -p "*.pdf" -o merged.pdf --no-sort
```

## 在Trae IDE中使用

如果你使用Trae IDE，可以直接调用skill：

1. 在Trae IDE中打开
2. 告诉AI："请使用 pdf-merger skill 帮我合并PDF"
3. 说明你的需求

## 项目结构

```
pdf-merger/
├── SKILL.md      # Skill配置文件
├── skill.py      # 主程序
└── README.md     # 说明文档
```

## 技术栈

- Python 3.6+
- pypdf 库

## 许可证

MIT License

## 问题反馈

如果你遇到任何问题或有建议，请提交Issue。
