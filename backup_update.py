import os
import shutil
import time
from os.path import join, getsize, isdir
from os import walk
from backup_locations import locations_update
from actions import * # (action_check_direcory, action_get_size, action_get_path)
# action_remove, action_compare_size, action_remove_and_copy, action_copy)

def iteration_through_locations_update():
	# adds all locations from locations_update to: list_source - keys
	# and to list_destination - values
	# makes iteration through 'locations_update' dictionary
	global loc_source
	for loc_source in locations_update:
		
		# loc_source = C:/Users/Lech/Desktop/folder C test
		list_source = []  # list to capture loc_source key
		list_destination = []  # list to capture loc_dest value
		
		global loc_dest         
		loc_dest = locations_update[loc_source]
		
		list_source.append(loc_source)
		list_destination.append(loc_dest)

		global list_of_locations
		list_of_locations = []

		global list_of_fold
		list_of_fold = []
		# list of folders in a source
		make_list_of_folders(list_source)  

		list_of_folders_source = list_of_fold
		
		list_of_locations = []  # fresh list
		list_of_fold = []  # fresh list
		# list of folders in a destination
		make_list_of_folders(list_destination)  

		global list_of_folders_destination
		list_of_folders_destination = list_of_fold
		
		# checks if folder from source is in backup folder
		compare_a_in_b(list_of_folders_source, list_of_folders_destination)

		# checks if folder from backup is already in source 
		# (in case there were forgotten old backups)
		compare_b_in_a(list_of_folders_destination, list_of_folders_source)

	print('\n *** End of backup ***')


# creates list of folders from given 'location' (like list_source),
# initiates make_list_of_locations
def make_list_of_folders(location):
	for folder in location:
		list_of_folders = os.listdir(folder)
		for a in list_of_folders:
			list_of_fold.append(a)

		make_list_of_locations(list_of_folders, folder)
                

# creates list of paths from given list of folders on list, creates list_of_locations
def make_list_of_locations(list_of_folders, folder):
	for loc in list_of_folders:
		source = action_get_path(folder, loc)
		list_of_locations.append(source)


def compare_a_in_b(location_a, location_b):
	for item in location_a:
		if item in location_b:
			action_compare_size(item, loc_source, loc_dest)
		else:
			action_copy(item, loc_source, loc_dest) 

 
def compare_b_in_a(location_a, location_b):
	for item in location_a:
		if item in location_b:
			pass
		else:
			action_remove(loc_dest, item)
