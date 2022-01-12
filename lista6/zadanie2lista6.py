import SzyfrCezara as cez

szyfr = input("Wprowadż tekst do szyfrowania: ")
klucz = int(input("Podaj klucz szyfrowania: "))
cez.szyfrowanie(szyfr, klucz)
cez.deszyfrowanie(szyfr, klucz)
