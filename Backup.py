import shutil
import os
import time
from backup_locations import *
from os import walk
from os.path import join, getsize, isdir
from datetime import datetime


# makes iteration through 'locations_copy_replace' with 'copy_replace()' function
def make_copy_replace():
	for loc_source in locations_copy_replace:
		copy_replace(loc_source)


# makes backup by updating old files
def copy_replace(loc_source):
	loc_dest = locations_copy_replace[loc_source]  # loc_source = klucz, loc_dest = wartość tego klucza,
	if not isdir(loc_dest):
		shutil.copytree(loc_source, loc_dest)
	else:
		if (get_size(loc_source)) == (get_size(loc_dest)):
			print('Files have the same size, they won\'t be copied.')
		else:
			print('Files have different size, the old file will be exchanged by a new one.')
			shutil.rmtree(loc_dest)
			time.sleep(7)
			copy_replace(loc_source)


# Gets size of files/folders in MB
def get_size(path):
	size = 0
	if not isdir(path):
		print(getsize(path))
	else:
		for root, dirs, files in walk(path):
			size += sum((getsize(join(root, name)) for name in files))
	return round(size / 1048576, 2) # po przeliczeniu na MB zaokrągla wielkość do 2 miejsc po przecinku
									# (odpowiednie zaokrąglenie do porównywania)


# produces a new location for backup and then makes iteration through
# 'locations_copy_new_version' with 'copy_new_version()' function
def make_copy_new_version():
	global isDir
	new_date_folder_name = 'Backup ' + datetime.now().strftime('%Y-%m-%d')
	backup_file_folder = '//192.168.20.20/kopia pulpit/WAŻNE PLIKI'
	isDir = '{}/{}'.format(backup_file_folder, new_date_folder_name)
	if not isdir(isDir):
		os.mkdir(isDir)
	else:
		print('Location already exists.')
	for loc in locations_copy_new_version:
		copy_new_version(loc)


# makes backup by adding new version of files in a new folder
def copy_new_version(loc):
	if isdir(loc):
		if not isdir(isDir):
			shutil.copy(loc, isDir)
		else:
			print('The file already exists.')
			pass
	else:
		print('Can\' find the file: {}'.format(loc))
		pass


make_copy_replace()

make_copy_new_version()
