import requests
from bs4 import BeautifulSoup

#Website containing medicine details
url = "https://www.drugs.com/lexapro.html"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
data = soup.find_all("p")

temp = [] #List for storing text values from html
for text in data:
    temp.append(text.get_text())
    
print(temp[1:4])
