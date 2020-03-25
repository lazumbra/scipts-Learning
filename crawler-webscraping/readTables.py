import requests
from bs4 import BeautifulSoup

result = requests.get("http://bvmf.bmfbovespa.com.br/market-data/html/md_stats_20200320.html")
src = result.content
soup = BeautifulSoup(src, 'lxml')

data = []

table = soup.find_all('table')

for tbs in table:
    for rows in tbs.find_all('tr'):
        print('rows normal:', rows)
        print('rows texto: ', rows.text)
        for man in rows.find_all('td'):
            print(man.text.strip())

    #print(tbs)
    #print('\n')


