import re

def valid_latitude_longitude(s):
    m = re.findall(r'^[(]([+-]?[1-9]\d*(?:[.]\d{1,})?)[,][ ]([+-]?\d{2,3}(?:[.]\d{1,})?)[)]$', s)
    if m and -90<=float(m[0][0])<=90 and -180<=float(m[0][1])<=180: 
        return 'Valid'
    else:
        return 'Invalid'
        
for _ in range(int(input())):
    print(valid_latitude_longitude(input()))
