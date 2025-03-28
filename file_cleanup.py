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

def organize_folder():
    # Folder path to organize
    folder_path = 'C:/Users/cbrav/Documents/'
    
    # List all files (ignoring directories) in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        file_ext = os.path.splitext(file)[1].lower()
        
        # Determine the appropriate category
        target_category = "Others"
        for category, extensions in CATEGORIES.items():
            if file_ext in extensions:
                target_category = category
                break
        
        # Create the category folder if it doesn't exist
        target_folder = os.path.join(folder_path, target_category)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        # Move the file to the category folder
        shutil.move(file_path, os.path.join(target_folder, file))
    
    print("Files in '{}' organized successfully!".format(folder_path))
#
#if __name__ == "__main__":
organize_folder()