#Programa que calcula o tamanho do Universo em milímetros.
tamanho_universo = 93000000000 #em anos-luz

#Cálculo da quantidade de segundos em 1 ano
segundos_por_min = 60 
segundos_por_h = 60 * segundos_por_min
segundos_por_dia = 24 * segundos_por_h
segundos_por_ano = 365 * segundos_por_dia

velocidade_luz_em_mms = 299792458000
tamanho_universo_mm = tamanho_universo \
					* velocidade_luz_em_mms \
					* segundos_por_ano 
print ("O Universo tem aproximadamente",
       tamanho_universo_mm, "milímetros.")
