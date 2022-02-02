liczby_s = {"jeden":1, "dwa":2, "trzy":3, "cztery":4, "pięć":5, "sześć":6,
"siedem":7, "osiem":8, "dziewięć":9, "dziesięć":10, "jedenaście":11,
"dwanaście":12, "trzynaście":13, "czternaście":14, "piętnaście":15,
"szesnaście":16, "siedemnaście":17, "osiemnaście":18, "dziewiętnaście":19,
"dwadzieścia":20, "trzydzieści":30, "czterdzieści":40, "pięćdziesiąt":50}

def liczby_d():
    x = input("Podaj liczbę słownie od 1 do 59: ")
    r = 0 #zmienna do której będzie dodawana wartość ze słownika
    for i in x.split(): #.split() rozdziela wprowadzoną liczbę na elementy listy(słowa), które potem będą wyszukiwane w słowniku
        r+= liczby_s[i] #do r wypisuje wartości odpowiadające kluczom ze słownika
    print(r)
        
liczby_d()
    
