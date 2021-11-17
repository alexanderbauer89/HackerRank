Regex_Pattern = r'^[^\d][^a,e,i,o,u][^b,c,D,F][^\s][^A,E,I,O,U][^.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
