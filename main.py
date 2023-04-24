import requests
from bs4 import BeautifulSoup

# first step to automate downloading the list
""" 
date = input("DATE (YYYY-MM-DD): ")

list_type = ""

print("1. Miscellaneous")
print("2. Miscellaneous Supplementary")
print("3. Regular")
print("4. Regular Supplementary")

option = int(input("Select one option: "))

if option == 1:
    list_type = "M_J_1"

elif option == 2:
    list_type = "M_J_2"

elif option == 3:
    list_type = "F_J_1"

elif option == 4:
    list_type = "F_J_2" """

# Set the URL of the website to scrape
url = 'https://main.sci.gov.in/causelist'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page with Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

def filter_links(href):
    if href and ('M_J_1.pdf' in href or 'M_J_2.pdf' in href or 'F_J_1.pdf' in href or 'F_J_2.pdf' in href):
        return True
        
    else:
        return False
    

links = soup.findAll('a', href=filter_links)

x = [link["href"] for link in links]

for i in x:
    if i[0] == ".":
        pass
    else:
        print(i) #Prints the url of the list


 # Work need to be done below here  


pdf_url = f"https://main.sci.gov.in/jonew/cl/{date}/{list_type}.pdf"

r = requests.get(pdf_url, stream = True)

with open("list.pdf", 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
