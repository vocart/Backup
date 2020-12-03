import shutil
import time
from datetime import datetime
from os import walk
from os.path import join, getsize, isdir


def action_check_if_directory_exists(path):
	return isdir(path)


# Creates full path from path and end folder
def action_concat_path(loc, item):
	if item == None:
		return loc
	else:
		return '{}/{}'.format(loc, item)


# Returns name for folder with added todays date
def action_generate_todays_date():
	return datetime.now().strftime('%Y-%m-%d')


def action_copy_tree(item, loc_source, loc_dest):
	loc_a = action_concat_path(loc_source, item)
	loc_b = action_concat_path(loc_dest, item)
	try:
		shutil.copytree(loc_a, loc_b)
	except NotADirectoryError:
		pass


def action_compare_if_locations_are_equal(item, loc_source, loc_dest):
	loc_a = action_concat_path(loc_source, item)
	loc_b = action_concat_path(loc_dest, item)

	return action_get_size_of_path(loc_a) == action_get_size_of_path(loc_b)


def action_get_size_of_path(path):
	size = 0
	if not action_check_if_directory_exists(path):
		print(getsize(path))
	else:
		for root, dirs, files in walk(path):
			size += sum(getsize(join(root, name)) for name in files)
	# after adding sizes converts it into MB with 2 decimal places 
	return round(size / 1048576, 2) 


def action_remove_tree_and_wait(item, loc_dest):
	if item == None:
		location_to_remove = loc_dest
	else:
		location_to_remove = action_concat_path(loc_dest, item)
	try:
		shutil.rmtree(location_to_remove)
	except NotADirectoryError:
		pass
	time.sleep(7)
