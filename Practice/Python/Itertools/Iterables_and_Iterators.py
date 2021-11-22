from itertools import combinations
_, n, K     = int(input()), ''.join(input().split()), int(input())
count_total = sum(1 for _ in combinations(n, K))
count_a     = sum(1 for item in combinations(n, K)  if 'a' in item)
print(count_a / count_total)
