lat_galeao = (22, 48, 34)
long_galeao = (43, 15, 0)
aeroporto_galeao = ('Galeão', lat_galeao, long_galeao)
lat_garulhos = (23, 26, 6)
long_garulhos = (46, 28, 22)
aeroporto_garulhos = ('Guarulhos', lat_garulhos,
                      long_garulhos)
aeroportos = {
    'Rio': aeroporto_galeao,
    'São Paulo': aeroporto_garulhos
}
for cidade in aeroportos:
    print('Aeroporto ' + cidade + ':\n\t' +
          aeroportos[cidade][0] + '\n\tLatitude: ' + 
          str(aeroportos[cidade][1][0]) + 'º' + 
          str(aeroportos[cidade][1][1]) + "'" + 
          str(aeroportos[cidade][1][2]) + '"' +
          '\n\tLongitude: ' + 
          str(aeroportos[cidade][2][0]) + 'º' + 
          str(aeroportos[cidade][2][1]) + "'" + 
          str(aeroportos[cidade][2][2]) + '"')
