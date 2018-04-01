import requests
from bs4 import BeautifulSoup

#Website containing medicine details

def get_details(medicine_name):
    url = "https://www.drugs.com/" + medicine_name + ".html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find_all("p")

    temp = [] #List for storing text values from html
    i = 0
    for text in data:
        temp.append(text.get_text())
        
        if i>=1 and i<5:
            print(temp[i])
        i+=1
