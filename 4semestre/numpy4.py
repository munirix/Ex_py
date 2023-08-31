import numpy as np

arr = np.array(range(10))
impar = np.where(arr % 2 != 0)

print(impar)
