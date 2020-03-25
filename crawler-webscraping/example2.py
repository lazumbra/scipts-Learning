import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

#Suppose you want to get only the html
#But know that you can also get the text of the URL
urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    pass
    #print('olha a tag: ', a_tag)
    #print('\n')

#I get all the url and append to urls
for h2_tag in soup.find_all('h2'):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

print(urls)