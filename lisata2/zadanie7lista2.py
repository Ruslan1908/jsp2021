help(sorted)
lista = [(2, 8), (5, 5), (9, 3), (1, 0), (3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]
print(lista)
sortowanie = sorted(lista, key = lambda x: x[1]) #sortowanie rosnąco odbywa się domyślnie, a za pomocą lambdy sortowanie odbywa się według drugiego elementu w krotce
print(sortowanie)
