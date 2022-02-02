import math
x=(-17**(1/2))*1j
print("(-17**(1/2))*1j = ", x)
y=x.conjugate()
print("Pierwiastek z -17: ", y)
import cmath
z=cmath.sqrt(-17)
print("Pierwiastek z -17 za pomocą cmath: ", z)
(a)=y-z
print("Porównanie: (-0+4.123105625617661j)-4.123105625617661j = ", abs(a))
