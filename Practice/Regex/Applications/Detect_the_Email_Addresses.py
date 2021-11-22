import re

def valid_email(s):
    match = re.findall(r'[\w|.]*[@]\w{1,}(?:[.]\w{1,}){1,}', s)
    return match
        
output = list()
for _ in range(int(input())):
    valid_email_result = valid_email(input())
    if(valid_email_result):
        output.extend(valid_email_result)

print(';'.join(sorted(list(set(output)))))
