import re

def valid_PAN(s):
    match = re.findall(r'^[A-Z]{5}\d{4}[A-Z]$', s)
    if match: 
        return 'YES'
    else:
        return 'NO'
        
for _ in range(int(input())):
    print(valid_PAN(input()))
