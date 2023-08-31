import numpy as np

arr = np.array(range(10))
#impar = np.where(arr % 2 != 0) -> (array([1, 3, 5, 7, 9], dtype=int64),)
arr[arr % 2 != 0] = -1
print(arr)
