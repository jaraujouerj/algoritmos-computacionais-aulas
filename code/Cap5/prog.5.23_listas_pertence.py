primos = [2, 3, 5, 7, 11, 13, 17, 19]

for i in range(3, 20, 2):
    if i in primos:
        print(i, 'está primos.')
    else:
        print(i, 'não está primos.')
