import re

def mac_regex(filename):


	valid_macs_dict = dict()
	pattern = r'\s((?:[A-F0-9]{2}:){5}(?:[A-F0-9]{2}))\s'
	with open(filename, 'r') as file:
		for line_num, line in enumerate(file):
			if line_num == 0:
				continue
			if re.search(pattern, line):
				server = line[0:3]
				valid_mac = re.search(pattern, line)
				valid_macs_dict[server] = valid_macs_dict.get(server, valid_mac.group(1))
		
		return valid_macs_dict


print(mac_regex('data.txt'))
