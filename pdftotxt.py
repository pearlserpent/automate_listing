from pypdf import PdfReader


# Converting list from pdf to txt

reader = PdfReader("F_J_1.pdf")
number_of_pages = len(reader.pages)


with open("regular.txt", 'w') as f:
    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        f.writelines(text)
