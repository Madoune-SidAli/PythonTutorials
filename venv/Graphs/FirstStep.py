import matplotlib.pyplot as plt

plt.title('Test graph \nChek it out')
plt.xlabel('Plot Numbers')
plt.ylabel('Important var ')

x = [1, 2, 3]
y = [4, 5, 3]

x2 = [1, 2, 3]
y2 = [7, 4, 6]

plt.plot(x, y, label="First line")
plt.plot(x2, y2, label="Second line")


plt.legend()
plt.show()