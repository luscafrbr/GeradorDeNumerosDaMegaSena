import random

lista = []
k = 0

while(k<6):
    lista.append(random.randrange(1, 60))
    k = k + 1

print(sorted(lista))
