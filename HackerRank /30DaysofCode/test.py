#!/bin/ python3

import math
import os
import random
import re
import sys

def bitwiseAnd(N, K):
    # Write your code here
    # range(start index, stop index, step) 
    max = 0
    for x in range(N-1, 0, -1):
        for y in range(N, 1, -1):
            if (x == y):
                continue
            andd = x & y
            if (andd == 0):
                y += 1
            if (andd == K - 1):
                return(andd)
            if (andd < K and andd > max):
                max = andd
    return (max)
        


def bitwiseAnd(N, K):
    # Write your code here
    # range(start index, stop index, step) 
    max = 0
    yrange = 2
    for x in range(1, N):
        for y in range(yrange, N+1):
            if (x == y): 
                continue
            A = format(x, "b")
            B = format(y, "b")
            andd = x & y
            print ("A = " + str(int(A,2)) + ",B = " + str(int(B,2)) + "; A & B = " + str(andd))
            if (andd < K and andd > max):
                max = andd
            if (andd == 0):
                y += 1
        yrange += 1
    print(max)
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)



    #     fptr.write(str(res) + '\n')

    # fptr.close()