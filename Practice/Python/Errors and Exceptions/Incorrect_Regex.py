import re
for _ in range(int(input())):
    try:
        regx = re.compile(input())
        print(True)
    except re.error:
        print(False)
