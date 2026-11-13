def divide():
    """Divide x por y."""
    try:
        x = int(input('Digite um numerador:'))
        y = int(input('Digite um denominador:'))
        print('A divisão de', x, 'por', y, 'é igual a', x/y)
    except ZeroDivisionError:
        print('Tentativa de divisão por zero.')
    except ValueError:
        print('Número inválido.')

divide()
