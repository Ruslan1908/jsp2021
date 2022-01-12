import time

n = int(input("Podaj wyraz kończący ciąg Fibonacciego: "))
#zadeklarowałem dwie zmienne, dla dwóch pierwszych wyrazów ciągu, poniważ są stałe
a = int(0)
b = int(1)
def iteracja(n,a,b):
    t1_start = time.process_time() #odlicza czas od rozpoczęcia funkcji
    print("Wyraz 1 - :", a)
    print("Wyraz 2 - :", b)
    #w pętli znajduje się przedział zaczynający się od 1 i kończy się n-1(jest ostatni wyraz ciągu podany przez użytkownika, -1 jest dlateg, że w range() przedział zaczyna się od 0, więc wyraz np 5 był by pokazany jako 6)
    for c in range(1, n-1):
        a, b = b, a+b #tutaj zastosowałem przypisanie wielokrotne, ponieważ on jest wykonywany od lewa do prawa, a przy próbie zastosowania a=b, b=a+b wychodziły inne liczby
        print("Wyraz", c+2, "- :", b) #c+2 jest po to, aby kolejny wyraz ciągu odpowiednio numerowało, ponieważ ciąg w for tak na prawdę zaczyna się od trzeciego wyrazu
    t1_stop = time.process_time() #zatrzymoje liczenie czasu działania funkcji
    print("Minęło czasu dla iteracji: ", t1_stop)

def rekurencja(n):
    if n==1:
        return 0 #dla 1 wyrazu zwróci wartość 0
    if n==2:
        return 1 #dla 2 wyrazu zwróci wartość 1
    return rekurencja(n-1)+rekurencja(n-2) #n-2 wyraz pierwszy z dwóch przed podanym dodaje do wyrazu drugiego przed podanym n wyrazem

iteracja(n,a,b)
t2_start = time.process_time()
print("Wyraz", n, "- :", rekurencja(n))
t2_stop = time.process_time()
print("Minęło czasu dla rekurencji: ", t2_stop)
