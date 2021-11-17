y = []
z = 0 #ta zmienna zadeklarowana dla indeksowania pierwszego elementu listy a potem w pętli for dla kolejnych elementów listy
for x in range(100, 401): #przedział jest do 401, ponieważ 400 by nie należało wtedy do przedziału
    if x%2 == 0: #sprawdza czy liczba jest podzielna przez dwa
        z+=1 #indeks dla każdego kolejnego elementu listy
        y.insert(z,x) #wstawia do pustej list "y" wszystkie parzyste liczby z przedziału
#lista automatycznie oddziela elementy przecinkami, więc nic z tym nie robiłem
print(y)
