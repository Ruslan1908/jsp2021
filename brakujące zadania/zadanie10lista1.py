import cmath
z = 1j
a = cmath.sin(z)
b = cmath.cos(z)
print("sin(z) = ", a, "\n", "cos(z) = ", b)
x = (a.real, a.imag)
print("Część rzeczywista i część urojona liczby sin(z): ", x)
y = (b.real, b.imag)
print("Część rzeczywista i część urojona liczby cos(z): ", y)
c = a**2+b**2
print("sin^2(z)+ cos^2(z) =", c)
d = c-1
print("Po odejmowaniu 1 od wyniku poprzedniego działania dany wynik nie jest równy 0, tylko ", d, ", zatem zależność sin^2(z)+cos^(z)=1 nie jest spełniona. Nie wszystko działa prawidłowo.")
print("Prawidłowe działanie: ")
x = z.real, z.imag
#Mając część rzeczywistą i urojoną liczby zespolonej 'i' można wyliczyć sinus (część rzeczywista podzielona przez moduł liczby 'z') oraz cosinus (część urojona podzielona przez moduł liczby 'z'
#Zatem suma kwadratów tych liczb wyniesie 1, co spełni zależność
a = z.real/abs(z)
b = z.imag/abs(z)
c = a**2+b**2
d = c-1
print(c)
print(d)

