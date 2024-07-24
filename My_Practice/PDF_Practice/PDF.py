import PyPDF2

with open("dummy.pdf",mode="rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)