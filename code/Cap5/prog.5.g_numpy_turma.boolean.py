import numpy as np

notas = np.array([5, 9, 5.5, 10, 8.4])
print(notas > 6) # [False True False True True]
print('Notas > 6:', notas[notas > 6]) # [ 9. 10. 8.4]
print('Notas <= 6:', notas[notas <= 6]) # [5. 5.5]
print(((notas > 6) & (notas < 10)).sum()) # entre 6 e 10: 2
notas[notas < 5.5] = 5.5
print(notas)
