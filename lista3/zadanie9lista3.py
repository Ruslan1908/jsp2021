m = int(input("Podaj ilość wierszy: "))
n = int(input("Podaj ilość kolumn: "))
#tutaj zastosowałem generator zagnieżdżony. Z przedziału "m" są tworzone wiersze, potem z "n" kolumny. Za pomocą tego utworzy się macierz, którą wypełniłem za pomocą formuły i*j
a = [[i*j for i in range(m)] for j in range(n)]
for wiersz in a:
    print(' '.join([str(elem) for elem in wiersz]))
#aby wszystkie te elementy ułożyły się w tablicę zostały oni pobrane za pomocą for do zmiennej wiersz, potem połączeni najpierw spacją(dla lepszej czytelności), zatem elementy z utworzonej zmiennej były zamienione na znaki
