import math

print('Graus  Radianos Seno Cosseno')
for graus in range(0, 361, 30):
    rad = graus * math.pi / 180
    print(graus, rad, math.sin(rad), math.cos(rad))
