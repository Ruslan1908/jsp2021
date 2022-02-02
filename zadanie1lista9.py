import numpy as np

#deklarowanie macierzy 5x5, która składa się z liczb rzeczywistych jednomianów (rzędy - całe równania, kolumny - jednomiany)
a = np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
#deklarowanie tablicy wyrazów wolnych i ich transpozycja
b = np.array([[6,2,-5,17,12]]).T

#obliczenie równań
c = np.linalg.solve(a,b)

x = c[0]
y = c[1]
z = c[2]
t = c[3]
u = c[4]
print ("x =", x, "y =", y, "z =", z, "t =", t, "u =", u)
#sprawdzenie czy równość jest prawdziwa
print (np.dot(a,c))
