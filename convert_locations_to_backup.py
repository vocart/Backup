import os


links_list = []
def get_links_from_file(links_file_name):

    if os.path.isfile(links_file_name):
        
        with open(links_file_name, "r", encoding="utf8") as files_content:
                      
            for line in files_content:
                line = line.replace('\n','').replace('\r','').replace('\t','').replace('\\','/')
                if line == '':
                    pass
                else:
                    links_list.append(line)
                    
    else:
        print ("File with links:", links_file_name, "doesn't exist.")


locations_copy_replace = {}
locations_copy_new_version = []
locations_update = {}
def sort_links():
    mark2 = links_list.index('locations_copy_new_version:')
    mark3 = links_list.index('locations_update:')
    
    for link in links_list[1:mark2]:
        dictionary_link = link.split(' : ')
        locations_copy_replace[dictionary_link[0]] = dictionary_link[1]
        
    for link in links_list[mark2+1:mark3]:
        locations_copy_new_version.append(link)
        
    for link in links_list[mark3+1:]:
        dictionary_link = link.split(' : ')
        locations_update[dictionary_link[0]] = dictionary_link[1]


file_with_locations = 'backup_locations.txt'
get_links_from_file(file_with_locations)
sort_links()
