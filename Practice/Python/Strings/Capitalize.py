#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    output = ''
    for i in range(0,len(s)):
        if(s[i - 1] == ' ' or i == 0):
            output += s[i].capitalize()
        else:
            output += s[i]
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
