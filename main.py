import requests
from bs4 import BeautifulSoup

# first step to automate downloading the list


# Set the URL of the website to scrape
url = 'https://main.sci.gov.in/causelist'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page with Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the link containing 'M_J_1.pdf'
link = soup.find('a', href=lambda href: href and 'M_J_1.pdf' in href)

# Extract the URL of the link
pdf_url = link['href']

# To be modified here

r = requests.get(pdf_url, stream = True)

with open("list.pdf", 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)


