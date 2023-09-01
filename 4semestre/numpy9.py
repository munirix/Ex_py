import numpy as np

a = np.array(range(10)).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)


print(a)
print('\n')
print(b)

#print("\nVertical stacking:\n", np.vstack((a, b)))

print("\nHorizontal stacking:\n", np.hstack((a, b)))
