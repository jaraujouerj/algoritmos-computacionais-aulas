def fib(n):
    """Calcula n-ésimo termo da série de Fibonacci."""
    print('Função chamada com',n);
    if n < 2:
        print('Retornando',n)
        return n
    resul = fib(n-1) + fib(n-2)
    print('Retornando soma',resul);
    return resul
        
print('fib(4) :',fib(4))
