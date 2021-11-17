import math
print("Program obliczy pierwiastki rzeczywiste równania kwadratowego o postaci ax^2+bx+c=0")
a = int(input("Podaj współczynnik a: "))
b = int(input("Podaj współczynnik b: "))
c = int(input("Podaj współczynnik c: "))
while a == 0:
    #jeśli a byłby 0, to wtedy kwadrat x przemnożony przez 0 dawał by 0 i nie było by to równanie kwadratowe
    a = int(input("Współczynnik a nie może być równy 0, podaj współczynnik jeszcze raz: "))
else:
    print("Twoje równanie kwadratowe ma postać: "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" = 0")
    delta = (b**2)-4*a*c
    print("Delta wynosi: "+str(delta))
    if delta > 0:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print("x1 = "+str(x1)+"\t x2 = "+str(x2))
    elif delta == 0:
        x0 = -b/(2*a)
        print("x0 = "+str(x0))
    else:
        print("Brak miejsc zerowych. Brak rozwiązań")
