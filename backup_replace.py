import shutil
import os
import os.path
import time
from os import walk
from os.path import join, getsize, isdir
from backup_locations import locations_copy_replace
from actions import * # (action_get_path, action_simple_copy,
						# action_check_direcory, action_get_size)


# makes iteration through 'locations_copy_replace' with 'copy_replace()' function
def make_copy_replace():
	# 'locations_copy_replace' from 'backup_locations_2'
	for loc_source in locations_copy_replace: 
		copy_replace(loc_source)


# makes backup by updating old files
def copy_replace(loc_source):
	# loc_source = klucz, loc_dest = wartość tego klucza
	loc_dest = locations_copy_replace[loc_source]
	if not action_check_direcory(loc_dest):
		action_simple_copy(loc_source, loc_dest)
		print('COPYING:   "{}"   COMPLETED'.format(loc_source))
	else:
		if (action_get_size(loc_source)) == (action_get_size(loc_dest)):
			print('Files in   "{}"  have the same size, they won\'t \
				be copied.'.format(loc_dest))
		else:
			print('Files in   "{}"   have different size, the old file will be \
exchanged by a new one.'.format(loc_dest))
			shutil.rmtree(loc_dest)
			time.sleep(7)
			copy_replace(loc_source)
