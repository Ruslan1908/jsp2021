#każdy wiersz zwiększa się o jeden element i każdy element w konkretnym wierszy przyjmuje wartość wiersza
for x in range(1,10):
    for y in range(1, x+1):
        print(x, end="")
    print()
