import json
from os import listdir
from os.path import isfile, join
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as dates

def save_graph(win_hours, win_all_contracts, name_file2save):
    plt.plot_date(win_hours, win_all_contracts)
    plt.xticks(rotation=85)
    plt.savefig(name_file2save, bbox_inches='tight')
    plt.clf()

def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()

def add_min_in_time(current_str_time, minutes):
    new_time = datetime.datetime.strptime(current_str_time, '%H:%M:%S')
    seconds = minutes * 60
    new_time = addSecs(new_time, seconds)
    return new_time

def add_information_hash(broker_name, symbol, value, dic_original, dia, hora):
    #hum = {'CM Capital': {'WING20': [70], 'WDO20': []}}
    ini_sym = symbol[:3]
    complete_symbol = symbol
    mes = symbol[3:]
    val = 10
    # {'01/09': [{'CM Capital': {'WING20': [70], 'WDO20': []}}]}
    tem_broker = False
    #print('dic_information', [*dic_information])#[*dic_information])
    broker = broker_name
    symbol = 'WING20'
    win_e = 'WIN'+ mes
    wdo_e = 'WDO' + mes

    tupla_add = (hora, value)
    #print("tupla ", tupla_add[0])

    #dic_symbol = {win_e: [],wdo_e: []}
    if ini_sym ==  'WIN':
        dic_symbol = {win_e: []}
    else:
        dic_symbol = {wdo_e: []}

    dic_sym2 = {}
    #print('mes mes:', ini_sym)
    if  ini_sym == 'WIN':
        dic_sym2

    dic_final = {}

    if ini_sym == 'WIN':
        #print('VALOR, value', value)
        #dic_symbol[win_e].append(value)
        pass
    else:
        #dic_symbol[wdo_e].append(value)]
        pass
    
    dic_final[broker] = dic_symbol
    #print('dic_final', dic_final)
    #print('DIC FINA FINA: ', dic_final)
    #lista_vazia = []
    #lista_vazia.append(dic_final)
    #dic_original[dia] = dic_final

    #value = (hora, valor_objetivo)

    if dia not in dic_original:
        dic_original[dia] = dic_final
        dic_original[dia][broker_name][complete_symbol].append( tupla_add )
        #print(dic_original[dia], broker_name)
        #print("dia nao existe la")
    else:
        #se ja tem dia
        #ver se ja tem o broker name. Se nao tiver, adicionar o broker name
        if broker_name not in dic_original[dia]:
            
            dic_original[dia][broker_name] = dic_final[broker_name]
            dic_original[dia][broker_name][complete_symbol].append( tupla_add )
        #se já tem o broker name. olhar se ja tem o simbol
        else:
            #nesse if eu sempre to colocando valor pela segunda vez.
            if complete_symbol in dic_original[dia][broker_name]:
                last_hour_added = dic_original[dia][broker_name][complete_symbol][-1][0]
                new_time = add_min_in_time(last_hour_added, 15)

                if tupla_add[0] > str(new_time):
                    #print('\n')
                    #print('hora adicionar',tupla_add[0], 'ultima hora', last_hour_added)
                    #print('anterior: ', dic_original)
                    #dic_original[dia][broker_name] = dic_final[broker_name]
                    dic_original[dia][broker_name][complete_symbol].append( tupla_add )
                    #print('posterior: ', dic_original)


                #dic_original[dia][broker_name][complete_symbol].append( tupla_add )

                #print( 'aqui eu pego a tupla', dic_original[dia][broker_name][complete_symbol][0][0] )
            #broker e diferente
            else:
                #ADICIONO VALOR
                #print('KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', complete_symbol, 'arquivo original',dic_original[dia])
                #print('fina', dic_final[broker_name], dic_original[dia])
                #print('ORIGINAL', dic_original)
                dic_original[dia][broker_name][complete_symbol] = dic_final[broker_name][complete_symbol]
                dic_original[dia][broker_name][complete_symbol].append( tupla_add )
                #print('ADICIONO', dic_original)
                #print('ADICIONO90', dic_original[dia][broker_name][complete_symbol])
                #exit()
                #dic_original[dia][broker_name] = dic_final[broker_name]
                #dic_original[dia][broker_name][complete_symbol].append( tupla_add )
                #dic_original[dia][broker_name][complete_symbol] Usar para append valor em qualquer lugar
                #print('OOOOOOOPPPPPPPPPPPP', dic_original[dia][broker_name][complete_symbol])
                
            #value aqui vai ser hora e valor
            #   dic_original[dia][broker_name][complete_symbol].append(value)
            #print('dic_original[dia][broker_name]::OOOOOOOOOOOOOO', complete_symbol in dic_original[dia][broker_name], dic_original[dia][broker_name])

                #dic_original[dia][broker_name][complete_symbol]

        #print("dia ja existe")


    ##Criar funcao para isso
    #print('HHHHHHHHHHHHHH',dic_final[broker][complete_symbol][0])

    '''
    resultado = dic_final[broker][complete_symbol][0]
    if dia in dic_original:
        #VER SE É O MESMO BROKER
        if [* dic_original[dia][0] ][0] == broker:
            for valor in dic_original[dia]:
                if broker in valor:
                    valor[broker][complete_symbol].append(value)
                    tem_broker = True
                    break
                dic_original[dia].append(dic_final)
        else:
            dic_original[dia].append(dic_final)
    else:
        #primeira inicialização quando nao acha o dia
        lista_vazia = []
        lista_vazia.append(dic_final)
        dic_original[dia] = lista_vazia
    '''

