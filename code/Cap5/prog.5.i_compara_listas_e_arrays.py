import numpy as np
import time
import random

num = 10000000

lista1 = random.choices(range(1,10001), k = num)
lista2 = random.choices(range(1,10001), k = num)
lista3 = [None] * num
print(len(lista3))

t1 = time.time()
for i in range(num):
	lista3[i] = lista1[i] * lista2[i]
t2 = time.time()
print ('Tempo total é  ', t2-t1)
print(type(lista3))
print(len(lista3))

l1 = np.array(lista1)
l2 = np.array(lista2)

t1 = time.time()
l3 = np.array(l1 * l2)
t2 = time.time()
print ('Tempo total é  ', t2-t1)
print(type(l3))
print(l3.size)
