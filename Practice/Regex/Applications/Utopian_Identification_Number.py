import re

def utopian_id(s):
    return re.findall(r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$', s)
        
for _ in range(int(input())):
    if utopian_id(input()):
        print('VALID')
    else:
        print('INVALID')
