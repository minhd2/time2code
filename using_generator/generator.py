# Thought Process: 
#	1) Use a function to create generator object for each line
#	2) Use separate for loop to get totalsum and count of objects
#	3) Get average
#	Runtime: o(n), number of lines.

def using_generator_average(filename):

	for row in open(filename, 'r'):
		yield row


totalsum = 0
counter = 0
genobjavg = using_generator_average('data.txt')

for row in genobjavg:
	totalsum += int(row)
	counter += 1

average = total/counter

print(average)


