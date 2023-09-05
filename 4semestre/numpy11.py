import numpy as np

a = np.array([1, 3, 7, 1, 2, 6, 0, 1])

b = np.sort(a)[::-1]
dois_maiores = np.where((a <= b[0]) & (a >= b[1]))[0]

print(dois_maiores)
