import requests

# first step to automate downloading the list

pdf_url = "https://main.sci.gov.in/jonew/cl/2023-04-17/M_J_1.pdf"

r = requests.get(pdf_url, stream = True)

with open("lista.pdf", 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)