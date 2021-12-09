n =int(input("wpisz summu pierwszych N członkowie pewnej liczby: "))
sum = 0
k = 1
s = 1
while s<= n:
    o = k/s
    sum += o
    k = k + 2
    s = s+1
print (sum)