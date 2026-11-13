def imprime_linha(n=5, carac='*'):
    print(carac * n)

num = int(input('Quantos caracteres você quer imprimir?'))
qual = input('Qual será o caractere a ser impresso?')
imprime_linha(num, qual)
imprime_linha(num)
imprime_linha()
imprime_linha(carac='@', n=2)
