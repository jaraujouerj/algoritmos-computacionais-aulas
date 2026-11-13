import math

def gera_coordenadas_aleatorias():
    """Gera par de coordenadas aleatórias."""
    x = y = 0
    return x, y

def coordenadas_dentro_circulo(x, y):
    """Testa se coordenadas estão dentro do círculo de raio 1."""
    return True

def calcula_pi(n):
    """Calcula pi e o erro associado a partir de n pontos."""
    conta_circulo = 0
    for i in range(n):
        x, y = gera_coordenadas_aleatorias()
        if coordenadas_dentro_circulo(x, y):
            conta_circulo += 1
    pi = 4 * conta_circulo / n
    erro = math.fabs(pi - math.pi)
    return pi, erro

num = int(input('Quantos pontos devem ser sorteados? '))
pi, erro = calcula_pi(num)
print('Com', num, 'pontos, o valor de pi é', pi, 'com erro', erro)
