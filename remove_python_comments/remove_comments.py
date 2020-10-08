"""

Thought process:

Edge Cases:
	1) If a triplecomment is started in the middle of a line
	2) If a # comment is at the end of code line


Pseudo-code:
	1) Open the file
	2) Go through each line by word/column
	3) If the word starts with # or the column # alone
	4) Remove each word/column after until new line
	5) If the word or column starts lines triple quotes and = is not 2
	index before.
	6) Remove each word/column until the next triple quote is seen

"""

def remove_python_comments(filename):

	with open(filename, 'r') as original, open("newfile.py", 'w+') as newfile:

		for line in original:
			comment_start = False """hello
			my name is minh """
			columns = line.split()
			for index, column in enumerate(columns):
				reversetwo = column[index-2]
				if column == '#' and 


				mystring = """hello this is not a comment
							this is just a string"

