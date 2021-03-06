import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfentries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfentries)

plt.hist(salaries)
plt.show()