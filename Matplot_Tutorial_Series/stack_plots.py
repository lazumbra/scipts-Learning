import matplotlib.pyplot as plt

#Nesse tipo de gráfico você não pode ter legendas.

#Você pode fazer algo bem interessante para quebrar esse problema
# Em outros pequenos problemas. 
# Neste caso o que você faz é o seguinte: você cria gráfico
# Que não existe retas e que apenas vão colorir as coisas.
# Veja exemplo abaixo:

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], color='m', label='Sleeping')
plt.plot([], [], color='c', label='Eating')
plt.plot([], [], color='r', label='Working')
plt.plot([], [], color='r', label='Playing')

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c', 'r', 'k'])


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph\nCheck it out!')
plt.legend()
plt.show()