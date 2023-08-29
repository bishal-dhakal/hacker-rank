#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    a=0
    for i in range(p,q+1):
        d = len(str(i))
        ps = i*i
        ps = str(ps)
        
        r = ps[-d:]
        l = ps[:len(ps)-d]
        
        l = int(l) if l != "" else 0
        r = int(r) if r != "" else 0
        if l+r == i:
            if i:
                print(i , end=' ')
            a = 1
    if a:
        pass
    else:
        print('INVALID RANGE')
                
                
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
