#alternative solution with regex
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names = re.findall('(\w{1,})', s)
    names = [x.capitalize() for x in names]
    spaces = re.findall('(\s{1,})', s)
    spaces.append('')
    zip_list = list(zip(names, spaces))
    output = [''.join(tups) for tups in zip_list]
    return ''.join(output)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
