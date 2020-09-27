"""
Pseudocode:
1) Take in a file and column number (for sort key)
2) Open file
3) Check length of first row (for error checking)
4) Create a list of lists with row being an item
5) Check length of list and column given, raise error if out of range
6) Try to sort the list, if it can't be sort then the number inputted is not numeric
7) Raise error if not numeric
8) return sorted_list

"""

# n = column to sort by
def my_sort(filename, n):

	wanted_index = n-1
	columns_list = list()
	sorted_list = list()

	with open(filename, 'r') as file:

		for line in file:
			columns_list.append(line.split())

		# check column length to inputted column
		if n > len(columns_list[0]) or n < 0:
			raise IndexError("Column inputted out of range, please try again")
		else:
			try:
				# sort by wanted_index (n - 1)
				sorted_list = sorted(columns_list, key=lambda x:int(x[wanted_index]))
				# join and print rows in sorted order and return sorted_list for ability to unittest
				for row in sorted_list:
					print(' '.join(row))
				return sorted_list
			except ValueError:
				print("Column selected is not numeric, please try again")


my_sort('data.txt', 3)
