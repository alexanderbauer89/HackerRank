import re

def scoring(s):
    needle = 'hackerrank'
    if re.search(r'^' + needle + '$', s):
        return 0
    elif re.search(r'^' + needle, s):
        return 1
    elif re.search( r'' + needle + '$', s):
        return 2
    else:
        return -1

for _ in range(int(input())):
    print(scoring(input()))
