import math

a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę, mniejszą od pierwszej: ")
while b>=a:
    print("Druga liczba jest większa od pierwszej lub równa jej! Podaj liczbę mniejszą od ", a)
    b = input()
else:
    print("Reszta z dzielenia, to: ", int(b)%int(a))
    Z = int(b)%int(a)
    Z*=Z+3
    print("Z*(Z+3) = ", Z)
