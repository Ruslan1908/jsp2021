import matplotlib.pyplot as plt

names = ['Python','C','Java','C++','C#','Visual Basic','JavaScript','Assembly','SQL','Swift']
values = [13.58, 12.44, 10.66, 8.29, 5.68, 4.74, 2.09, 1.85, 1.80, 1.41]

plt.figure(figsize=(12,12)) #rozmiar wykresu
plt.bar(names, values) #wykres słupkowy, gdzie oś X to nazwy języków, a oś Y wartości popularności
plt.xlabel('nazwy') #nazwa osi x
plt.ylabel('ranking') #nazwa osi y
plt.suptitle('Ranking języków programowania') #tytuł wykresu
plt.show() #rysowanie wykresu
