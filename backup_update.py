import os
import shutil
import time
from os.path import join, getsize, isdir
from os import walk
from convert_locations_to_backup import locations_update
from actions import *  # (action_get_size, action_concat_path)
# action_remove, action_compare_if_locations_are_equal, action_remove_and_copy, action_copy)


def backup_of_subfolders_update():

	for locations_source_and_destination in locations_update:

		path_source = get_key_from_dict(locations_source_and_destination)
		loc_dest = get_value_from_dict(locations_source_and_destination, locations_update)
		path_destination = add_value_to_list(loc_dest)

		list_of_folders_in_source = make_list_of_folders(path_source)
		list_of_folders_in_destination = make_list_of_folders(path_destination)
		
		# checks if folder from source is in backup folder
		compare_a_in_b(list_of_folders_in_source, list_of_folders_in_destination, locations_source_and_destination, loc_dest)

		# checks if folder from backup is already in source 
		# (in case there were forgotten old backups)
		compare_b_in_a(list_of_folders_in_destination, list_of_folders_in_source, loc_dest)


def get_key_from_dict(locations_source_and_destination):
	path_source = []  
	path_source.append(locations_source_and_destination)  # czy to jest na pewno locaton_sour....?
	return path_source


def get_value_from_dict(locations_source_and_destination, locations_update):
	loc_dest = locations_update[locations_source_and_destination]
	return loc_dest


def add_value_to_list(loc_dest):
	path_destination = [] 
	path_destination.append(loc_dest)
	return path_destination


def make_list_of_folders(location):
	list_of_subfolders = []
	for folder in location:
		listed_folders = os.listdir(folder)
		for directory in listed_folders:
			list_of_subfolders.append(directory)
	return list_of_subfolders


def compare_a_in_b(location_a, location_b, path_source, loc_dest):
	for folder in location_a:
		if folder in location_b:
			if (action_compare_if_locations_are_equal(folder, path_source, loc_dest)) is True:
				print('Folder   {}   have the same size, it won\'t be copied.'.format(folder))
			else:
				print('Folder   {}   have different sizes, old folder deleted, new copied.'.format(folder))
				action_remove_tree_and_wait(folder, loc_dest)
				action_copy_tree(folder, path_source, loc_dest)

		else:
			print('Folder   {}   not in backup yet, copying.'.format(folder))
			action_copy_tree(folder, path_source, loc_dest) 


def compare_b_in_a(location_a, location_b, loc_dest):
	for folder in location_a:
		if folder in location_b:
			pass
		else:
			print('Folder   {}   in backup but not in source, \
removing from backup.'.format(folder))
			action_remove_tree_and_wait(folder, loc_dest)
