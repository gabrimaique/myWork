import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfentries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfentries)
ages = np.random.randint(low=21, high = 65, size = numberOfentries)

plt.scatter(ages, salaries)

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = 'r', label = "x squared")

plt.title("random plot")
plt.xlabel("salaries")
plt.ylabel("age")
plt.legend()
plt.show()

plt.savefig('prettier-plot.png')