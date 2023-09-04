import numpy as np

a = np.array([1, 2, 3])
# tile -> 123 123 123
var_tile = np.tile(a, 3)
# repeat -> 111 222 333
var_repeat = np.repeat(a, 3)
arr = np.append(var_repeat,var_tile)
print(arr)
