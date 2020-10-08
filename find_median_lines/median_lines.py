"""
Pseudocode:
1) Iterate through file once to get number of lines.
2) If number of lines/2 = even then there will be 2 middle lines
	Sample 6/2 = 3 (the two middle lines = 3,4)
3) If number of lines/2 = odd then there will only only 1 median
	Sample 7/2 = 3.5 (round down and that's the middle line) = 3
4) Iterate through file once more to find that line number
5) Take note that in coding line starts at 0. 

Big O: O(2n) we have to iterate twice as file shouldn't fit in RAM
"""


def median_lines(filename):

	medianlines = list()

	with open(filename, 'r') as file:

		# first iteration to get totallines
		for totallines, line in enumerate(file):
			pass

		# returns to beginning of file for second iteration
		file.seek(0)
		median = int(totallines/2)
		if median % 2 == 0:
			secondmedian = median + 1
			for linenum, line in enumerate(file):
				if linenum == median or linenum == secondmedian:
					medianlines.append(line)
					print(line.rstrip())
					return medianlines
		else:
			for linenum, line in enumerate(file):
				if linenum == median:
					medianlines.append(line)
					print(line)
					return medianlines
		

median_lines('data.txt')