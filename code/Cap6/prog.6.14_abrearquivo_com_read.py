arquivo = open('nomes.txt', 'r')
texto = arquivo.read()
arquivo.close()
print ('Imprimindo linhas de texto')
print(texto)
linhas = texto.split('\n')
print ('Imprimindo linhas (read com split)')
for linha in linhas:
    print (linha)
