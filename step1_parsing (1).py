from docx import Document
from PyPDF2 import PdfReader

def read_docx(path):
    doc = Document(path)
    for p in doc.paragraphs:
        print(p.text)

def read_pdf(path):
    reader = PdfReader(path)
    for page in reader.pages:
        print(page.extract_text())

# TEST
read_docx("sample.docx")
# read_pdf("sample.pdf")
