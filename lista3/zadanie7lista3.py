n = int(input("Podaj wyraz kończący ciąg Fibonacciego: "))
#zadeklarowałem dwie zmienne, dla dwóch pierwszych wyrazów ciągu, poniważ są stałe
a = int(0)
b = int(1)
print("Wyraz 1 - :", a)
print("Wyraz 2 - :", b)
#w pętli znajduje się przedział zaczynający się od 1 i kończy się n-1(jest ostatni wyraz ciągu podany przez użytkownika, -1 jest dlateg, że w range() przedział zaczyna się od 0, więc wyraz np 5 był by pokazany jako 6)
for c in range(1, n-1):
    a, b = b, a+b #tutaj zastosowałem przypisanie wielokrotne, ponieważ on jest wykonywany od lewa do prawa, a przy próbie zastosowania a=b, b=a+b wychodziły inne liczby
    print("Wyraz", c+2, "- :", b) #c+2 jest po to, aby kolejny wyraz ciągu odpowiednio numerowało, ponieważ ciąg w for tak na prawdę zaczyna się od trzeciego wyrazu

