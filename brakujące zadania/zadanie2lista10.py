import itertools

class Listy():
    def __init__(self, lista, wynik):
        self.lista = lista
        self.wynik = wynik
    def ls(self):
        for i in range(0, len(self.lista)+1): #dla każdego elementu w przedziale od 0 do długości listy+1
            for j in itertools.combinations(self.lista, i): #każdy element kombinacji listy z ilością kombinacji(i)
                self.wynik.append(list(j)) #dodaje do pustej listy wynikowej uzyskaną listę z kombinacji
        print(self.wynik)

wynik = []
lista = [1, 2, 3]

listy = Listy(lista,wynik)

listy.ls()
