import matplotlib.pyplot as plt

population_ages = [22, 44, 55, 34, 44, 76, 33, 59, 98, 102, 22, 37, 61, 68, 76, 76, 22, 98, 37, 11, 7, 8, 36, 98]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()