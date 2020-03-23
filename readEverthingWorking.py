import os
import datetime

def whenWednesday(day15):
    """
    day15 : int
        O day15 é qual dia da semana cai o dia 15. Lembrando que esse dia tem de ser de 0 a 6.
    return : int
        return o dia que é a quarta-feira.    
    """
    if day15 < 2:
        auxNum = day15 + 5
        return 15 - auxNum
    else:
        auxNum = day15 - 2
        return 15 - auxNum

def nextWednesday(day15):
    if day15 == 6:
        return 15 + 3
    elif day15 < 2:
        return (2 - day15) + 15
    elif day15 > 2 and day15 < 6:
        print('ta entrando aqui')
        return 15 - (day15 - 2)
    else:
        return 15


def ruleWdo(monthR, rulesWdo):

    return rulesWdo[monthR]

def ruleWin(dayR, yearR, monthR, rulesWin):
    """
    Preciso testar para os casos limites que são:
    1. Último mês e primeiro mês.
    Verificar mas eu acredito que eu não preciso usar o year
    """
    fifteenDay = datetime.datetime(int(yearR), int(monthR), 15)
    dayWeek15 = fifteenDay.weekday()
    nextRule = nextWednesday(dayWeek15)

    if int(monthR) % 2 == 0:
        if int(dayR)  >= nextRule:
            monthRule = int(monthR) + 1
            monthRule = str(monthRule).rjust(2, '0')
            return rulesWin[monthRule]
        else:
            monthRule = int(monthR) - 1
            monthRule = str(monthRule).rjust(2, '0')
            return rulesWin[monthRule]
    else:
        return rulesWin[monthR]

 
#Rules de Win
#rules1 = {'2020':{'01': 'WING', '02': ['14', 'WINJ'], '03': 'WINJ', '04': ['15', 'WINM'], '05': 'WINM', '06': ['10', 'WINQ'], '07': 'WINQ', '08': ['12', 'WINV'], '09': 'WINV', '10': ['14', 'WINZ'], '11': 'WINZ', '12': ['09', 'WING']}}


rules2 = {'01': 'WING', '03': 'WINJ', '05': 'WINM', '07': 'WINQ', '09': 'WINV','11': 'WINZ'}

#Rules de WDO
rulesWDO = {'01': 'WDOG', '02': 'WDOH', '03': 'WDOJ', '04': 'WDOK', '05': 'WDOM', '06': 'WDON', '07': 'WDOQ', '08': 'WDOU', '09': 'WDOV', '10': 'WDOX', '11': 'WDOZ', '12': 'WDOF'}


inputFiles = '/mnt/hd/test_files/10-03-2020/output_file/'
#inputFiles = '/mnt/hd/testRmoveFile'


for path, subdirs, files in os.walk(inputFiles):
    for name in files:

        fileName =  name.split('_')
        symbol = fileName[1][:4]
        year = fileName[2][:4]
        month = fileName[2][4:6]
        day = fileName[2][6:8]
        
        print('\nNova Estratégia')

        rules = []

        rulWdo = ruleWdo(month, rulesWDO)
        rules.append(rulWdo)
        rulWin = ruleWin(day, year, month, rules2)
        rules.append(rulWin)
        print('rules here: ', rules)

        print('rule para wdo: ', 'WDOJ' in rules)
        print('rule para win: ', 'WK' in rules)
        allPath = path+'/'+name
        if symbol[:4] not in rules:
            os.remove(allPath)
        print('file:', symbol[:4])

        #Agora que eu comparei, Eu vou excluir todos os aquivos que não fazem prte


        #adicionar a função que retorna as regras

#Usar isso path=os.path.join(path,file)

for path, subdirs, files in os.walk(inputFiles):
    #aqui é onde eu zero minhas rules
    rules = []
    print('paths',subdirs)
    print('\nrules no inicio: ', rules)
    for diretorios in files:

        
        print('file: ', diretorios)

        fileName =  name.split('_')
        symbol = fileName[1][:4]
        year = fileName[2][:4]
        month = fileName[2][4:6]
        day = fileName[2][6:8]

        rulWdo = ruleWdo(month, rulesWDO)
        if rulWdo not in rules:
            rules.append(rulWdo)
        rulWin = ruleWin(day, year, month, rules2)
        if rulWin not in rules:
            rules.append(rulWin)
        
        #allPath = path+'/'+name
        allPath = os.path.join(path, name)
        print('ve ai se o join funcionou')
        print(allPath)
        exit()
        if symbol[:4] not in rules:
            os.remove(allPath)

    print('Rules no fim: ', rules)

        #print('diretorios: ', diretorios)


exit()

'''
for path, subdirs, files in os.walk(inputFiles):
    for name in files:

        fileName =  name.split('_')
        symbol = fileName[1][:4]
        year = fileName[2][:4]
        month = fileName[2][4:6]
        day = fileName[2][6:8]
        
        print('\nNova Estratégia')

        if int(month) % 2 == 0:
            print('day', day)
            if int(day) < 9:
                monthRule = int(month) - 1
                monthRule = str(monthRule).rjust(2, '0')
                print('O simbolo é o seguinte: ', rules2[monthRule], month)
            
            elif int(day) >= 15:
                monthRule = int(month) + 1
                monthRule = str(monthRule).rjust(2, '0')
                print('O New é o seguinte: ', rules2[monthRule], month)
            
            else:
                hoje = datetime.datetime(int(year), int(month), 15)
                weekday15 = hoje.weekday()
                runOutDay = whenWednesday(weekday15)
                if 
                print('cheguei parou', year, month, day)
                print()
                exit()

            
        else:
            print('Esta aí o simbolo', rules2[month], month)
            #exit()
'''

print('Se é pra testar, então vamos lá')
quemSou = datetime.datetime.today()
print(quemSou.weekday())
umMes = '03'
quemSou1 = datetime.datetime(2020, int(umMes), 20)
print('quem sou novo', quemSou1.weekday())

diaAgora = whenWednesday(0)
print('resultado: ',diaAgora)

newDay = nextWednesday(0)
print('new day', newDay)