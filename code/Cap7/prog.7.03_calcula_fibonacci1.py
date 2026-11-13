def fib(n):
    """Calcula n-ésimo termo da série de Fibonacci."""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
        
print(fib(8))
