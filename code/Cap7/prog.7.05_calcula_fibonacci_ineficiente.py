def fib(n):
    """Calcula n-ésimo termo da série de Fibonacci."""
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(100):
    print('fib(',i,'):',fib(i))
