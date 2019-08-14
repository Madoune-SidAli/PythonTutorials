import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7, 8, 6, 11, 9]
eating =   [2, 3, 4, 3, 2]
working =  [7, 8, 7, 8, 8]
playing =  [8, 5, 7, 2, 5]

plt.stackplot(days,
              sleeping,eating,working,playing,
              labels=['Slepping','Eating','Waeking','Playing'],
              colors=['red','blue','purple','green'],
              linewidth=5)

plt.xlabel('Days')
plt.ylabel('Activities')
plt.title('Daily life activities')
plt.legend()
plt.show()