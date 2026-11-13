print ('Tabela de conversão de Fahrenheit para Celsius')
for fahr in range(0,301,20):
    celsius = (5/9)*(fahr - 32)
    print ('{:>5d} -> {:>5.1f}'.format(fahr, celsius))
