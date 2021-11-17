x = input("Podaj dowolną liczbę całkowitą: ")
if int(x) % 2 == 0:
    print("Podana liczba jest parzysta")
else:
    print("Podana liczba jest nieparzysta")
#------------------------------------------------
y = input("Podaj dowolną liczbę całkowitą: ")
while int(y) % 2: #za pomocą "while", dopóki jest reszta z podanej liczby, będzie to liczba nieparzysta, w przeciwnym przypadku parzysta.
    print("Nieparzysta")
    break
else:
    print("Parzysta")
