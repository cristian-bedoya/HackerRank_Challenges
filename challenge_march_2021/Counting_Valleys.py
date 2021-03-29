#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    level_see = 0
    valley = 0
    step = 0
    while step < steps:
        if path[step] == 'D' and level_see == 0:
            for stp in range(step, steps):
                if path[stp] == "U":
                    level_see += 1
                    step += 1
                if path[stp] == "D":
                    level_see -= 1
                    step += 1
                if path[stp] == "U" and level_see == 0:
                    valley += 1
                    break

        elif path[step] == "U":
                    level_see += 1
                    step += 1
        elif path[step] == "D":
                    level_see -= 1
                    step += 1
    
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
