from borb.pdf import Document

with open("list.pdf", "rb") as f:
    pdf = Document.from_bytes(f.read())

for page in pdf.pages:
    print(page.get_text())