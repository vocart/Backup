from backup_copy import make_copy_new_version
from backup_replace import make_copy_replace
from backup_update import iteration_through_locations_update



print('\n \nSTART OF BACKUP. \n \n')
make_copy_new_version()
print('\n *** New backup copy was created. *** \n')

make_copy_replace()
print('\n *** Backup files were replaced by new ones. *** \n')

iteration_through_locations_update()
print('\n *** Backup files were checked and updated. *** \n')
print('\n \nBACKUP COMPLETED. \n \n')
