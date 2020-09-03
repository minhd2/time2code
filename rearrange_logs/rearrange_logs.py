#I could have probably sorted the dictionaries for the stats_log.txt to look nicer.


def rearrange_logs(*args):

	getdict = dict()
	setdict = dict()
	adddict = dict()

	for logfile in args:
		with open(logfile, 'r') as file:
			for line in file:
				column = line.split()
				date = column[1]
				calltype = column[2]
				if calltype == 'Get':
					with open('get_log.txt', 'a+') as getlog:
						getlog.write(line)
						getdict[date] = getdict.get(date, 1) + 1
				elif calltype == 'Set':
					with open('set_log.txt', 'a+') as setlog:
						setlog.write(line)
						setdict[date] = setdict.get(date, 1) + 1
				else:
					with open('add_log.txt', 'a+') as addlog:
						addlog.write(line)
						adddict[date] = adddict.get(date, 1) + 1



	with open('stats_log.txt', 'a+') as stats:
		stats.write('Get')
		stats.write('\n')
		for date, totalcount in getdict.items():
			newlinestring = "{0} {1}".format(str(date), str(totalcount))
			stats.write(newlinestring)
			stats.write('\n')

		stats.write('Set')
		stats.write('\n')
		for date, totalcount in setdict.items():
			newlinestring = "{0} {1}".format(date, totalcount)
			stats.write(newlinestring)
			stats.write('\n')

		stats.write('Add')
		stats.write('\n')
		for date, totalcount in adddict.items():
			newlinestring = "{0} {1}".format(date, totalcount)
			stats.write(newlinestring)
			stats.write('\n')
				






rearrange_logs('data.txt')
