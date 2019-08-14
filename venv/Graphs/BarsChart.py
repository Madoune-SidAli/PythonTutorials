import matplotlib.pyplot as plt

plt.title('Test graph \nChek it out')
plt.xlabel('Plot Numbers')
plt.ylabel('Important var ')

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 5]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 4, 6, 5, 8]

plt.bar(x, y, label="First line")
plt.bar(x2, y2, label="Second line",color='orange')


plt.legend()
plt.show()