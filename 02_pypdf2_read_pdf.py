from PyPDF2 import PdfReader

reader = PdfReader("sample.pdf")

for page in reader.pages:
    print(page.extract_text())
