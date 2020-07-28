"""
Open the file and grab the percentage.
Strip away the % and turn into float to use for if condition.
Add server:percentage pair into dictionary.
return Dictionary

Complexity: O(N), for lines in logs
"""
def full_servers(filename):
	full_disk_dict = {}

	with open(filename, 'r') as file:
		for line in file:
			words = line.split()
			percentage = float(words[-1].rstrip('%'))
			print(percentage)
			if percentage > 85:
				full_disk_dict[words[0]] = words[-1]

	return full_disk_dict

print(full_servers("testdata.txt"))