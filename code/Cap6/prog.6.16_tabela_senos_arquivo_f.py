import math

arquivo = open('tabelaSenoCosseno.txt', 'w')
arquivo.write (f"{'Graus':>9}{'Radianos':>9}{'Seno':>9}{'Cosseno':>9}\n")
for graus in range(0,361,30):
    rad = math.radians(graus)
    arquivo.write(f'{graus:>9.2f}{rad:>9.2f}{math.sin(rad):>9.2f}{math.cos(rad):>9.2f}\n')
arquivo.close()
