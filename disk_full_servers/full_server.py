
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