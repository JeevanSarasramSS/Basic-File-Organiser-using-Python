import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory not found!")
        return

    file_types = {
        'Images': ['.jpg', '.png', '.gif', '.jpeg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar']
    }

    for category, extensions in file_types.items():
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1].lower()
                if ext in extensions:
                    shutil.move(file_path, os.path.join(folder_path, file))

    print("Files organized successfully!")

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ")
    organize_files(folder)
