import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6]])
print(m.shape) # (2, 3)
print(m[1, 2]) # 6 (linha 1, coluna 2)
print(m[:, 0]) # [1 4] (coluna 0)
print(m[0, :]) # [1 2 3] (linha 0)
print(m.sum(axis=0)) # [5 7 9] (soma de cada COLUNA)
print(m.sum(axis=1)) # [ 6 15] (soma de cada LINHA)
print(m.T)
