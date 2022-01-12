import SzyfrCezara as cez
import os

def program():
    try:
        katalog = input("Podaj ścieżkę do katalogu z plikiem: ")
        os.chdir(katalog)
    except FileNotFoundError:
        print("Katalog nie istnieje!")
        program()
    try:
        plik = input("Podaj nazwę pliku: ")
        f = open(plik, "r", encoding="utf-8")
        zaszyfr = f.read()
    except FileExistsError:
        print("Plik nie istnieje!")
        program()
    n = list(plik) #tworzy listę z nazwy pliku
    klucz = n[17] #szyka 18 element, czyli klucz deszyfrowania
    cez.deszyfrowanie(zaszyfr, klucz)
    f.close()
program()
