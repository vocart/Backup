import shutil
import os
import os.path
from convert_locations_to_backup import locations_copy_new_version
from Backup import backup_file_folder
from actions import *  # (action_concat_path, action_check_if_directory_exists)


# produces a new location for backup and then makes iteration through
# 'locations_copy_new_version' with 'copy_new_version()' function
def make_copy_new_version():
	new_date_folder_name = 'Backup ' + action_generate_todays_date()
	backup_directory_with_date = action_concat_path(backup_file_folder, new_date_folder_name)
	create_directory_if_not_exists(backup_directory_with_date)
	for loc in locations_copy_new_version:
		copy_new_version(loc, backup_directory_with_date)
	

# checks if the directory already exists, if not it creates it
def create_directory_if_not_exists(path):
	if not action_check_if_directory_exists(path):
		os.mkdir(path)
	else:
		pass


# checks if the file is available to copy and makes backup by 
# adding new version of files in a new folder
def copy_new_version(loc, backup_directory_with_date):
	isfile = os.path.isfile
	if isfile(loc):
		shutil.copy(loc, backup_directory_with_date)
		print('"{}"    copied.'.format(loc))
	else:
		print('Can\'t find the file:   {}'.format(loc))
