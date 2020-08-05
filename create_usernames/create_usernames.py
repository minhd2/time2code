"""Using readlines isn't that great because it'll load everything into memory, if it is a big file.
Instead I could've used 

from itertools import islice
	for line in islice(file, 1, None)

Definitely struggled doing this a bit. Had to think about how I was goign to check if a user name had
already excited or not.
This script is quite long and can be broken down into two separate functions.
I could've created another function to check if username is already in a dictionary and return the new username

"""

def create_usernames(filename):
	username_exist_dict = {}

	with open(filename, 'r') as file, open('newdata.txt', 'w') as newfile:
		for linenumber, line in enumerate(file):
			if linenumber == 0:
				headerwords = line.split()
				headerwords.append("Username")
				newfile.write(' '.join(headerwords))
				newfile.write('\n')
				continue

			words = line.split()
			firstinitial = words[0][0]
			lastname = words[1]
			username = firstinitial.lower() + lastname.lower()

			if username in username_exist_dict:
				a = True
				counter = 1
				while a:
					newusername = username + str(counter)
					if newusername not in username_exist_dict:
						username_exist_dict[newusername] = 1
						words.append(newusername)
						newfile.write(' '.join(words))
						newfile.write('\n')
						a = False
					counter += 1
				continue
			username_exist_dict[username] = 1
			words.append(username)
			newfile.write(' '.join(words))
			newfile.write('\n')


print(create_usernames('data.txt'))