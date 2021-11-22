import re

def valid_IP(s):
    match_ipv4 = re.findall('^(\d*)[.](\d*)[.](\d*)[.](\d*)$', s)
    match_ipv6 = re.findall(r'^([a-f0-9:]+:+)+[a-f0-9]+$', s)
    if match_ipv4:
        for ip_block in match_ipv4[0]:
            if int(ip_block) > 255:
                return 'Neither'
        return 'IPv4'
    elif match_ipv6:
        return 'IPv6'
    else:
        return 'Neither'
        
for _ in range(int(input())):
    print(valid_IP(input()))
