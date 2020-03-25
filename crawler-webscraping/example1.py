import requests
from bs4 import BeautifulSoup

print('cheguei até aqui')

#open the webpage
result = requests.get("https://www.google.com/")
#check if the website is okay
#I should get 200 as answer
print(result.status_code)

# Check the header of the HTTP
#print(result.headers)

#Get the content of the html and store in a variable
src = result.content
#print(src)

#Once we have the page content is important to parse the page
#to a soup format so that we can get its information
#There are two ways to do it:
#soup = BeautifulSoup(src, "html.parser") or 
#soup = BeautifulSoup(src, "lxml")
#Check the difference between the two examples above
soup = BeautifulSoup(src, "lxml")
#print(soup)

#Now tyou can chech the elements of the page
#Check all links
#It atore all the links in an array
links = soup.find_all("a")
#print(links)
#print('\n')

#Search specific informaion in the link
#get the attribute information. Ex: href
for link in links:
    #print(link)
    if "Gmail" in link.text:
        print('Ao menos um: ',link)
        print('Atribute reference: ', link.attrs['href'])