from itertools import product
a, b =   list(map(int, input().split())), list(map(int, input().split()))
for item in product(a, b):
    print(item, end=' ')
