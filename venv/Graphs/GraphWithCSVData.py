import matplotlib.pyplot as plt
import  numpy as np

plt.title("Data of Test.txt file as graph")

plt.xlabel("X")
plt.ylabel("Y")

x, y = np.loadtxt('Test.csv',delimiter=',', unpack=True)

plt.plot(x, y)

plt.show()