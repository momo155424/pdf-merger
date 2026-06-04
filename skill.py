import os
import glob
import argparse
from pypdf import PdfWriter

def merge_pdfs(directory, output, pattern="*.pdf", sort=True):
    """
    合并多个PDF文件
    
    Args:
        directory: PDF文件所在目录
        output: 输出的PDF文件名
        pattern: 文件名匹配模式
        sort: 是否按文件名排序
    """
    if not directory:
        directory = os.getcwd()
    
    # 构建完整路径
    if not os.path.isabs(directory):
        directory = os.path.abspath(directory)
    
    if not os.path.isabs(output):
        output = os.path.join(directory, output)
    
    # 查找PDF文件
    pdf_pattern = os.path.join(directory, pattern)
    pdf_files = glob.glob(pdf_pattern)
    
    if not pdf_files:
        print(f"在 {directory} 目录下未找到匹配 {pattern} 的PDF文件")
        return False
    
    # 排序
    if sort:
        pdf_files.sort()
    
    print(f"找到 {len(pdf_files)} 个PDF文件")
    for pdf in pdf_files:
        print(f"  - {os.path.basename(pdf)}")
    
    # 合并PDF
    pdf_writer = PdfWriter()
    for pdf_path in pdf_files:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_writer.append(pdf_file)
    
    with open(output, 'wb') as output_file:
        pdf_writer.write(output_file)
    
    print(f"\n合并完成！输出文件: {output}")
    return True

def main():
    parser = argparse.ArgumentParser(description="合并多个PDF文件")
    parser.add_argument("-d", "--directory", default="", help="PDF文件所在目录")
    parser.add_argument("-o", "--output", required=True, help="输出的PDF文件名")
    parser.add_argument("-p", "--pattern", default="*.pdf", help="文件名匹配模式")
    parser.add_argument("-s", "--sort", action="store_true", default=True, help="按文件名排序")
    parser.add_argument("--no-sort", action="store_false", dest="sort", help="不排序")
    
    args = parser.parse_args()
    
    merge_pdfs(args.directory, args.output, args.pattern, args.sort)

if __name__ == "__main__":
    main()
