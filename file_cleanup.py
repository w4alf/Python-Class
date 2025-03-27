
#import the os module to work with files and directories
import os

#set paths for the original and destination folders
folder_original = 'C:/users/cbrav/Documents/'
folder_destination = 'C:/users/cbrav/Documents/Cleaned_Up/'

# makes a new directory if it does not exist
os.mkdir(folder_destination)    

# loop through the files in the original folder
# and move them to the destination folder
for entry in os.scandir(folder_original):
    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)
    # check if the entry is a file, we don't want to move directories
    if os.path.isfile(location_original):
        # move the file to the destination folder, rename can change the name of the file, but you can also use it to move files
        os.rename(location_original, location_destination)


