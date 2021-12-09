liczba = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":30, 
"x":10, "IX":9, "V":5, "IV":4, "I":1}
def liczba_f():
    x = str(input("Podaj liczbę rzymcką: "))
    r = 0
    for i in x:
        r += liczba[i]
    print(r)
liczba_f()