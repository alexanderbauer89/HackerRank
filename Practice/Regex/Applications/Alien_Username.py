import re

def alien_username(s):
    return re.findall(r'^[_.][0-9]{1,}[a-zA-Z]{0,}[_]?$', s)
        
for _ in range(int(input())):
    if alien_username(input()):
        print('VALID')
    else:
        print('INVALID')
