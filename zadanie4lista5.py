klucz = {"a":"y", "e":"i", "i":"o", "o":"a", "y":"e"}
def szyf():
    x = input("Wpisz tekst do szyfrowania: ")
    y = list(x)
    for i in y:
        for j in klucz:
            y = y.insert(i, j)
    print(y)
szyf()
