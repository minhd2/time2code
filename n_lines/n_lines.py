

def tailv1(filename, number_of_lines):
	
	totallines = 0

	#edge case of entering 0
	if number_of_lines == 0:
		print(' ')
	
	with open(filename, 'r') as file:
		for line in file:
			totallines += 1

		if number_of_lines >= totallines:
			print(file.read())

	with open(filename, 'r') as file:
		for currentline, line in enumerate(file, start=0):
			difference = totallines - currentline
			if difference <= number_of_lines:
				print(line)

tailv1('data.txt', 11)

def tailv2(filename, number_of_lines):

	with open(filename, 'r') as f:
		linelist = f.readlines()
		totallines = len(linelist)
		print(totallines)

		if totallines <= number_of_lines:
			print(f.read())

		negativelinesindex = number_of_lines - (number_of_lines*2)

		for line in linelist[negativelinesindex::]:
			print(line.rstrip('\n'))



tailv2('data.txt', 11)


