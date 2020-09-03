import re


def find_active(filename):

	active_users = dict()

	with open(filename, 'r') as file:

		for linenum, line in enumerate(file):
			if linenum == 0:
				continue
			columns = line.split()
			if columns[1] == 'Yes':
				active_users[columns[0]] = 1

	return active_users


def find_numbers(filename):

	pattern = r'(\w*)@\w*\.\w+ (\(\d{3}\) \d{3}-\d{4})'
	active_users = find_active('active.txt')

	with open(filename, 'r') as file:

		for line in file:

			if re.search(pattern,line):
				match = re.search(pattern, line)

				username = match.group(1)
				phone_number = match.group(2)

				if username in active_users.keys():
					active_users[username] = phone_number
		
		for key, value in active_users.items():
			if value == 1:
				active_users[key] = '(444) 123-1233'


		for key, value in active_users.items():
			print('{} {}'.format(key, value))
	
	return active_users


find_numbers('contact.txt')

