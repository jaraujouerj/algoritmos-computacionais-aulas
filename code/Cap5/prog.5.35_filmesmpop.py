filmes = {1975:'Em Busca do Cálice Sagrado', 
          1979:'A Vida de Brian', 
          1983:'O Sentido da Vida', 
          1989:'Erik, O Viking'} 
del(filmes[1989]) #apaga elemento
print('Values:', filmes.values())
print('Itens:', filmes.items())
print('Chaves:', filmes.keys())
print('Filme de 1979:', filmes.get(1979))
print('Filme de 1971:', filmes.get(1971))
filmes[1971]='E Agora Para Algo Completamente Diferente'
print('Filme de 1971:', filmes.get(1971))
for ano in filmes:
    print ('"' + filmes[ano] + '" foi lançado em ' + str(ano)) 
 
