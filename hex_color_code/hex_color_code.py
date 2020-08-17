import re


def hex_color_code(filename):\
	#this regex will ensure that the match isn't in beginning of line.
	pattern = r'(?<!^)#(?:[A-Fa-f0-9]+){3,6}'
	hex_list = list()
	with open(filename, 'r') as file:
		for line in file:
			matches = re.findall(pattern, line)
			if len(matches) >= 1:
				#break list if multiple are found in single line.
				for item in matches:
					hex_list.append(item)
	return hex_list


print(hex_color_code('data.txt'))


