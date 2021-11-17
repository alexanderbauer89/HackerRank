import re

def hi(s):
    return re.findall(r'^[H|h][I|i][\s][^D|d].*', s)
        
for _ in range(int(input())):
    match = hi(input())
    if match:
        print(match[0])
