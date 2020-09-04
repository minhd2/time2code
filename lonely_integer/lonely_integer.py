# Problem is from:
# https://www.hackerrank.com/challenges/lonely-integer/problem
# Copy and paste directly into to finish
# Thought process:
# 1) Use a dictionary to track number of number occurences
# 2) Iterate through dictionary to find value == 1 (lonely number)
# 3) Return that key
# Runtime: O(n+m) --> O(n) due to iterating through array
# Input from question link, first input, a number for length
# of array. Second input for the numbers to be in array
# Below is the meat of the function from the HackerRank problem

def lonelyinteger(a):
    
    numtracker = dict()
    print(a)
    for num in a:
        numtracker[num] = numtracker.get(num, 0) + 1
    
    print(numtracker)
    for key, value in numtracker.items():
        if value == 1:
            return key