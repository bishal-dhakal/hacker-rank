#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    minsum = 0
    maxsum = 0
    for i in arr:
        minsum = minsum + i

    minsum = minsum - arr[n-1]
    
    
    for i in arr:
        maxsum = maxsum + i 

    maxsum = maxsum - arr[0]

    print(f"{minsum} {maxsum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
