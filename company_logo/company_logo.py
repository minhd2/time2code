# Problem: https://www.hackerrank.com/challenges/most-commons/problem
# Copy and paste bottom will work into that problem.
# Thought Process:
#	1) Use dictionary to store char/occurences at kv pair
#	2) Sort in reverse by key first then normal by value
#	3) Print only first three items and their occurence count
# I struggled with finding how to do the sort on only one key and
# the reverse on the other, I had to look that up.
# Runtime: O(nlogn) due to sort.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    charoccurences = dict()
    for char in s:
        charoccurences[char] = charoccurences.get(char, 0) + 1
    
    sortoccurences = sorted(charoccurences.items(), key=lambda x:(-x[1], x[0]))

    for item in sortoccurences[:3]:
        print(item[0], item[1])
