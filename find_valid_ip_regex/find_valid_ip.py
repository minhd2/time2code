import re

def find_valid_ip(filename):
	valid_ip = []

	pattern = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}"
	r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$")

	with open(filename, 'r') as file:
		for line in file:
			if re.match(pattern, line):
				valid_ip.append(line.rstrip("\n"))

	print(valid_ip)


find_valid_ip('data.txt')