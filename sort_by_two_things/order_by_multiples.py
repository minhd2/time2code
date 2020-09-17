# Thought process:
# I know lambda functions are powerful and very versatile
# Using this, I took only the first index as the main sort
# Then I turned the rest into an integer so they can be the second
# source of sort
# BigO: O(nlogn) per sorted function.

mylist = ['a1', 'b20', 'c1', 'd5', 'a3', 'b1', 'd11', 'b3']

def sortbytwothings(alist):


	print(sorted(alist, key = lambda x:(x[0],int(x[1::]))))



sortbytwothings(mylist)