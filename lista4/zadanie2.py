from itertools import groupby
x = ['a', 'a', 'a', 'b', 'c', 'c', 'f']
b = [el for el, _ in groupby(x)]
print(b)