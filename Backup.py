import shutil
import os
import time
from os import walk
from os.path import join, getsize, isdir
from datetime import datetime


# list of locations to backup with their backup directories for copy_swap()
locations_copy_swap = {
	'E:/fotki pulpit': '//192.168.20.20/kopia pulpit/Zdjęcia z pulpitu',

	'C:/Users/Lech/Desktop/Programowanie': '//192.168.20.20/kopia pulpit/Programowanie',
	
	'C:/Zdjęcia do obróbki': '//192.168.20.20/kopia pulpit/Zdjęcia z pulpitu/Zdjęcia do obróbki',

	'H:/muza/GRAJEK': '//192.168.20.20/muzyka/GRAJEK',
	'H:/muza/REDMI': '//192.168.20.20/muzyka/REDMI',
	
	'H:/MOJE/Warhammer i gry': '//192.168.20.20/kopia pulpit/Warhammer i gry',
	'H:/MOJE/Zdjęcia': '//192.168.20.20/zdjęcia',
	'H:/MOJE/Muzyka/mp3': '//192.168.20.20/muzyka/mp3',

	'H:/MOJE/Różne/PRACA/FIRMA': '//192.168.20.20/kopia pulpit/PRACA/FIRMA',
	'H:/MOJE/Różne/PRACA/ARCHITEKTURA': '//192.168.20.20/kopia pulpit/PRACA/ARCHITEKTURA',
	'H:/MOJE/Różne/PRACA/CV': '//192.168.20.20/kopia pulpit/PRACA/CV',
	'H:/MOJE/Różne/PRACA/Pity': '//192.168.20.20/kopia pulpit/PRACA/Pity',

	'H:/MOJE/Różne/DOM': '//192.168.20.20/kopia pulpit/DOM',
	'H:/MOJE/Różne/PROGRAMY': '//192.168.20.20/kopia pulpit/PROGRAMY',
	'H:/MOJE/Różne/RESZTA': '//192.168.20.20/kopia pulpit/RESZTA',
	'H:/MOJE/Różne/ROZRYWKA': '//192.168.20.20/kopia pulpit/ROZRYWKA'
	}

# list of files to copy for copy_new_version()
locations_copy_new_version = (
	'H:/MOJE/figurki - aukcje, kasa.xls', 
	'H:/MOJE/obiektywy.xls',
	'H:/MOJE/figurki - spis 2020.xls',
	'H:/MOJE/waga.xls'
	)


# makes iteration through 'locations_copy_swap' with 'copy_swap()' function
def make_copy_swap():
	for loc_a in locations_copy_swap:
		copy_swap(loc_a)


# produces a new location for backup and then makes iteration through
# 'locations_copy_new_version' with 'copy_new_version()' function
def make_copy_new_version():
	global new_date_folder_name
	global backup_file_folder
	new_date_folder_name = 'Backup ' + datetime.now().strftime('%Y-%m-%d')
	backup_file_folder = '//192.168.20.20/kopia pulpit/WAŻNE PLIKI'

	try:
		os.mkdir('{}/{}'.format(backup_file_folder, new_date_folder_name))
	except FileExistsError:
		print('Location already exists.')

	for loc in locations_copy_new_version:
		copy_new_version(loc)


# makes backup by updating old files
def copy_swap(loc_a):  
	loc_b = locations_copy_swap[loc_a]
	try:
		shutil.copytree('{}'.format(loc_a), '{}'.format(loc_b))
	except FileExistsError:
		if (compare_size(loc_a)) == (compare_size(loc_b)):
			print('Files have the same size, they won\'t be copied.')
		else:
			print('Files have different size, the old file will be exchanged by a new one.')
			shutil.rmtree('{}'.format(loc_b))
			time.sleep(7)
			copy_swap(loc_a)


# makes backup by adding new version of files in a new folder
def copy_new_version(loc):  
	try:
		shutil.copy('{}'.format(loc), '{}/{}'.format(backup_file_folder, new_date_folder_name))
	except FileExistsError:
		print('The file already exists.')
		pass
	except FileNotFoundError:
		print('Can\' find the file: {}'.format(loc))
		pass
	

# Gets size of files/folders in MB
def compare_size(path):
	size = 0
	if not isdir(path):
		print(getsize(path))
	else:
		for root, dirs, files in walk(path):
			size += sum((getsize(join(root, name)) for name in files))
	return round(size / 1048576, 2)


make_copy_swap()

make_copy_new_version()
