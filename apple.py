#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    
    # acounter = 0
    # ocounter = 0
     
    # alist = [a + x for x in apples]
    # if any(s<=x<=t for x in alist):
    #     acounter += 1 
    # print(acounter)
 
    # olist = [b + x for x in oranges]
    # if any(s<=x<=t for x in olist):
    #     ocounter += 1 
    # print(ocounter)

    acount = ocount = 0

    for i in range(len(apples)):
        if(s <= a+apples[i]) <= t:
            acount += 1

    for i in range(len(oranges)):
        if(s <= a+oranges[i]) <= t:
            ocount += 1

    print(acount)
    print(ocount)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, apples)
