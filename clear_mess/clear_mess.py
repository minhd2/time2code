import re


def clean_mess(filename):

	namepattern = r'[A-Za-z]+'
	datepattern = r'\d{2}\/\d{2}\/\d{4}'
	numberpattern = r'\d{3}-\d{3}-\d{4}'

	fixeddict = dict()

	with open(filename, 'r') as file, open('clean_mess.txt', 'a+') as newfile:

		newfile.write('Username Phone_num Start_date\n')

		for line in file:
			number = re.search(numberpattern, line).group()
			date = re.search(datepattern, line).group()
			name = re.search(namepattern, line).group()

			fixeddict[name] = [number, date]

		
		sorteddict = sorted(fixeddict.items())


		for item in sorteddict:
			newlineinput = '{} {} {}'.format(item[0], item[1][0], item[1][1])
			newfile.write(newlineinput)
			newfile.write('\n')

			

			


				



				

				#print(name, number ,date)



clean_mess('data.txt')