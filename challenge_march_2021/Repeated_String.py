#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    length = len(s)
    
    if (length == 1 and s == "a"):
        return n
    

    ocurrences = 0
    for letter in s:
        if letter == 'a':
            ocurrences += 1
    
    ocurrences = ocurrences * (int(n/length))
    
    module = n % length
    if (module != 0):
        for letter in s[:module]:
            if letter == 'a':
                ocurrences += 1

    return ocurrences

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
