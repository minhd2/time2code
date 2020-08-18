# Current runtime is O(MxN) I believe. This could probably just be changed to O(n)
# if I used a dictionary instead for O(1) look up time.

import re

def random_password(filename):
	distinct_password = list()
	pattern = r'^((?:[a-z0-9]{4}-){2}[a-z0-9]{4})$'

	with open(filename, 'r') as file:
		for line in file:

			if re.search(pattern, line):
				match = re.search(pattern, line)
				if match.group(1) in distinct_password:
					distinct_password.remove(match.group(1))
					continue
				else:
					distinct_password.append(match.group(1))

	return distinct_password



print(random_password('data.txt'))




