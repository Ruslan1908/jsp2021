def nty_wyraz(n, a1, q):
    nty = a1*q**(n-1)
    print(nty)

n = int(input("Podaj numer elementu ciągu: "))
a1 = input("Podaj wartość pierwszego elementu ciągu (domyślnie 1): ")
if not a1==float or a1==int: #jeśli wartość zmiennej nie jest float albo int, to domyślnie a1=1
    a1=int(1)
q = input("Podaj wartość iloczynu geometrycznego (domyślnie 2): ")
if not q==float or q==int: #tak samo, jak z a1 q domyślnie przyjmie wartość 2
    q=int(2)

nty_wyraz(n, a1, q)
