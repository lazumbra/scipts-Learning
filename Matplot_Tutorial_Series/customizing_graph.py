import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

source_code = urllib.request.urlopen(stock_price_url).read().decode()

stock_data = []
split_source = source_code.split('\n')

#Aqui eu estou apenas filtrando a minha informação
#stock_data vai ter tipo um texto e por isso vou precisar
#usar numpy para converter os dados para os valores
#que eu reamente quero usar
for line in split_source:
    split_line = line.split(',')
    if len(split_line) == 7:
        if 'Date' not in split_line:
            stock_data.append(line)


#Use plt.figure para poder fazer modificações no seu gráfico
#Sempre que quiser fazer modificações no grafico é importante
#Usar plt.figure
fig = plt.figure()
#subplot2grid não entendi muito bem. Vou explicar o que entendi
#Usa (1,1) pra dizer o tamanho do subplot e (0,0) para dizer
#Onde o gráfico vai começar.
ax1 =  plt.subplot2grid((1,1),(0,0))

# Essa função não está mais funcionando: bytedate2num
date, closep, highp, lowp, closep, adjusted_close, volumep = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0:bytespdate2num('%Y-%m-%d')})

ax1.plot_date(date, closep, '-', label='Price')
#Rotacionar as labels
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
#Para adicionar um grid no seu gráfico basta fazer
ax1.grid(True)#, color='g', linestyle='-', linewidth=5)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Intresting Graph\nCheck it out')
#Caso você queira ajustar como o gráfico é mostrado na tela
#Use os comandos abaixo
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.legend()
plt.show()