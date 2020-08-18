import re


def validate_email(filename):

	valid_emails = list()
	pattern = r'\s([A-Za-z0-9]+[A-Za-z0-9-]+-?@[A-Za-z]*\.(?:net|com|edu|gov))'

	with open(filename, 'r') as file:
		for line_num, line in enumerate(file):
			if line_num == 0:
				continue
			if re.search(pattern, line):
				match = re.search(pattern, line)
				valid_emails.append(match.group(1))
	
	return valid_emails


print(validate_email('data.txt'))