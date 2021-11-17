x = input("Wpisz literę: ")
#wymieniłem w listach samogłoski i spółgłoski, potem za pomocą if program sprawdza do której listy należy wprowadzony x
lista = ["a","ą","e","ę","i","o","ó","u","y","A","Ą","E","Ę","I","O","Ó","U","Y"]
lista2 = ["b","c","ć","d","f","g","h","j","k","l","ł","m","n","ń","p","t","w","x","z","ź","ż","B","C","Ć","D","F","G","H","J","K","L","Ł","M","N","Ń","P","T","W","X","Z","Ź","Ż"]
if x in lista:
    print("Podana litera jest samogłoską")
elif x in lista2:
    print("Podana litera jest spółgłoską")
else:
    print("Podana litera nie jest samogłoską ani spółgłoską lub w ogóle nie jest literą")
