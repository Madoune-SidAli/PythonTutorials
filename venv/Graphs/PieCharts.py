import matplotlib.pyplot as plt

plt.title('Daily life activities')

days =  {1, 2, 3, 4, 5}

sleeping = [7, 8, 6, 11, 7]
eating   = [2, 3, 4, 3, 2]
working  = [7, 8, 7, 2, 2]
playing  = [8, 5, 7, 8, 11]

slices = [7, 2, 2, 13]
activities = ['sleeping','eating','working','playing']
colors = ['r','c','y','g']

plt.pie(slices,
        labels=activities,
        colors=colors,
        startangle=0,
        explode=(0,0,0,1),
        autopct='%1.1f%%')

plt.show()