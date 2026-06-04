---
name: "pdf-merger"
description: "合并多个PDF文件为单个PDF，支持按模式匹配和排序。Invoke when user asks to merge multiple PDFs into one file."
---

# PDF Merger

这个skill用于合并多个PDF文件为单个PDF文件。

## 使用方式

### 参数说明

- `directory`: PDF文件所在目录（可选，默认为当前目录）
- `output`: 输出的PDF文件名
- `pattern`: 文件名匹配模式（可选，例如"*.pdf"或"北森套题*.pdf"）
- `sort`: 是否按文件名排序（默认为true）

### 示例

1. 合并当前目录所有PDF文件：
   ```
   使用pdf-merger合并PDF，输出为merged.pdf
   ```

2. 合并特定模式的PDF：
   ```
   使用pdf-merger合并，pattern="北森套题*.pdf"，output="北森套题合集.pdf"
   ```

3. 指定目录：
   ```
   使用pdf-merger合并指定目录下的PDF，directory="E:/path/to/pdfs"，output="merged.pdf"
   ```
