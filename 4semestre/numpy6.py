import numpy as np
# sem alterar arr
arr,arr2 = np.array(range(10)),np.array(range(10))
arr2[arr % 2 != 0] = -1
print(arr2)
