import shutil
import os
import os.path
import time
from os import walk
from os.path import join, getsize, isdir
from convert_locations_to_backup import locations_copy_replace
from actions import * # (action_get_path, action_copy_tree, action_compare_if_locations_are_equal
						# action_check_if_directory_exists, action_get_size)


def iteration_through_locations_with_backup_replace():
	# 'locations_copy_replace' from 'convert_locations_to_backup'
	for loc_source in locations_copy_replace: 
		make_copy_replace(loc_source)


# makes backup by updating old files
def make_copy_replace(loc_source):
	# loc_source = key, loc_dest = key's value
	loc_dest = locations_copy_replace[loc_source]
	if not action_check_if_directory_exists(loc_dest):
		print('Folder   {}   not in backup yet, copying.'.format(loc_dest))
		action_copy_tree(None, loc_source, loc_dest)
	else:
		if action_compare_if_locations_are_equal(None, loc_source, loc_dest) is True:
			print('Files in   "{}"  have the same size, they won\'t \
be copied.'.format(loc_dest))
		else:
			print('Files in   "{}"   have different size, the old file will be \
exchanged by a new one.'.format(loc_dest))
			action_remove_tree_and_wait(None, loc_dest)
			make_copy_replace(loc_source)

