a = int(input("podaj a: "))
b = int(input("podaj b: "))

while b:
    a,b = b, a%b
print("największy wspólny dzielnik: ",a)
