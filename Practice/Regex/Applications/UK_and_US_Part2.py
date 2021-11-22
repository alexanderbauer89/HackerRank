import re
txt = ' '.join([input() for _ in range(int(input()))])
for _ in range(int(input())):
    print(len(re.findall(input().replace('our','ou?r')+r'\b', txt)))
