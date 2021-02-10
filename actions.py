import shutil
import time
import os
from datetime import datetime
from os import walk
from os.path import join, getsize, isdir



ignored_list = ['@Recycle', 'Desktop.ini', 'Thumbs.db', 'desktop.ini', '_BAJKI', 
'spis filmów.xls', 'brakujące seriale.txt', 'braki serialowe 2020.12.xls']

def action_ignore(folder):
	#print('Item {} on ignored_list, won\'t be copied'.format(folder))
	pass


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

# Checks if the txt file exists (if not it creates it) and initiates function that adds a location to this txt
def add_to_disobedient_files(loc_b):
	if action_check_if_directory_exists('disobedient_files.txt') is True:
		action = 'a'
		action_open_txt_and_add_location(action, loc_b)
	else:
		action = 'w'
		action_open_txt_and_add_location(action, loc_b)


def action_copy_tree(item, loc_source, loc_dest):
	loc_a = action_concat_path(loc_source, item)
	loc_b = action_concat_path(loc_dest, item)
	if item in ignored_list:
		action_ignore()
	else:
		try:
			shutil.copytree(loc_a, loc_b)
		except NotADirectoryError:
			pass

		except PermissionError:
			add_to_disobedient_files(loc_b)
					
		except FileExistsError:
			add_to_disobedient_files(loc_b)
			print ('USUŃ   {}   I ZAPUŚĆ PONOWNIE BACKUP!'.format(loc_b))
			pass


def action_open_txt_and_add_location(action, location):
	with open('disobedient_files.txt', action) as plik:
		plik.write(location)
		plik.write("\n")


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
	elif item in ignored_list:
		action_ignore()
	else:
		location_to_remove = action_concat_path(loc_dest, item)
	try:
		shutil.rmtree(location_to_remove)
	except NotADirectoryError:
		print('Not a directory!!!!!!!!!!!!! ')
		pass
	except PermissionError:
		print ('NIE MOŻNA USUNĄĆ   {}   !!!!!!!!'.format(location_to_remove))
		action = 'a'
		action_open_txt_and_add_location(action, location_to_remove)
		pass
	time.sleep(7)


def print_files_to_remove_and_remove_temporary_file():
	if os.path.exists('disobedient_files.txt'):
		print('Te pliki należy usunąć z backupu ręcznie:')
		with open('disobedient_files.txt', 'r') as plik:
			for line in plik:
				print(line)
		os.remove('disobedient_files.txt')
	else:
		pass


def action_check_if_the_disc_is_connected(location):
	
	disc = action_make_disc_name(location)
	
	if disc == '//1':
		print('serwer, lokacja = TRUE')
		return True

	else:
		return isdir(disc)


def action_make_disc_name(location):
	if len(location) <2:
		disc = location[0][:3]
		#print(disc)
	else:
		disc = location[:3]
		#print(disc)

	return disc