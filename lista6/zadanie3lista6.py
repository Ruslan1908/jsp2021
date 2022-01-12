def look_and_say(s):
    wynik = [] #wynikiem będzie lista
    i = 0
    while i < len(s):
        x = 1 #ta zmienna będzie przyjmować wartość jedynki w każdej liczbie ciągu
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            x += 1
        wynik.append(str(x) + s[i])
        i += 1
    return ''.join(wynik)

s = "1" #w danym ciągu każda liczba kończy się jedynką
n = int(input("Podaj n pierwszych wyrazów ciągu look-and-say: "))
for i in range(n-1):
    s = look_and_say(s) #zmienna "s" będzie przyjmowała za każdym przejściem w pętli wartość z funkcji
    print(s)
