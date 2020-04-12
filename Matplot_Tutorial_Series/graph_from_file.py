import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []

#Part 1
#Parte 1 mostra como ler um csv da pior forma possivel
#Na parte 2 a gente vai ver como realmente se feve ler u arquivo.
'''
with open('example.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

plt.plot(x, y, label='Loaded from file!')
'''

#Part 2
#Usamos o parametro unpack para guardar os valores nas variáveis x e y
x, y = np.loadtxt('example.csv', delimiter=',', unpack=True)
plt.plot(x, y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()