import itertools
lista = [[2,4,3],[1,5,6],[9],[7,9,0]]
wynik = itertools.chain.from_iterable(lista)
print(list(wynik))
