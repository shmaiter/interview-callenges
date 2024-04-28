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

    # final distances of each apple and orange, inside the range
    apples = [val for val in [a + apple for apple in apples]
              if val >= s and val <= t]
    oranges = [val for val in [b + orange for orange in oranges]
               if val >= s and val <= t]

    print(len(apples), len(oranges), sep='\n')


if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()

    # s = int(first_multiple_input[0])

    # t = int(first_multiple_input[1])

    # second_multiple_input = input().rstrip().split()

    # a = int(second_multiple_input[0])

    # b = int(second_multiple_input[1])

    # third_multiple_input = input().rstrip().split()

    # m = int(third_multiple_input[0])

    # n = int(third_multiple_input[1])

    # apples = list(map(int, input().rstrip().split()))

    # oranges = list(map(int, input().rstrip().split()))

    # countApplesAndOranges(s, t, a, b, apples, oranges)
    countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
