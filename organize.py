import os
import shutil

# Define the categories and their associated file extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".cs", ".rb"],
    "Executables": [".exe", ".bat", ".sh", ".app"],
    "Others": []
}

def organize_desktop():
    desktop_path = 'C:/Users/cbrav/Documents'  # Get the desktop path
    print("printing desktop path", desktop_path)
      

    # Get all the files on the desktop
    files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]
    
    # Loop through each file and move it to the appropriate folder
    for file in files:
        # Get the file path and extension
        file_path = os.path.join(desktop_path, file)

        # Get the file extension by splitting the file name and getting the last part
        # of the split string, then convert it to lowercase
        file_ext = os.path.splitext(file)[1].lower()
        
        # Find the appropriate category for the file
        folder_name = "Others"

        # Loop through the categories and check if the file extension matches
        # any of the extensions in the category
        # If it does, set the folder name to the category
        # and break out of the loop
        for category, extensions in CATEGORIES.items():
            if file_ext in extensions:
                folder_name = category
                break
        
        #if folder does not exist, create it
        folder_path = os.path.join(desktop_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        #move the file to the folder
        #
        # The shutil.move() function moves the file from the original location to the new location    
        shutil.move(file_path, os.path.join(folder_path, file))
    
    print("Desktop organized successfully!")

if __name__ == "__main__":
    organize_desktop()
