import requests
from bs4 import BeautifulSoup
import csv
import calendar
import datetime
import time
import os.path

def form_table(tableProcess, dayFile):
    """
    table : for table one should be table[1]
    """
    header_csv = None
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


    smallVai.insert(0, 'date')

    header_csv = smallVai


    #tabelinhaFinal.append(smallVai)


    smallVai = []
    smallVai.append(firstPtable[1][0])
    smallVai.append('0'), smallVai.append('0'), smallVai.append('0')
    smallVai.append(firstPtable[2][0].split(':')[1])
    smallVai.append(firstPtable[2][1].split(':')[1])

    smallVai.insert(0, dayFile)

    tabelinhaFinal.append(smallVai)

    for linha in finalTable:
        linha.insert(0, dayFile)
        tabelinhaFinal.append(linha)


    return tabelinhaFinal, header_csv

def write_table2File(list_info, header_file, path_file):

    fileEmpty = os.stat(path_file).st_size == 0

    if fileEmpty:
        with open(path_file, "a+") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header_file)
    
    with open(path_file, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(list_info)



#Criar todas as datas para o mês de janeiro.
year = 2020
month = 3
JanMonth = calendar.monthcalendar(2020, 3)

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
                        src = result.content
                        soup = BeautifulSoup(src, 'lxml')
                        table = soup.find_all('table')
                        
                        if len(table) > 0:
                            
                            namePath1 = './csv-files/arq1.csv'
                            namePath2 = './csv-files/arq2.csv'

                            tableOne = table[1]
                            tableTwo = table[3]
                            dayName = str(year) + str(month).rjust(2, '0') + str(dateIs).rjust(2,'0')
                            vejaTabela, header_arq = form_table(tableOne, dayName)
                            write_table2File(vejaTabela, header_arq, namePath1)

                            vejaTabela, header_arq = form_table(tableTwo, dayName)
                            write_table2File(vejaTabela, header_arq, namePath2)

                    time.sleep(1)
                
                
                
                
                    
                    

            #print('Dia da semana: ', dateIs, dayOfWeek)

