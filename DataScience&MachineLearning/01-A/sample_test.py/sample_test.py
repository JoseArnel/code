# 1. Array Subsets
# conditions, intersection A&B is null, union A&B is = to orginal, 
# subset A is minmal, sum of A > sum of B elements

# return subset in increaseing order where sum of A's > sum of B's
# if more than on subset, return one with maximal sum

# ex: n = 5, arr = [3,7,5,6,2]
# return: [6,7]

# psuedo 
# Go through entire set, keep interating, reverse, subtract then add
# once the vales > than sum them return
# interate through, set
# find max? 
# find second max

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def subsetA(arr):
    
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]
        
    a = []
    sum2 = 0
    for i in range(n-1, -1, -1):
        for j in range(len(a)):
            sum2 += a[j]
        sum = sum - arr[i]
        if sum2 < sum:
            a.append(arr[i])
        
    new = arr.sort()
    return (new, new)
        
if __name__ == '__main__':


    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# 2.Binary Number in a Linked list
# given a binary, linked list node. data = 
# return number from binary