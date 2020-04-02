import csv
from datetime import date
from configparser import ConfigParser


def get_days(file_path):
    '''
    Descrição:
      Função retorna todos os dias que já foram processados
      Essa função nem é necessária *

    Utilização:
      funcao(param1, param2)

    Parâmetros:
      param1
        Um texto qualquer
      param2
        Outro texto qualquer
  '''

    row_in_list = []
    with open(file_path, 'r') as f:
        data = csv.reader(f)
        for raw in data:
            row_in_list.append(raw[0])
    
    return row_in_list


def get_days_range(last_active_day, current_day):
    if current_day < last_active_day:
        range_one = list(range(last_active_day+1, 32))
        range_two = list(range(1, current_day))
        joinedlist = range_one + range_two
    else:
        joinedlist =  list(range(last_active_day+1, current_day))

    return joinedlist

def save_current_vld_date(config_ini, current_vld_date, input_file):

  config_ini.set('main', 'valid_date', current_vld_date)

  with open(input_file, 'w') as f:
    config.write(f)


config = ConfigParser()
config.read('config.ini')



save_current_vld_date(config, '21', 'config.ini')
who_is = config.get('main', 'valid_date')
print('who is: ', who_is)


data = None
rowlio = []
filePath = '/home/jefferson/Beyond_workspace/crawler-b3/csv-files/table1.csv'

rowlio = get_days(filePath)

mes = [20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31]
dia_atual = 20
today_day = str(date.today())[8:]
today_day = int(today_day)
year = str(date.today())[:4]
month = str(date.today())[5:7]



new_lista = get_days_range(25, 27)
print('new_lista: ', new_lista)




for day_It in mes:
    if day_It != 0 and day_It <= today_day:
        firstPartStr = "http://bvmf.bmfbovespa.com.br/market-data/html/md_stats_" + str(year) + str(month).rjust(2, '0') + str(day_It).rjust(2,'0') + ".html"
        print('hah: ', firstPartStr)



print('today: ', year, month, today_day)
            
print('20200228' in rowlio)

    




    

