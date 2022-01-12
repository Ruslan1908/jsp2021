def szyfrowanie(szyfr, klucz):
    #alfabet jest podwójnie wypisany, ponieważ dla szyfrowania ostatnich liter
    #klucz musi się przemieszczać na pierwsze litery alfabetu
    alfabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    szyfr = szyfr.lower() #przekształcenie wprowadzonego tekstu na małe litery
    zaszyfr = ""

    for i in szyfr: #za pomocą for zwraca index litery, żeby potem zamienić ją na nową
        poz = alfabet.find(i) #find() szuka w zmiennej alfabet pierwsze podobieństwo, zatem zwróci numer tej litery
        npoz = poz + klucz #do indexu litery jest dodawany klucz
        if i in alfabet:
            zaszyfr = zaszyfr + alfabet[npoz] #dodawanie nowej litery, jako zaszyfrowanej
        else:
            zaszyfr = zaszyfr + i #jeśli to jest symbol, a nie litera, to jest on dodawany do zmiennej bez zmian
    print("Twoją wiadomość zaszyfrowana: ", zaszyfr)
def deszyfrowanie(szyfr, klucz):
    #napisałem alfabet na odwrót, więc przy wpisaniu zaszyfrowanej wiadomości i podaniu klucza d "Deszyfrowanie: " wyświetli się deszyfrowany tekst
    alfabet = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"
    szyfr = szyfr.lower()
    deszyfr = ""

    for i in szyfr:
        poz = alfabet.find(i)
        npoz = poz + klucz
        if i in alfabet:
            deszyfr = deszyfr + alfabet[npoz]
        else:
            deszyfr = deszyfr + i
    print("Deszyfrowanie: ", deszyfr)
