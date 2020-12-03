Backup - program for making different kinds of backup from indicated locations to a serwer. For manual launch once a month.

It enables for three kinds of backup:
- for important files creates a new folder and makes copies of files (don't delete old copies)
- for locations with frequent changes and smaller sizes it checks the size of whole location and if it's different it is deleted and replaced by the new copy
- for locations with occassional changes but many subfolders (like locations with mp3, films, archival photos) it checks the size of each folder in location and replaces only these with different sizes.
New paths can be added to a dictionary.

It consists of:
- Backup.py - initializing file - starts three kinds of backup (each in a different file)
- backup_locations.txt - it contains of three lists of copied locations, for each backup. Two lists have system of naming 'location_source':'location_destination' and the third is only a list of files to copy.
- actions.py - contains common actions for backup files
- convert_locations_to_backup.py - changes links from txt to dictionaries/list for files to use
- three backupping files, each makes different kind of backup: 
  - new version of files in a fresh folder with todays date
  - replacing old folders with new ones - checks if folders size changed, if not it doesn't take action, if it is different - the folder is removed and replaced by a new one
  - updating folders - checks each folder inside location if they differ from the already backupped version and replaces them if they do

v.4
- backup_locations changed from .py to .txt with 'normal' copied destinations rather than already changed to use by program
- convert_locations_to_backup.py added to convert destinations from txt to dictionaries/lists
- changes of names and simplyfiyng functions
 
v.3
Program divided for different roles - initialize, actions, locations and three kinds of backup.
Even more clean code.

v.2
File paths separated from main files to a different file.
Cleaner code:)
