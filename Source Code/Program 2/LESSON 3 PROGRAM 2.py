import requests
from bs4 import BeautifulSoup

html = requests.get("https://en.wikipedia.org/wiki/Deep_learning") #URL for web scraping

bsObj=BeautifulSoup(html.content,"html.parser") #

print(bsObj.title.string)
file = open('links.txt','w')
for link in bsObj.find_all('a'): # search links in html
    formattedLink=(str(link.get('href')) + '\n\n')
    if '/' in formattedLink:
        if '/wiki/' in formattedLink:
            file.write("https://en.wikipedia.org/" + formattedLink) #write the links into a text file
        else:
            file.write(formattedLink)

file.close()
