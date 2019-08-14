import matplotlib.pyplot as plt

plt.title('Population ')
plt.xlabel('Ages')
plt.ylabel('Important var ')

population_ages = [10 ,12, 21, 42, 51, 45, 71, 81, 5, 100, 99, 92, 32, 26, 45, 58, 107, 31, 35, 39, 19, 22, 9, 60 ]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.show()