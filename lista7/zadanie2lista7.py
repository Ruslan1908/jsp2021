import time
import random

lista1 = [] #utworzono 3 puste listy
lista2 = []
lista3 = []
t1_start = time.process_time()
for i in range(0,101): 
    lista1.append(random.randint(0,20)) #dla przedziału od 0 do 100 wypełni listę losowymi elementami w przedziale <0,20>

for i in range(1, len(lista1)):
    j = i-1 #poprzedni element listy dla porównywalnego [i]
    key = lista1[i] #zmienna pomocnicza dla elementu porównywalnego dla sortowania w liście
    while j >= 0 and key < lista1[j]: #wykonywanie pętli dopóki element znajdujący się przed [i] jest większy lub równy 0 i [i] jest mniejszy od elementu [j]
        lista1[j+1] = lista1[j] #zmiana elementu po prawej stronie od [i] na element [j], np czwarty element będzie zastąpiony trzecim
        j-=1 #za każdym przejściem j sięzmniejsza
    lista1[j+1] = key #na miejsce [j+1] wpisywana jest wartość elementu [i]
print(lista1)
print()
#dalej wszystko działa na tej samej zasadzie co pierwsza lista
for i in range(0,201):
   lista2.append(random.randint(0,20))

for i in range(1, len(lista2)):
    j = i-1
    key = lista2[i]
    while j >= 0 and key < lista2[j]:
        lista2[j+1] = lista2[j]
        j-=1
    lista2[j+1] = key
print(lista2)
print()

for i in range(0,301):
    lista3.append(random.randint(0,20))

for i in range(1, len(lista3)):
    j = i-1
    key = lista3[i]
    while j >= 0 and key < lista3[j]:
        lista3[j+1] = lista3[j]
        j-=1
    lista3[j+1] = key
print(lista3)
t2_stop = time.process_time()
print("Czas: ", t2_stop)
