import shutil
import os
import os.path
from os.path import isdir
from backup_locations import locations_copy_new_version
from actions import * # (action_get_path, action_check_direcory)



# produces a new location for backup and then makes iteration through
# 'locations_copy_new_version' with 'copy_new_version()' function
def make_copy_new_version():
	global isDir
	new_date_folder_name = 'Backup ' + action_generate_todays_date()
	backup_file_folder = '//192.168.20.20/kopia pulpit/WAŻNE PLIKI'
	isDir = action_get_path(backup_file_folder, new_date_folder_name)
	check_directory(isDir)
	for loc in locations_copy_new_version:
		copy_new_version(loc)
	

# checks if the directory already exists, if not it creates it
def check_directory(path):
	if not action_check_direcory(path):
		os.mkdir(path)
	else:
		print('Location   {}   already exists.'.format(path))


# checks if the file is available to copy and makes backup by 
# adding new version of files in a new folder
def copy_new_version(loc):
	isfile = os.path.isfile
	if isfile(loc):
		shutil.copy(loc, isDir)
		print('COPYING:   "{}"    COMPLETED'.format(loc))
	else:
		print('Can\'t find the file:   {}'.format(loc))
		pass
