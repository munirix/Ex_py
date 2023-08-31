import numpy as np

arr = np.array(range(10))
arr[arr % 2 != 0] = -1
print(arr)
