n = int(input())
s = set(map(int, input().split()))
for x in range(int(input())):
    method, *args = input().split()
    getattr(s, method)(*map(int, args))
print(sum(s))
