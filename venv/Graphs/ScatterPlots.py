import matplotlib.pyplot as plt

plt.title('Test graph \nChek it out')
plt.xlabel('Plot Numbers')
plt.ylabel('Important var ')

x = [1,5,9,19,4,75,12,8,12,35,15,1,5,80,5,80,7,8,4,40,4,40,4,4]
y = [2,4,8,7,9,5,7,8,4,2,20,14,21,25,95,75,84,35,96,2,2,8,14,29]


plt.scatter(x,y,label="skitcat",color="red", marker="*",linewidths=5)


plt.legend()
plt.show()