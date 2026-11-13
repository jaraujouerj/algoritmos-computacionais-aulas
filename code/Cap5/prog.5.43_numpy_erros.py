import numpy as np

a = np.array(['Python', 1, 2, 3])
print(a)

a = [1, 2, 3, 4, 5]
b = a[1:]
b[0]= 42
print('Lista a:', a)
print('Lista b:', b)

a = np.array([1, 2, 3, 4, 5])
b = a[1:]
b[0]= 42
print('Lista a:', a)
print('Lista b:', b)
