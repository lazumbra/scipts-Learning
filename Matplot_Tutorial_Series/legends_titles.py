import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

#A gente só usa label quando queremos imprimir legandas na 
#figura.
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')
#Legendas e titulos devem ser colocados antes de plt.show()
#E depois de plt.plot()
# Legendas só devem ser usadas quando se tem mais de um
#gráfico sendo criado na mesma figura.

plt.xlabel('Plot number')
plt.ylabel('Important var')

plt.title('Interesting graph\nCheck it out')
plt.legend()

plt.show()