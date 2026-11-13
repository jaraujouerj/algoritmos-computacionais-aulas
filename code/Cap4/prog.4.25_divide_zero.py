def divide(x, y):
    """Divide x por y."""
    try:
        z = x / y
        print(z)
    except ZeroDivisionError:
        print('Tentativa de divisão por zero')

divide(1, 2)
divide(1, 0)
