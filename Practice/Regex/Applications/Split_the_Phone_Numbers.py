import re

def split_phone_numbers(s):
    return re.split(r'[ -]', s)

for i in range(int(input())):
    match = split_phone_numbers(input())
    print('CountryCode=' + match[0] + ',LocalAreaCode=' + match[1] + ',Number=' + match[2])
