import json
from os import listdir
from os.path import isfile, join
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import configparser
from statistics import mean

from shutil import copyfile
import os


input_logs = '/home/jefferson/Documents/test_files/13-02-2020/conjunto_sessions/'  
files_input = '/home/jefferson/Documents/test_files/13-02-2020/conjunto_sessions'

novo_local = '/home/jefferson/Documents/test_files/13-02-2020/new_folder'


onlyfiles = [f for f in listdir(files_input) if isfile(join(files_input, f))]

numero = 0

for i in range(len(onlyfiles)):
    day = None
    month = None
    symbol = None 
    num_lines = sum(1 for line in open(input_logs + onlyfiles[i]))
    #print("file: ", onlyfiles[i])
    with open(input_logs + onlyfiles[i], 'r') as fp:
        for line in fp.readlines():

            l = line.find('{')
            json_line = line[l : ].strip()

            if l == -1:
                #print('invalid line: ' + line.strip())
                continue
            
            info = json.loads(json_line)

            if info['op'] == 'refresh_profit':
                time = info['last_time'][:8]
                month = info['last_time'][4:6]
                day = info['last_time'][6:8]
                #print('time:', time, month, day)

               
            if info['op'] == 'refresh_book':
                symbol = info['symbol'][:4]
                #print('simbolo: ', symbol)
            
            if day != None and symbol != None:
                if symbol[:3] == 'WDO':
                    if month == '12' and day < '31' and symbol == 'WDOF':
                        if month == '12' and day == '10':
                            numero+=1
                            print('cima', onlyfiles[i])
                        #print('WDOF')
                        #copyfile(input_logs + onlyfiles[i], os.path.join(novo_local, onlyfiles[i]))
                        break
                    elif month == '01' and day < '30' and symbol == 'WDOG':
                        if month == '12' and day == '10':
                            numero+=1
                            print('baixo')                            
                        #print('WDOG')
                        #copyfile(input_logs + onlyfiles[i], os.path.join(novo_local, onlyfiles[i]))
                        break
                else:
                    if month == '12' and day < '18' and symbol == 'WINZ':
                        numero+=1
                        #print('WINZ')
                        #copyfile(input_logs + onlyfiles[i], os.path.join(novo_local, onlyfiles[i]))
                        break
                    elif (month == '12' and day > '17' and symbol == 'WING') or (month == '01' and day < '30' and symbol == 'WING'):
                        #print('arquivo para copiar')
                        numero+=1
                        #copyfile(input_logs + onlyfiles[i], os.path.join(novo_local, onlyfiles[i]))
                        break

print('num: ', numero)
                    


            

