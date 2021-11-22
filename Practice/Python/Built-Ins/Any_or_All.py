N, n = int(input()), input().split()
print(all([int(i)>0 for i in n]) and any([c == c[::-1] for c in n]))
