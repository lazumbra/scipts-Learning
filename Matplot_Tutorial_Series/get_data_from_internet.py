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


# Essa função não está mais funcionando: bytedate2num
date, closep, highp, lowp, closep, adjusted_close, volumep = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0:bytespdate2num('%Y-%m-%d')})

plt.plot_date(date, closep, '-', label='Price')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Intresting Graph\nCheck it out')
plt.legend()
plt.show()