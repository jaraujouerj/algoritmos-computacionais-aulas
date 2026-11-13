from math import radians, sin, cos

print('{:>9}{:>9}{:>9}{:>9}'.format('Graus', 'Radianos',
                                    'Seno', 'Cosseno'))
for graus in range(0, 361, 30):
    rad = radians(graus)
    print('{:>9.2f}{:>9.2f}{:>9.2f}{:>9.2f}'.format(
        graus, rad, sin(rad), cos(rad)))
