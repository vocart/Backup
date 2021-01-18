import os
import shutil
import time
from os.path import join, getsize, isdir
from os import walk
from convert_locations_to_backup import locations_update
from actions import * # (action_get_size, action_concat_path)
# action_remove, action_compare_if_locations_are_equal, action_remove_and_copy, action_copy)


def backup_of_subfolders_update():

	for locations_source_and_destination in locations_update:

		path_source = get_key_from_dict(locations_source_and_destination)
	
		loc_dest = get_value_from_dict(locations_source_and_destination, locations_update)
		path_destination = add_value_to_list(loc_dest)

		if check_if_path_exists(path_source) is True and check_if_path_exists(path_destination) is True:
			list_of_folders_in_source = make_list_of_folders(path_source)
			list_of_folders_in_destination = make_list_of_folders(path_destination)
			
			# checks if folder from source is in backup folder
			compare_a_in_b(list_of_folders_in_source, list_of_folders_in_destination, locations_source_and_destination, loc_dest)

			# checks if folder from backup is already in source 
			# (in case there were forgotten old backups)
			compare_b_in_a(list_of_folders_in_destination, list_of_folders_in_source, loc_dest)
		else:
			print('Dysk {} lub {} nie jest podłączony.'.format(path_source, path_destination))
			pass
	
		

def get_key_from_dict(locations_source_and_destination):
	path_source = []  
	path_source.append(locations_source_and_destination)
	return path_source


def check_if_path_exists(location):
	a = action_make_disc_name(location)
	if a[0].isalpha():
		if action_check_if_the_disc_is_connected(location) is True:
			#print(action_make_disc_name(location), 'ten dysk jest')
			return True
		else:
			#print(action_make_disc_name(location), 'nie ma tego dysku')
			return False
	else:
		return True
	

def get_value_from_dict(locations_source_and_destination, locations_update):
	loc_dest=locations_update[locations_source_and_destination]
	return loc_dest


def add_value_to_list(loc_dest):
	path_destination = [] 
	path_destination.append(loc_dest)
	return path_destination


def make_list_of_folders(location):

	list_of_folders = []
	for folder in location:
		if action_check_if_directory_exists(folder) is True:
			make_list_of_subfolders(folder, list_of_folders)
			#print (list_of_folders, 'lista folderów w {}'.format(location))
		else:
			print('There is no directory {}. Creating the directory.'.format(folder))
			pass

	return list_of_folders


def make_location(location_to_make):
	os.makedirs(location_to_make)
	return location_to_make


def make_list_of_subfolders(location, list_to_fill):
	listed_folders = os.listdir(location)
	for directory in listed_folders:
		list_to_fill.append(directory)
	return list_to_fill


def compare_a_in_b(location_a, location_b, path_source, loc_dest):
	for folder in location_a:
		if folder in ignored_list:
			action_ignore(folder)
		else:
			if folder in location_b:
				if (action_compare_if_locations_are_equal(folder, path_source, loc_dest)) is True:
					pass
					#print('Folder   {}   have the same size, it won\'t be copied.'.format(folder))  ########
				else:
					print('Folder   {}   have different sizes, old folder deleted, new copied.'.format(folder))
					action_remove_tree_and_wait(folder, loc_dest)
					try:
						action_copy_tree(folder, path_source, loc_dest)
					except FileExistsError:
						time.sleep(7)
						action_copy_tree(folder, path_source, loc_dest)
			else:
				print('Folder   {}   not in backup yet, copying.'.format(folder))
				action_copy_tree(folder, path_source, loc_dest) 
	print('A in B completed')

 
def compare_b_in_a(location_a, location_b, loc_dest):  # a=destination!
	#print(loc_dest, 'loc_dest', location_a, 'location_a')
	for folder in location_a:
		if folder in ignored_list:
			action_ignore(folder)
			print('{} on ingnored list'.format(folder))
		else:
			if action_check_if_the_disc_is_connected(loc_dest) is True:
				#print('Dysk jest podłączony ')
				if folder in location_b:
					#print('{} b in a, pass'.format(folder))
					pass
				else:
					print('Folder   {}   in backup but not in source, \
		removing from backup.'.format(folder))
					action_remove_tree_and_wait(folder, loc_dest)
			else:
				print('Dysk nie podłączony - {}'.format(folder))
				pass
	print('B in A completed')
