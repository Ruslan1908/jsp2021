import time
import os

def szyfrowanie(szyfr, n):
    #alfabet jest podwójnie wypisany, ponieważ dla szyfrowania ostatnich liter
    #klucz musi się przemieszczać na pierwsze litery alfabetu
    alfabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    szyfr = szyfr.lower() #przekształcenie wprowadzonego tekstu na małe litery
    zaszyfr = ""

    for i in szyfr: #za pomocą for zwraca index litery, żeby potem zamienić ją na nową
        poz = alfabet.find(i) #find() szuka w zmiennej alfabet pierwsze podobieństwo, zatem zwróci numer tej litery
        npoz = poz + n #do indexu litery jest dodawany klucz
        if i in alfabet:
            zaszyfr = zaszyfr + alfabet[npoz] #dodawanie nowej litery, jako zaszyfrowanej
        else:
            zaszyfr = zaszyfr + i #jeśli to jest symbol, a nie litera, to jest on dodawany do zmiennej bez zmian
    katalog = str(input("Podaj nazwę katalogu w którym chcesz utworzyć plik zaszyfrowany: "))
    try:
        os.mkdir(katalog) #próba utworzyć katalog
    except FileExistsError: #jeśli katalog istnieje, to wyświetla się komunikat i program jest kontynuowany
        print("Katalog już istnieje. Plik zaszyfrowany został zapisany w nim.")
    os.chdir(katalog) #zmiana katalogu na katalog podany wcześniej
    plik = "plik_zaszyfrowany" + str(n) + "_" + time.strftime("%Y_%m_%d") + ".txt" #utworzenie nazwy pliku
#za pomocą time.strftime() tworzy odpowiedni format aktualnej daty
    p = open(plik, "w", encoding="utf-8") #tworzy plik do zapisu
    p.write(zaszyfr) #wypełnia plik zaszyfrowanym tekstem
    p.close() #zamyka plik
    print("Plik zaszyfrowany!")

def deszyfrowanie(zaszyfr, klucz):
    alfabet = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"
    zaszyfr = zaszyfr.lower()
    deszyfr = ""
    klucz = int(klucz)

    for i in zaszyfr:
        poz = alfabet.find(i)
        npoz = poz + klucz
        if i in alfabet:
            deszyfr = deszyfr + alfabet[npoz]
        else:
            deszyfr = deszyfr + i
    plik = "plik_deszyfrowany"+str(klucz)+"_"+time.strftime("%Y_%m_%d")+".txt"
    p = open(plik, "w", encoding="utf-8")
    p.write(deszyfr)
    p.close()
    print("Plik deszyfrowany!")
