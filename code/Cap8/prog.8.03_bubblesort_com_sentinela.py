def bubblesort(lista):
    """Ordena uma lista pelo método da bolha"""
    n = len(lista)
    fora_de_ordem = True
    while fora_de_ordem:
        fora_de_ordem = False
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j],lista[j + 1] = lista[j + 1],lista[j]
                fora_de_ordem = True
        print(lista)

l = [
    503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154,
    509, 612, 677, 765, 703
]

bubblesort(l)
