class Zero():
 def suma(self, n):
        n = sorted(n) #sortowanie elementów listy dla łatwej interpretacji
        wynik = [] #końcowe listy zostaną dodane do tej listy
        i = 0 #pierwszy element
        while i < len(n):
            j = i+1 #drugi element
            k = len(n)-1 #trzeci element (ostatni w liście)
            while j < k:
                if n[i]+n[j]+n[k] < 0: #jeśli suma pierwszych dwóch i ostatniego elementów
                    j += 1             #jest mniejsza od 0, to przesuń j o jeden dalej po liście
                elif n[i]+n[j]+n[k] > 0: #jeśli suma trzech elementów większa od 0, to przesuń k o jedno miejsce w lewo 
                    k -= 1
                else:
                    wynik.append([n[i], n[j], n[k]]) #jeśli suma trzech wyrazów jest równa 0, dodaj jako trzyelementową listę do wyniku
                    j = j+1
                    k = k-1
                    while j < k and n[j] == n[j-1]: #zabezpieczenie przed powtórzeniem się list
                        j += 1
                    while j < k and n[k] == n[k+1]:
                        k -= 1
            i += 1
            while i < len(n) and n[i] == n[i-1]:
                i += 1
        return wynik

print(Zero().suma([0,-9,9,5,-2,-3,-18,20,-1,-1,3,3,1]))
