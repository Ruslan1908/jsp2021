#W folderzeznajduje się plik "zmienne"

import zmienne
from time import time

def sortowanie_babelkowe(lista):
    n = len(lista)
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True
        n -= 1
        if zamien == False: break    
    print(lista)

t1=time()
sortowanie_babelkowe(zmienne.generator100())
t2=time()
print("Sortowanie 100 elementow zajelo: ", t2-t1)

t3=time()
sortowanie_babelkowe(zmienne.generator200())
t4=time()
print("Sortowanie 200 elementow zajelo: ", t4-t3)

t5=time()
sortowanie_babelkowe(zmienne.generator300())
t6=time()
print("Sortowanie 300 elementow zajelo: ", t6-t5)