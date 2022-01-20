import SzyfrCezara as cez

def program():
    filepath = input("Podaj ścieżkę do pliku szyfrowalnego: ")
    try: #próba otworzyć plik
        f = open(filepath, "r", encoding="utf-8")
        szyfr = f.read() #wczytuje do zmiennej dane pliku
        n = int(input("Podaj klucz szyfrowania (przesunięcia) w zakresie 1-10: "))
        while n < 1 or n > 10: #zakres dla klucza(przesunięcia)
            print("Klucz nie mieści się w zakresie!")
            n = int(input("Podaj klucz szyfrowania (przesunięcia) w zakresie 1-10: "))
        cez.szyfrowanie(szyfr, n) #wywołanie funkcji z modułu
        f.close() #zamyka plik
    except FileNotFoundError: #jeśli plik nie znaleziony, to wyświetla się komunikat oraz program zaczyna się od nowa
        print("Plik nie znaleziono!")    
        program()
program()
