import numpy as np

a = np.array([1,2,3])

x = np.repeat(a,3)
x = np.hstack((x,a))
arr = np.append(np.repeat(a,3),a)
print(x)
print(arr)

