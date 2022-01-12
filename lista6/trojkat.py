def obwod(a,b,c):
    ob = a+b+c
    return ob
def pole(a,b,c):
    import math
    p = (a+b+c)/2
    P = math.sqrt(p*(p-a)*(p-b)*(p-c))
    #zastosowałem wzór na pole, w którym wystarczy mieć boki oraz połowę obwodu
    return P
def rodzaj(a,b,c):
    #zastosowałem twierdzenia zgodnie z którymi w matematyce można wyznaczyć rodzaj trójkąta
    if a**2==(b**2)+(c**2) or b**2==(a**2)+(c**2) or c**2==(a**2)+(b**2):
        print("Trójkąt jest prostokątny.")
    elif a**2>(b**2)+(c**2) or b**2>(a**2)+(c**2) or c**2>(a**2)+(b**2):
        print("Trójkąt jest rozwartokątny.")
    elif a**2<(b**2)+(c**2) or b**2<(a**2)+(c**2) or c**2<(a**2)+(b**2):
        print("Trójkąt jest ostrokątny.")
def rodzaj2(a,b,c):
    if a==b==c:
        print("Trójkąt jest równoboczny.")
    elif a==b or a==c or b==c:
        print ("Trójkąt jest równoramienny.")
    elif a!=b and a!=c and b!=c:
        print("Trójkąt jest różnoboczny.")
