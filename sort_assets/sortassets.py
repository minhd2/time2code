

from datetime import datetime


def sort_assets(filename):

	listoflines = list()
	assetcount = 1
	with open(filename, 'r') as file, open('sortedassets.txt', 'a+') as newfile:
		for linenumber, line in enumerate(file):
			if linenumber == 0:
				newheader = 'Asset# {}'.format(line)
				newfile.write(newheader)
				continue
			listoflines.append(line.split())


		sortedlines = sorted(listoflines, key = lambda x:(x[0], datetime.strptime(x[1], '%m/%d/%Y')))

		for line in sortedlines:

			line.insert(0, str(assetcount).zfill(6))
			newfile.write(' '.join(line))
			newfile.write('\n')
			assetcount += 1


sort_assets('data.txt')