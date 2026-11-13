primos = [2, 3, 13, 17, 19]
print('Lista completa: ', primos[:])
print('Lista de 2 em 2, começando em 0: ', primos[::2])
print('Lista de 3 em 3, começando em 0: ', primos[::3])
primos[2:2] = [5, 7]
primos[4:4] = [11]
print('Lista completa: ', primos[:])
print('Lista de 2 em 2, começando em 3: ', primos[3::2])
print('Lista de 2 em 2, terminando em 4: ', primos[:5:2])
primos[2:3] = []
print('Retira 1 elemento da posição 2: ', primos)
primos[::2] = [3, 11, 17, 23]
print('Substitui 4 elementos: ', primos)
primos[::2] = [2, 7, 13, 19]
primos[2:2] = [5]
print('Reinserindo elementos: ', primos[:])
