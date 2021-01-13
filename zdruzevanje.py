import random
import numpy as np
import time
import matplotlib.pyplot as plt


random.seed(10)

dimensions = [0, 100, 500, 1000, 1500, 2000, 2500]
times_py = [0, 0, 0, 0, 0, 0, 0]
times_np = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(dimensions)):
    size = dimensions[i]
    print("Size: ", str(size))

    X = [[random.random() for e in range(size)] for m in range(size)]
    # print(X)

    Y = [[random.random() for e in range(size)] for m in range(size)]
    # print(Y)

    res = [[0 for e in range(size)] for m in range(size)]
    # print(res)

    Xn = np.array(X)
    Yn = np.array(Y)

    initialTime = time.time()

    res2 = X + Y

    time_s = time.time() - initialTime
    times_py[i] = time_s
    print("Time taken by nested list :",
          time_s,
          "seconds")

    initialTime = time.time()
    # res_np = np.dot(Xn, Yn)
    res_np = array = np.concatenate((Xn, Yn),
                          axis=0)
    # print(res_np)
    time_s = time.time() - initialTime
    times_np[i] = time_s
    print("Time taken by Numpy :",
          time_s,
          "seconds")

    print("----------------------")

print(dimensions)
print(times_py)
print(times_np)

plt.plot(dimensions, times_py, label="Python lists")
plt.plot(dimensions, times_np, label="Numpy arrays")

# naming the x axis
plt.xlabel('Dimenzija matrike')
# naming the y axis
plt.ylabel('Čas izvedbe [s]')
# giving a title to my graph
plt.title('Združevanje matrik')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
# plt.savefig('zdruzevanje.png', bbox_inches='tight')
