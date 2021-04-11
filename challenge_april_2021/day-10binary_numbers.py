#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = bin(n)[2:]

    nmax = 0 
    npart = 0
    len1 = len(binary)
    i = 0
    while i < len1:
        if binary[i] == '1':
            npart += 1
            if i == len1 -1 and npart > nmax:
                nmax = npart
        else:
            if npart > nmax:
                nmax = npart
            npart = 0
        i += 1

        print(nmax)
