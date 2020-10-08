# Thought process:
#	1) Put all items into a list and sort by PID
#	2) Go through list index and index+1, step 2 as we know it's an even number
#	3) Turn date/time into a datetime obj and find difference
#	4) Append to an ordereddict and return the ordereddict
#	Runtime: O(nlogn) due to sorting.


from datetime import datetime
from collections import OrderedDict


def clear_things(filename):

	totalfile = list()
	pidtimediff = OrderedDict()

	with open(filename, 'r') as file:

		for linenum, line in enumerate(file):
			if linenum == 0:
				continue
			columns = line.split()
			totalfile.append(columns)

		sortedfile = sorted(totalfile, key = lambda x:x[2])
	
	for index in range(0, len(sortedfile), 2):
		starttime = str(sortedfile[index][1]) + ' ' + str(sortedfile[index][0])
		endtime = str(sortedfile[index+1][1]) + ' ' +str(sortedfile[index+1][0])

		starttimeobj = datetime.strptime(starttime, '%m/%d/%Y %H:%M:%S')
		endtimeobj = datetime.strptime(endtime, '%m/%d/%Y %H:%M:%S')

		timedifference = endtimeobj - starttimeobj
		pidtimediff[sortedfile[index][2]] = str(timedifference)
		print(sortedfile[index][2], timedifference)

	print(pidtimediff)
	return pidtimediff





clear_things('data.txt')

