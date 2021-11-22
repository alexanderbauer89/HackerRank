from itertools import combinations
S, k = input().split()
for x in range(1, int(k) + 1):
    for y in combinations(sorted(S), x):
        print(''.join(y))
