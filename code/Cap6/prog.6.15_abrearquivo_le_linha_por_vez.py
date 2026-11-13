arquivo = open('nomes.txt', 'r')

for linha in arquivo:
    print (linha.rstrip())
arquivo.close()
