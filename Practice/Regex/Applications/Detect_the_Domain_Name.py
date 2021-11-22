import re

def valid_domain(s):
    m = re.findall(r'http[s]?://(?:www)*[.]*([\w.-]*\w*)["]?(?:[/?>]|["][ ][o])', s)
    return m
        
output = list()
for _ in range(int(input())):
    valid_domain_result = valid_domain(input())
    if(valid_domain_result):
        output.extend(valid_domain_result)
output = list(filter(None, output))
print(';'.join(sorted(list(set(output)))))
