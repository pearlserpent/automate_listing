from PyPDF2 import PdfReader, DocumentInformation

reader = PdfReader("list.pdf")

print(reader.getDocumentInfo())