def free_information():
    dia_arq = None
    broker_name_arq = None
    symbol_arq = None
    value_arq = None
    hour_arq = None
    return dia_arq, broker_name_arq, symbol_arq, value_arq, hour_arq

def new_add_information_hash(broker_name, symbol, value, dic_original, dia):
    #hum = {'CM Capital': {'WING20': [70], 'WDO20': []}}
    ini_sym = symbol[:3]
    complete_symbol = symbol
    mes = symbol[3:]
    val = 10
    # {'01/09': [{'CM Capital': {'WING20': [70], 'WDO20': []}}]}
    tem_broker = False
    #print('dic_information', [*dic_information])#[*dic_information])
    broker = broker_name
    symbol = 'WING20'
    win_e = 'WIN'+ mes
    wdo_e = 'WDO' + mes

    dic_symbol = {win_e: [],wdo_e: []}
    dic_final = {}

    if ini_sym == 'WIN':
        #print('VALOR, value', value)
        dic_symbol[win_e].append(value)
    else:
        dic_symbol[wdo_e].append(value)
    
    dic_final[broker] = dic_symbol
    #print('DIC FINA FINA: ', dic_final)

    ##Criar funcao para isso
    #print('HHHHHHHHHHHHHH',dic_final[broker][complete_symbol][0])

    
    resultado = dic_final[broker][complete_symbol][0]
    if dia in dic_original:
        #VER SE É O MESMO BROKER
        if [* dic_original[dia][0] ][0] == broker:
            for valor in dic_original[dia]:
                if broker in valor:
                    valor[broker][complete_symbol].append(value)
                    tem_broker = True
                    break
                dic_original[dia].append(dic_final)
        else:
            dic_original[dia].append(dic_final)
    else:
        #primeira inicialização quando nao acha o dia
        lista_vazia = []
        lista_vazia.append(dic_final)
        dic_original[dia] = lista_vazia
    

rapum = {}
dia1 = '01/09'

dia2 = '02/09'

dia3 = '03/09'

dia4 = '04/09'
papapa = {'CM Capital': {'WING20': [70], 'WDO20': []}}
oraora = {'Orama': {'WING20': [70], 'WDO20': []}}


broker_name1 = 'Orama'
broker_name2 = 'Oram2a'
symbol1 = 'WING20'
symbol2 = 'WDOG20'
value1 = 30
value2 = 20
'''
add_information_hash(broker_name1, symbol1, value1, rapum, dia1)
add_information_hash(broker_name2, symbol1, value1, rapum, dia1)
add_information_hash(broker_name2, symbol1, value2, rapum, dia1)
add_information_hash(broker_name2, symbol1, value2, rapum, dia2)
add_information_hash(broker_name1, symbol1, value2, rapum, dia2)
add_information_hash(broker_name1, symbol2, value2, rapum, dia2)
'''
#print("começou aqui")
print("RAPUM 1: ", rapum)
'''
print("\n")
print("começou aqui")
print("RAPUM: ", rapum)
add_information_hash(papapa, rapum, dia1)
print("RAPUM logo apos: ", rapum)
print("\n")
add_information_hash(oraora, rapum, dia1)
print("RAPUM: ", rapum)
add_information_hash(oraora, rapum, dia2)
print("RAPUM: ", rapum)
add_information_hash(papapa, rapum, dia2)
#print("RAPUM: ", rapum)
'''


