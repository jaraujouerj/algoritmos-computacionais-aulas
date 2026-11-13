lin = 3
col = 4
matriz = [None] * lin
for i in range(lin):
    matriz[i] = [0] * col
print(matriz)
# com erro
matriz = [[0] * col] * lin
print (matriz)
matriz[0][2] = 33
print (matriz)
