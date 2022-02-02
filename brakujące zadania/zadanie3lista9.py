import numpy as np
import math
import matplotlib.pyplot as plt

g = 9.81 #przyśpieszenie ziemskie

def hmax(v0, g): #przyjmuje jako argumenty prędkość początkową i przyśpieszenie ziemskie
    hm = (v0**2)/(2*g) #wzór na wysokość
    print("Wysokość maksymalna wynosi:", round(hm, 2), "m") #wynik zaokrąglany do 2 miejsc po przecinku

def zasieg(v0,g,alpha):
    alpha *= 2 #zgodnie ze wzorem kąt jest mnożony razy 2
    sinus = math.sin(math.radians(alpha)) #konwertacja w radiany i wyliczenie sinusa
    z = ((v0**2)*sinus)/g #ze wzoru na zasięg
    print("Zasięg rzutu wynosi:", round(z, 2), "m")

def czaslotu(v0,g,alpha):
    sinus = math.sin(math.radians(alpha))
    t = (2*v0*sinus)/g #ze wzora na czas
    print("Czas lotu wynosi:", round(t, 2), "s")

def wykresy(v0,g,alpha):
    alpha = math.radians(alpha)
    t = (2*v0*math.sin(alpha))/g
    interwaly = np.arange(0, t, 0.001)
    x = []
    y = []
    for i in interwaly: #tor rzutu
        x.append(v0*math.cos(alpha)*i)
        y.append(v0*math.sin(alpha)*i-0.5*g*(i**2))

    x1 = interwaly
    y1 = []
    for i in interwaly: #prędkość chwilowa w kierunku pionowym i poziomym
        vy = v0*math.sin(alpha)-g*i
        vx = v0*math.cos(alpha)
        vw = math.tan(vy/vx)
        y1.append(vw)

    s = (2*v0*t)/2 #droga całkowita
    x2 = interwaly
    y2 = []
    for i in interwaly:
        y2.append(s*i)
    
    plt.figure(figsize=(12,12))
    plt.subplot(3,1,1).plot(x1, y1)
    plt.title('Prędkość chwilowa w kierunku pionowym i poziomym')
    plt.subplot(3,1,2).plot(x2, y2)
    plt.title('Położenie od czasu')
    plt.subplot(3,1,3).plot(x, y)
    plt.title('Tor rzutu')
    plt.show()
    


while 1: #dopóki wartość nie będzie typu float będzie wykonywana pętla
    try:
        v0 = float(input("Podaj prędkość początkową: "))
        break
    except:
        print("Podałeś złą wartość. Spróbuj jeszcze raz.")

while 1:
    try:
        alpha = float(input("Podaj kąt rzutu: "))
        break
    except:
        print("Podałeś złą wartość. Spróbuj jeszcze raz.")

print(40*"-")
hmax(v0, g)
zasieg(v0,g,alpha)
czaslotu(v0,g,alpha)
print(40*"-")
wykresy(v0,g,alpha)
