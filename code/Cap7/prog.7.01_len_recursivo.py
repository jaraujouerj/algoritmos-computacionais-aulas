def tam(f):
    """Calcula tamanho da lista f."""
    if f == []:
        return 0
    else:
        return 1 + tam(f[1:])


def main():
    fila = [1, 43, 2, 3]
    tamanho = tam(fila)
    print('O tamanho da fila é', tamanho)        

main()
