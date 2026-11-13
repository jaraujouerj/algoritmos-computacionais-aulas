def insert_sort(lista):
    """Ordena uma lista pelo método da inserção"""
    for j in range(1, len(lista)):
        i = j - 1
        elemento = lista[j]
        while i >= 0 and lista[i] > elemento:
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = elemento
        print(lista)

l = [
    503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154,
    509, 612, 677, 765, 703
]
insert_sort(l)
