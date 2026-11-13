def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat = fat * i
    return fat

n = 5
resul1 = fatorial(n)
fat(4)
resul2 = fatorial(n + 1)
num = 10
resul3 = fatorial(num)
print("Resultados:", resul1, resul2, resul3)
print("Resultados:", fatorial(n), fatorial(n + 1),
      fatorial(num))
