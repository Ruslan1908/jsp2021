def L():
    for row in range(6):
        print("*", end="")
        print() #wypisuje gwiazdki w kolumnie
    for col in range(5):
        print("*", end="")
    print() #tutaj dałem printa, bo bez niego górna gwiazdka "A" najeżdżała na wiersz "L"

def A():
    for row in range(11):
        for col in range(13):
            #warunek sprawdza i wpisuje gwiazdkę, jeśli element wiersza równy 4 i element kolumny większy od 2 i mniejszy od 11(inaczej środkowa kreska by wyjeżdżała za granicy)
            #dalej sprawdza położenie gwiazdek, które mają iść pod kątem, czyli np dla górnej gwiazdki element wiersza pierwszy (0) plus element kolumny siódmy(6) jest równy 6, w drugim wierszu 1+5=6 itd.
            #dla drugiej strony element kolumny minus wiersz, działa na tej samej zasadzie co poprzedni
            if (row==4 and (col>2 and col<11)) or row+col==6 or col-row==6:
                print("*", end="")
            else:
                print(end=" ") #jeśli warunek nie spełniony - wypełnie miejsca spacjami
        print()

def R():
    for row in range(7):
        for col in range(5):
            if col==0 or (col==4 and(row!=0 and row!=3)) or ((row==0 or row==3) and (col>0 and col<4)): #tutaj podobnie, jak z A, tylko więcej kombinacji, ponieważ R nie jest symetryczna.
                print("*", end="")
            else:
                print(end=" ")
        print()


L()
A()
R()
