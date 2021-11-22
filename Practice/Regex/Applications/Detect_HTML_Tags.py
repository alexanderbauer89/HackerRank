import re

def valid_tag(s):
    match = re.findall(r'[<](\w{1,})[ >]', s)
    return match
        
output = list()
for _ in range(int(input())):
    valid_tag_result = valid_tag(input())
    if(valid_tag_result):
        output.extend(valid_tag_result)

print(';'.join(sorted(list(set(output)))))
