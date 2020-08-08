import re

def find_US_numbers(filename):

	pattern = re.compile(r"(?:[0-9]{3}-){2}[0-9]{4}\b|(?:[0-9]{3}\.){2}[0-9]{4}\b|(?:[0-9]{3} ){2}[0-9]{4}\b|(?:\([0-9]{3}\) [0-9]{3}(?: |-)[0-9]{4})")
	valid_num_dict = dict()

	with open(filename, 'r') as file:
		for line in file:
			columns = line.split()
			if re.search(pattern, line):
				m = re.search(pattern, line)
				valid_num_dict[columns[0]] = m.group(0)

	return(valid_num_dict)



print(find_US_numbers("data.txt"))