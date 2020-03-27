import requests
from bs4 import BeautifulSoup
import csv
import calendar
import datetime
import time

def form_table_1(tableProcess):
    """
    table : for table one should be table[1]
    """
    i = 0
    j = 0
    firstPtable = []
    finalTable = []
    for row in tableProcess.find_all('tr'):
        i += 1
        qunatiLinhas = len(row.find_all('td'))
        smallTable = []
        smallFirstT = []
        for linhas in row.find_all('td'):
            j+=1
            if i < 4:
                smallFirstT.append(linhas.text.strip())
                
            if(i >= 4):
                smallTable.append(linhas.text)
        j = 0
        if len(smallFirstT) > 0:
            firstPtable.append(smallFirstT)
        if len(smallTable) > 0:
            finalTable.append(smallTable)
    
    #Hora de formar a minha tabelinha final
    tabelinhaFinal = []
    smallVai = []
    smallVai.append(firstPtable[0][0])
    smallVai.append(firstPtable[0][1])
    smallVai.append(firstPtable[0][2])
    smallVai.append(firstPtable[0][3])
    smallVai.append(firstPtable[2][0].split(':')[0])
    smallVai.append(firstPtable[2][1].split(':')[0])

    tabelinhaFinal.append(smallVai)
    smallVai = []
    smallVai.append(firstPtable[1][0])
    smallVai.append('0'), smallVai.append('0'), smallVai.append('0')
    smallVai.append(firstPtable[2][0].split(':')[1])
    smallVai.append(firstPtable[2][1].split(':')[1])

    tabelinhaFinal.append(smallVai)

    for linha in finalTable:
        tabelinhaFinal.append(linha)


    return tabelinhaFinal

result = requests.get("http://bvmf.bmfbovespa.com.br/market-data/html/md_stats_20200320.html")
src = result.content
soup = BeautifulSoup(src, 'lxml')

data = []

#Here I find all the table
table = soup.find_all('table')

for tbs in table:
    for rows in tbs.find_all('tr'):
        print('rows normal:', rows)
        print('rows texto: ', rows.text)
        for man in rows.find_all('td'):
            print('que e man: ', type(man),'man is:', man)
            print('PANDEMIA', man.text.strip())
            if 'Number of Messages' in man.text.strip():
                print('TEM SIM PORRA')
                print(man.text.strip())
                #exit()

    #print(tbs)
    #print('\n')
print('\n')
print('começa a printar as tabelas')

if len(table) > 0:
    for tabela in table:
        print(tabela)
        print('\n')


if len(table) > 0:
    print('table 1\n')
    print(table[1])
    print('\n')
    #pd.read_html(table[1])


if len(table) > 0:
    primTabela = table[1]

    for row in primTabela.find_all('tr'):
        print('ROW: ', row.text)
        print('row sem texto: ', row)
        print('ENTRE NO FOR')
        qunatiLinhas = len(row.find_all('td'))
        print('quantidade de linhas é: ', qunatiLinhas)
        for linhas in row.find_all('td'):
            print('quantos tds')
            print('----->',linhas.text)
        print('SAIR DO FOR')
        print('FIM DE ROW SEM TEXTO')
        columns = row.find('td')

print('quantidade de tabelas')
print(len(table))

print('\n')
print('Começar novar etapa. Simbora que agora da certo')

