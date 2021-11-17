lista = ["Kasia", "Basia", "Marek", "Darek"] #utworzenie listy
print(lista)
lista.append("Józek") #rozszerzenie listy o jeden kolejny element
print(lista)
lista.extend(["Ania", "Basia"]) #rozszerzenie listy o dwa kolejne elementy
print(lista)
lista.sort() #sortowanie listy
print(lista)
print(lista[3], "\n", lista[0:2], "\n", lista[-2:]) #wyświetlanie czwartego elementu listy, dwóch pierwszych elementów i dwóch ostatnich
lista.remove("Basia") #usuwanie elementu z listy
lista.remove("Basia") #ponowne użycie polecenia, ponieważ remove() służy do usuwania jednego elementu w liście. Jeśli elementów kilka, to usunie tylko pierwszy napotkany
print(lista)
print(len(lista)) #ilość ilementów w liście
krotka = (lista,) #utworzenie krotki. Ponieważ lista jest jako jeden element, dla utworzenia krotki po nazwie listy trzeba użyć przecinka
print(krotka)
