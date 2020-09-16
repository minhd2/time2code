# Thought Process:
# 1) List all files in listed directory
# 2) Print current directory
# 3) Go through all files and check size, if under 3KB remove.
# 4) Also add to list for removed items.
# 5) Print removed items
# Additional Thoughts:
# This will only work nicely if the directory only has files, it may work
# with subdirectories
# os.walk might be a better choice for this.
# Big O: O(n) n being the number of files in a directory.

import os

def remove_small_files(filename):

	removed_files = list()

	all_files = os.listdir(filename)
	sorted(all_files)

	root_path = os.path.relpath(filename)
	print(root_path+ '/')

	os.chdir(filename)
	print("Directory changed to " +filename)
	
	for file in all_files:
		filesize = os.path.getsize(file)
		kbfilesize = filesize/1000
		print('{} {} KB'.format(file, kbfilesize))
		if kbfilesize < 3:
			os.remove(file)
			removed_files.append(file)

	for file in removed_files:
		print(file + ' removed!')





remove_small_files('test_dir')

