import re
from datetime import datetime


def sort_by_date(file):
	file_date_dict = {}
	pattern = r"\w* \d+, \d{4}"
	with open(file, 'r') as file:
		for line in file:
			columns = line.split()
			date = re.search(pattern, line)
			print(line)
			file_date_dict[columns[-1]] = file_date_dict.get(columns[3], date.group(0))

	sorted_by_date_dict = sorted(file_date_dict.items(), key = lambda x:datetime.strptime(x[1], '%B %d, %Y'), reverse=True)

	return sorted_by_date_dict
	#below to print each one line by line.
	#for pair in sorted_by_date_dict:
		#print(pair)


sort_by_date('data.txt')


