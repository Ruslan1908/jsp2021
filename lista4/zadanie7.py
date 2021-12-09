def elm(row):
    row = [1] + row
    for i in range(1, len(row)-1):
        row[i] += row[i+1]
row = []
n = int(input("Podaj ilosc wierszy:"))
for i in range(n):
    row = elm(row)
    print(row)