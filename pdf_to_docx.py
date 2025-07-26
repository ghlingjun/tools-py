# 导入pdf2docx模块
from pdf2docx import Converter


def pdf2word(file_path):
    # 截取文件名称
    file_name = file_path.split('.')[0]

    # 转换后的文件名称
    doc_file = f'{file_name}.docx'

    # 创建Converter对象
    p2w = Converter(file_path)

    # 执行转换方法，start开始页，0从第一页开始，end结束页，None为无限制
    p2w.convert(doc_file, start=0, end=None)
    p2w.close()

    return doc_file


pdf2word(r"data/temp.pdf")
