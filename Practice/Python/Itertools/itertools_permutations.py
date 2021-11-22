from itertools import permutations
S, k    =   input().split()
for x in list(permutations(sorted(S), int(k))):
    print(''.join(x))
