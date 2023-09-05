import numpy as np

A = np.array([12,9,4,1,11,5,8,1,1,2,3,1]).reshape(3,-1)
print("A = \n",A)
B = np.array([1,5,1,7,1,9,1,1]).reshape(4,-1)
print("B = \n",B)

C = np.dot(A,B)
print("C = \n",C)
