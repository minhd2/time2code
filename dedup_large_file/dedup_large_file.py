# Thought Process:
#	1) Using an OrderedDict() go through each line and add as key
#	2) For each item in key, append to new file, overwriting new file if
#		it exists already or create it if not.

from collections import OrderedDict


def dedup_large_file(filename):

	unique_lines = OrderedDict()

	with open(filename, 'r') as file, open('deduptext.txt', 'w+') as newfile:

		for line in file:
			unique_lines[line] = 1


		for item in unique_lines.keys():
			newfile.write(item)


dedup_large_file('data.txt')