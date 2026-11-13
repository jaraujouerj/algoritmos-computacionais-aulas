def fatorial(n):
    fat = 1
    for i in range(1,n+1):
        fat = fat * i
    return fat

n = int(input('Qual o número para calcular o fatorial? '))
fat = fatorial(n)
print ('O fatorial de', n, 'é', fat)
