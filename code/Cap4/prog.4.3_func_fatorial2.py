def fatorial(n):
    """Calcula o fatorial de n."""
    fat = 1
    for i in range(1,n+1):
        fat = fat * i
    return fat
    
n = int(input('Qual o número para calcular o fatorial? '))
print ('O fatorial de', n, 'é', fatorial(n))
