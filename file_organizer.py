import os
import shutil

def organize_files_by_extension(directory_path):
    if not os.path.exists(directory_path):
        print("Directory does not exist.")
        return

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                _, file_extension = os.path.splitext(file)
                file_extension = file_extension[1:].lower()
                
                if file_extension:
                    destination_folder = os.path.join(directory_path, file_extension)
                    os.makedirs(destination_folder, exist_ok=True)
                    
                    destination_path = os.path.join(destination_folder, file)
                    shutil.move(file_path, destination_path)
                    print(f"Moved '{file}' to '{destination_path}'")

if __name__ == "__main__":
    target_directory = input("Enter the target directory path: ")
    organize_files_by_extension(target_directory)
