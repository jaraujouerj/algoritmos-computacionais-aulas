arquivo = open('nomes.txt', 'r')
linhas =  [linha.rstrip() for linha in arquivo.readlines()]
arquivo.close()
for linha in linhas:
    print (linha)
