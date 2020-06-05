"""
bjective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
Explanation

Sample Case 1:
The binary representation of 5 is 101 , so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.


"""

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    max = 0
    val = 0
    while n > 0:
        if n % 2 != 0:
            val = val + 1
            if val > max:
                max = val
        if n % 2 == 0:
            val = 0
        n = n // 2

    print(max)    