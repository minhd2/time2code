import os
import re
import shutil


def file_manipulation():

	htmlpattern = r'.+\.html'
	jpgpattern =  r'.+\.jpg'
	textpattern = r'.+\.txt'
	txtfiles = list()
	list_of_files = os.listdir('.')

	for file in list_of_files:

		if re.match(htmlpattern, file):
			htmlbase = os.path.splitext(file)[0]
			os.rename(file, htmlbase + '.htm')

		if re.match(jpgpattern, file):
			shutil.move(file, 'Pictures')

		if re.match(textpattern, file):
			txtfiles.append(file)

	txtfiles.sort()
	for files in txtfiles:
		with open(files, 'r') as txtfile: 
			with open('Stuff.txt', 'a+') as stuff:
				for line in txtfile:
					stuff.write(line)

				stuff.write('\n')



file_manipulation()