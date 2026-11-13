def fib(n):
    """Calcula n-ésimo termo da série de Fibonacci."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
print(fib(9))
