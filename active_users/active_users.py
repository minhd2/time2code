"""
Pseudocode:
1) Go through active.txt to find all active users and add into a dictionary as key, value can be anything
2) Return that dictionary and use it's output in another function
3) Using Regex, go through each line in contact.txt
4) Separate username and phone number with regex grouping
5) Add number into a new dictionary with username as key
6) Go through dictionary once more to find all left over valued as 1 and change that to company number
7) Print and return dictionary

Data Structures:
1) Dictionary{username: ifActive=1}
2) Dcitionary{username: phonenumber}

Big O: O(n), n being the number of lines in a file
"""


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

