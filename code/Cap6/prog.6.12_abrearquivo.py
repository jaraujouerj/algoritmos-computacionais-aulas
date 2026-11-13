arquivo = open('nomes.txt', 'r')
linhas = arquivo.readlines()
arquivo.close()
for linha in linhas:
    print(linha)
