import requests
 
url = "https://www.hareandturtle.ai/"

response = requests.get(url)
 
from bs4 import BeautifulSoup
 
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify()) 

# Getting title 
print(soup.title.text)

# Getting headers
print(soup.header.text)