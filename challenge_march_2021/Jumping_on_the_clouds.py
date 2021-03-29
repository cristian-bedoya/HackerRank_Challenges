#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    n = len(c)
    i = 0
    step = 0
    
    if (n == 2 or n == 3):
        return 1

    while i < (n-1):
        if ( i== n-2 and c[-2] == 0 and c[-1]== 0):
            i += 1
            step +=1
        elif ( (not c[i+1] and not c[i+2]) or (c[i+1])):
            i += 2
            step +=1
        elif ( not c[i+1] and c[i+2]):
            i += 1
            step +=1
    
    return step
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
