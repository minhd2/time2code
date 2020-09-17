# Thought Process:
#	1) Using generator object to gather both files line by line
#	2) Check if file sizes are the same, if not return False
#	3) Iterate through each line for both files using zip()
#	4) If line is different, return False and print diff and linenum
#	5) Return True is all goes through
#	Big O: O(n)

import os


def compare_large_files(file1, file2):

	file1gen = (row for row in open(file1))
	file2gen = (row for row in open(file2))

	file1size = os.stat(file1).st_size
	file2size = os.stat(file2).st_size

	if file1size != file2size:
		return False

	for linenum, (a,b) in enumerate(zip(file1gen, file2gen), 1):

		if a != b:
			print('Diff at line {}'.format(linenum))
			print('-'*15)
			print(a)
			print(b)
			print('-'*15)
			return False
		
	return True


print(compare_large_files('file1.txt', 'file2.txt'))