#print("\n")
#print("começou NOVO aqui")
rapum2 = {}
broker_name1 = 'Orama'
broker_name2 = 'Oram2a'
symbol1 = 'WING20'
value1 = 30
new_add_information_hash(broker_name1, symbol1, value1, rapum2, dia1)
new_add_information_hash(broker_name1, symbol1, value1, rapum2, dia1)
#print('ENTRADO AQUI')
new_add_information_hash(broker_name2, symbol1, value1, rapum2, dia1)
new_add_information_hash(broker_name2, symbol1, value1, rapum2, dia2)
#print("\n")
#print("\n")
#print("RAPUM: ", rapum2)

'''
print("RAPUM: ", rapum)
add_information_hash(hum2, rapum, dia2)
print("RAPUM: ", rapum['02/09'])
add_information_hash(hum, rapum, dia2)
print("RAPUM: ", rapum)
'''




#FaZR A PARTIR DAQUI
input_logs = '/home/jefferson/Downloads/conjunto_sessions/'
files_input = '/home/jefferson/Downloads/conjunto_sessions'
onlyfiles = [f for f in listdir(files_input) if isfile(join(files_input, f))]

#Começa aqui
'''
dia_arq = None
broker_name_arq = None
symbol_arq = None
value_arq = None
hour_arq = None

hour_min_arq = None
'''
rapum3 = {}
for i in range(len(onlyfiles)):
    num_lines = sum(1 for line in open(input_logs + onlyfiles[i]))

    with open(input_logs + onlyfiles[i], 'r') as fp:
        for line in fp.readlines():
            l = line.find('{')
            json_line = line[l : ].strip()

            if l == -1:
                print('invalid line: ' + line.strip())
                continue
            
            info = json.loads(json_line)

            if info['op'] == 'list_strategies':
                for strategy in info['strategies']:
                    dia_arq, broker_name_arq, symbol_arq, value_arq, hour_arq = free_information()
                    #print('broker_name_arq: ', broker_name_arq)
                    broker_name_arq = strategy['broker_name']
                    #print('broker_name: ' + strategy['broker_name'])

            if info['op'] == 'refresh_book':
                symbol_arq = info['symbol']

            if info['op'] == 'refresh_profit':
                hour_arq = info['last_time'][9:17]
                dia_arq = info['last_time'][:8]
                value_arq = info['sell_orders']
                hour_min_arq = info['last_time'][9:17]
                #print('veja o refresh profit: ', info['last_time'][9:17])
                if(broker_name_arq == None or  symbol_arq == None or dia_arq ==  None):
                    #print('erro')
                    a = 1

                else:
                    #print(broker_name_arq, 'broker_name_arq')
                    #print(symbol_arq)
                    #print('value_arq', value_arq)
                    add_information_hash(broker_name_arq, symbol_arq, info['buy_contracts'], rapum3, dia_arq, hour_min_arq)
print(rapum3)
print('cara')
print('\n\n')
hours_fin = []
value_fin = []

for ano, compl in rapum3.items():

    print(ano)
    #print(type(v))
    for broker, compl2 in compl.items():
        print(broker)
        #print('compl2',compl2)
        for symbol, valores in compl2.items():
            print(symbol)
            #print(len(valores))
            for i in range(len(valores)):
                print(valores[i])
                hours_fin.append(valores[i][0])
                value_fin.append(valores[i][1])
            #print('hours_fin: ',hours_fin)
            #print('value_fin: ',value_fin)
            print("##################################")
            
            
            file_arquivo = ano + '_' + broker+ '_' + symbol + '.png'
            if ano != '':
                save_graph(hours_fin, value_fin, file_arquivo)
                hours_fin = []
                value_fin = []
            else:
                hours_fin = []
                value_fin = []
        #print("apenas um")
    #print('hours_fin: ', len(hours_fin))
    #print(value_fin)
    #print('value_fin: ', len(value_fin))





            
#save_graph(win_hours, win_all_contracts, name_file2save)


