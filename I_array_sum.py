#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.   This will return the max sum from an "I" shape in a 2d array


def printHourglass(arr, x, y):
    # print (arr[x-1][y-1], arr[x-1][y], arr[x-1][y+1])
    # print (' ',arr[x][y])
    # print (arr[x+1][y-1], arr[x+1][y], arr[x+1][y+1])
    return arr[x-1][y-1] + arr[x-1][y] + arr[x-1][y+1] + arr[x][y] +\
        arr[x+1][y-1] + arr[x+1][y] + arr[x+1][y+1]


def hourglassSum(arr):
    width = len(arr[0])
    height = len(arr)

    my_sum = -99999999
    for i in range(1, width - 1):
        for j in range(1, height-1):
            # print(i, j, "-->", arr[i][j])
            tmp_sum = printHourglass(arr, i, j)
            my_sum = max(my_sum, tmp_sum)
    return my_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
