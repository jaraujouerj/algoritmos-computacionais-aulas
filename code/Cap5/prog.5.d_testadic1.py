d = {'amazonas': 'AM', 'rio de janeiro': 'RJ'}
print('amazonas' in d)         # True (testa as CHAVES)
print(d.get('acre', '?'))      # ’?’ (sem KeyError)
for chave in d:                # percorre as chaves
    print(chave, '->', d[chave])
for chave, valor in d.items(): # chave e valor juntos
    print(chave, valor)
print(list(d.keys()), list(d.values()))
del d['amazonas']
