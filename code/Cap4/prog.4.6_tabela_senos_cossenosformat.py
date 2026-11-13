import math

print ('{:>9}{:>9}{:>9}{:>9}'.format('Graus',
      'Radianos','Seno','Cosseno'))
for graus in range(0,361,30):
    rad = math.radians(graus)
    print ('{:>9.2f}{:>9.2f}{:>9.2f}{:>9.2f}'.format(graus, 
    rad, math.sin(rad), math.cos(rad)))
