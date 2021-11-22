from itertools import combinations_with_replacement
S, k = input().split()
for x in combinations_with_replacement(sorted(S), int(k)):
    print(''.join(x))
