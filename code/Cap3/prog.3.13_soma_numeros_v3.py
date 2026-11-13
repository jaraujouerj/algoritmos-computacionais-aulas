n = int(input('Qual o número final? (0 para terminar '))
while n != 0:
  if n > 0:
      soma = 0
      i = 1
      while i <= n:
          soma = soma + i
          i = i + 1
      print('A soma de 1 até ', n, ' = ', soma)
  else:
	  print('Use números positivos')
  n = int(input('Qual o número final? (0 para terminar) '))
