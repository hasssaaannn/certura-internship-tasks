# file_organizer.py
# Hassaan Ahmed - Certura Internship Task 2 (Shutil-free version)

import os

# Define file categories and their extensions
FILE_TYPES = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Videos": ['.mp4', '.avi', '.mov', '.mkv'],
    "Music": ['.mp3', '.wav', '.aac'],
    "Code": ['.py', '.cpp', '.java', '.html', '.js'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Others": []  # Will catch anything that doesn't match
}

# This function finds the correct category based on file extension
def get_file_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

# Main logic to organize the files
def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a folder
        if os.path.isfile(file_path):
            # Get file extension (e.g. .jpg, .pdf)
            _, ext = os.path.splitext(filename)

            # Find which folder/category it belongs to
            category = get_file_category(ext)

            # Create path for target folder (like "Images", "Documents")
            target_folder = os.path.join(directory, category)

            # If that folder doesn't exist, make it
            if not os.path.exists(target_folder):
                os.mkdir(target_folder)

            # Build new path and move the file
            new_path = os.path.join(target_folder, filename)
            os.rename(file_path, new_path)

    print("Files organized successfully using only os module!")


folder_path = input("Enter path of folder to organize:\n> ").strip()

if os.path.exists(folder_path):
    organize_files(folder_path)
else:
    print("Error: Folder not found.")