#novo
if len(table) > 0:
    primTabela = table[1]
    i = 0
    j = 0
    firstPtable = []
    finalTable = []
    for row in primTabela.find_all('tr'):
        i += 1
        print('ENTRE NO FOR')
        qunatiLinhas = len(row.find_all('td'))
        print('valor de i: ', i)
        smallTable = []
        smallFirstT = []
        for linhas in row.find_all('td'):
            j+=1
            print('quantos tds', j)
            print('como ficaria: ', i -4, j-1)
            print('----->',linhas.text)
            if i < 4:
                smallFirstT.append(linhas.text.strip())
                
            if(i >= 4):
                smallTable.append(linhas.text)
        j = 0
        if len(smallFirstT) > 0:
            firstPtable.append(smallFirstT)
        if len(smallTable) > 0:
            finalTable.append(smallTable)
        print('SAIR DO FOR')
    
    print(len(finalTable))
    print(len(finalTable[0]))
    print(finalTable)

    for tabela in firstPtable:
        print(tabela)

    #Hora de formar a minha tabelinha final
    tabelinhaFinal = []
    smallVai = []
    smallVai.append(firstPtable[0][0])
    smallVai.append(firstPtable[0][1])
    smallVai.append(firstPtable[0][2])
    smallVai.append(firstPtable[0][3])
    smallVai.append(firstPtable[2][0].split(':')[0])
    smallVai.append(firstPtable[2][1].split(':')[0])

    tabelinhaFinal.append(smallVai)
    smallVai = []
    smallVai.append(firstPtable[1][0])
    smallVai.append('0'), smallVai.append('0'), smallVai.append('0')
    smallVai.append(firstPtable[2][0].split(':')[1])
    smallVai.append(firstPtable[2][1].split(':')[1])

    tabelinhaFinal.append(smallVai)

    for linha in finalTable:
        tabelinhaFinal.append(linha)

    print('\n')
    print('veja tudo')

    for linha in tabelinhaFinal:
        print(linha)
    print(type(tabelinhaFinal))

    with open('outut.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(tabelinhaFinal)
    


#Tabela 2
#novo
if len(table) > 0:
    primTabela = table[3]
    i = 0
    j = 0
    firstPtable = []
    finalTable = []
    for row in primTabela.find_all('tr'):
        i += 1
        print('ENTRE NO FOR')
        qunatiLinhas = len(row.find_all('td'))
        print('valor de i: ', i)
        smallTable = []
        smallFirstT = []
        for linhas in row.find_all('td'):
            j+=1
            print('quantos tds', j)
            print('como ficaria: ', i -4, j-1)
            print('----->',linhas.text)
            if i < 4:
                smallFirstT.append(linhas.text.strip())
                
            if(i >= 4):
                smallTable.append(linhas.text)
        j = 0
        if len(smallFirstT) > 0:
            firstPtable.append(smallFirstT)
        if len(smallTable) > 0:
            finalTable.append(smallTable)
        print('SAIR DO FOR')
    
    #veja se a segunda parte da tabela está correta
    tabelinhaFinal = []
    smallVai = []
    smallVai.append(firstPtable[0][0])
    smallVai.append(firstPtable[0][1])
    smallVai.append(firstPtable[0][2])
    smallVai.append(firstPtable[0][3])
    smallVai.append(firstPtable[2][0].split(':')[0])
    smallVai.append(firstPtable[2][1].split(':')[0])

    tabelinhaFinal.append(smallVai)
    smallVai = []
    smallVai.append(firstPtable[1][0])
    smallVai.append('0'), smallVai.append('0'), smallVai.append('0')
    smallVai.append(firstPtable[2][0].split(':')[1])
    smallVai.append(firstPtable[2][1].split(':')[1])

    tabelinhaFinal.append(smallVai)

    for linha in finalTable:
        tabelinhaFinal.append(linha)

    for linha in tabelinhaFinal:
        print(linha)    


result = requests.get("http://bvmf.bmfbovespa.com.br/market-data/html/md_stats_20200102.html")
src = result.content
print(src)
print(result.status_code)


#Criar todas as datas para o mês de janeiro.
year = 2020
month = 1
JanMonth = calendar.monthcalendar(2020, 1)

#loop over the month
for i in range(len(JanMonth)):
    for j in range(len(JanMonth[0])):
        if JanMonth[i][j] != 0:
            dateIs = JanMonth[i][j]
            dayWeek = datetime.datetime(year, month, dateIs)
            dayOfWeek = dayWeek.weekday()

            #Create String to get the html
            if dayOfWeek < 5:
                firstPartStr = "http://bvmf.bmfbovespa.com.br/market-data/html/md_stats_" + str(year) + str(month).rjust(2, '0') + str(dateIs).rjust(2,'0') + ".html"


                attemptives = 4
                result = None

                while attemptives > 0:
                    attemptives -= 1
                    result = requests.get(firstPartStr)
                    if result.status_code == 200:
                        attemptives = -1
                        print(firstPartStr, dayOfWeek)
                        src = result.content
                        soup = BeautifulSoup(src, 'lxml')
                        table = soup.find_all('table')
                        print(len(table))
                        
                        if len(table) > 0:
                            tableOne = table[1]
                            tableTwo = table[3]
                            vejaTabela = form_table_1(tableOne)
                            print('veja a tabela')
                            print(vejaTabela)
                            print('\nVeja a tabela 2')
                            vejaTabela = form_table_1(tableTwo)
                            print(vejaTabela)


                        print('Deu certo')
                    time.sleep(1)
                
                
                
                
                    
                    

            #print('Dia da semana: ', dateIs, dayOfWeek)

