x = list(range(3, 100, 3)) #utworzenie listy za pomocą range(), gdzie pierwszym elementem jest "3", ostatnim "100"(ale będzie "99"), krok jest o "3".
print(x)
del x[4:100:3] #usuwanie elementów z listy za pomocą indexów, gdzie "4" jest piątym elementem listy, "99" ostatnim elementem listy i "3" jest krokiem usuwania, co trzeci element.
print(x)
print(len(x)) #za pomocą len() sprawdziłem ilość elementów listy.
y = sum(x)/23 #sum() sumuje wszystkie elementy listy "x" potem dzieli uzyskaną wartość przez ilość elementów (23).
print(y)

