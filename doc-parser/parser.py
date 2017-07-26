# encoding=utf-8
from docx import Document

PATH = 'data/说明书.docx'


def read_document():
    return Document(PATH)


def parse_block():
    document = read_document()
    for i, para in enumerate(document.paragraphs):
        print(para.text)


if __name__ == '__main__':
    parse_block()
