import shutil
import time
from datetime import datetime
from os import walk
from os.path import join, getsize
from os.path import isdir


# Gets size of files/folders in MB
def action_get_size(path):
	size = 0
	if not action_check_direcory(path):
		print(getsize(path))
	else:
		for root, dirs, files in walk(path):
			size += sum(getsize(join(root, name)) for name in files)
	# after adding sizes converts it into MB with 2 decimal places 
	return round(size / 1048576, 2) 


# Checks if the directory exists and returns True/False
def action_check_direcory(path):
	return isdir(path)


# Creates full path from path and end folder
def action_get_path(loc, item):
	return '{}/{}'.format(loc, item)


# Copies folder from one destination to another
def action_simple_copy(loc_source, loc_destination):
	shutil.copytree(loc_source, loc_destination)


# Returns name of folder with added todays date
def action_generate_todays_date():
	return datetime.now().strftime('%Y-%m-%d')


# Removes location after getting path to it
def action_remove(loc_dest, item):
	print('Folder   {}   in backup but not in source, \
		removing from backup.'.format(item))
	loc_b = action_get_path(loc_dest, item)
	try:
		shutil.rmtree(loc_b)
	except NotADirectoryError:
		pass


# Copies folders after creating their paths
def action_copy(item, loc_source, loc_dest):
	print('Folder   {}   not in backup yet, copying.'.format(item))
	loc_a = action_get_path(loc_source, item)
	loc_b = action_get_path(loc_dest, item)
	try:
		shutil.copytree(loc_a, loc_b)
	except NotADirectoryError:
		pass


# Compares sizes of folders after creating their paths
def action_compare_size(item, loc_source, loc_dest):
	loc_a = action_get_path(loc_source, item)
	loc_b = action_get_path(loc_dest, item)
	if action_get_size(loc_a) == action_get_size(loc_b):
		print('Folders   {}   have the same size, no action.'.format(item))
	# updates in backup if folders with the same names have different sizes
	else:
		print('Folders   {}   have different sizes, folder updated.'.format(item))
		action_remove_and_copy(loc_a, loc_b)


# Removes folder and replaces it with a new one
def action_remove_and_copy(loc_a, loc_b):
	print('Folder deleted and...')
	shutil.rmtree(loc_b)
	time.sleep(7)
	print('... copied a new one.')
	try:
		shutil.copytree(loc_a, loc_b)
	except NotADirectoryError:
		pass
