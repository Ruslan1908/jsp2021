import trojkat as t #zaimportowałem moduł i nadałem mu krótszą nazwę jako "t"

def boki():
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    if a >= b+c or b >= a+c or c >= a+b:
        print("Najdłuższy bok nie jest krótszy od sumy dwóch pozostałych.")
        boki()
    else:
        print("Obwód trójkąta jest równy: ", t.obwod(a,b,c))
        print("Pole trójkąta wynosi: ", t.pole(a,b,c))
        t.rodzaj(a,b,c)
        t.rodzaj2(a,b,c)

boki()
