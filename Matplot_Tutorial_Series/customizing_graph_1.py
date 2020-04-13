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
#Eu tinha um texto e tranformo o texto em uma lista
#Cada elemento da lista era separado pelo '\n'
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
ax1 = plt.subplot2grid((1,1),(0,0))
# Essa função não está mais funcionando: bytedate2num
date, closep, highp, lowp, closep, adjusted_close, volumep = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0:bytespdate2num('%Y-%m-%d')})

ax1.plot_date(date, closep, '-', label='Price')

#Caso você queira colocar legenda nas partes sombreadas
#Você vai ter de "plotar" dois gráficos vazios
#Veja o exemplo abaixo
ax1.plot([], [], linewidth=5, label='loss', color='r', alpha=0.3)
ax1.plot([], [], linewidth=5, label='gain', color='g', alpha=0.3)

#Caso você queira pintar a área abaixo do gráfico
#Você usar plot_date ou fill_between para pintar
#Mas também é possivel usar os dois caso queira pintar
#E ainda ter a reta no gráfico.
#Você pode usar um fator de opacidade com o parametro alpha
#Você pode dar um limiar. Por exemplo o primeiro valor pra pintar
#Aí ele vai pinar tudo acima ou tudo abaixo
#Você também pode usar where para especificar partes específicad
#Do gráfico que você quer pintar. Exemplo eu quero pintar
#Os pontos do gráfico maiores que closep[0]
#Se eu quiser colocar uma cor específica eu preciso usar facecolor
#Podemos pintar duas cores paa o gráfico também. Aí eu preciso
#Fazer outro fill_between. Digamos que esse outro fill_between é nossa perda
ax1.fill_between(date, closep, closep[0], where=(closep > closep[0]), facecolor='g', alpha=0.3)
ax1.fill_between(date, closep, closep[0], where=(closep < closep[0]), facecolor='r', alpha=0.3)

#Rotacionar as labels
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
#Para adicionar um grid no seu gráfico basta fazer
ax1.grid(True)# color='g', linestyle='-', linewidth=5)
#Adicionar cor nas legendas x e y
ax1.xaxis.label.set_color('c')
ax1.yaxis.label.set_color('r')
#Caso você queira especificar os valores para o yaxis ser mostrado
ax1.set_yticks([0,200,400,700])

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Intresting Graph\nCheck it out')
#Caso você queira ajustar como o gráfico é mostrado na tela
#Use os comandos abaixo
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.legend()
plt.show()