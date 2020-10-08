import os
import shutil

def combine_directory(dir1, dir2):

	os.rename(dir1, 'newdir')
	dir2dict = dict()

	for root, subdir, files in os.walk(dir2):
		print(root)
		print(subdir)
		print(files)
		for filename in files:
			print(filename)







combine_directory('dir1', 'dir2')