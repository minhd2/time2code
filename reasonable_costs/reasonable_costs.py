# Thought Process:
#	1) Iterate every item, split by column
#	2) turn cost into float
#	3) Conditional statement on 'Recommended' Yes and 'Cost' < 50
#	4) Add into a list of tuples
#	5) Used datetime to turn into datetime object and sort
#	6) Output
# Runtime: O(nlogn) because of the sort.



from datetime import datetime


def find_good_food(filename):

	goodcosts = list()

	with open(filename, 'r') as file:

		for linenum, line in enumerate(file):
			if linenum == 0:
				continue
			column = line.split()
			cost = float(column[2].lstrip('$'))
			if column[-1] == 'Yes' and cost < 50:
				goodcosts.append((column[0], column[1], column[2], column[3]))


		sortgoodcosts = sorted(goodcosts, key=lambda x:datetime.strptime(x[0], '%m/%d/%y'))

		for item in sortgoodcosts:
			print('{} {} {} {}'.format(item[0], item[1], item[2], item[3]))

		return sortgoodcosts

find_good_food('data.txt')