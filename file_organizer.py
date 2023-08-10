import os #necessary for working with the file system
import shutil #file operations

def organize_files_by_extension(directory_path):
    if not os.path.exists(directory_path): #error handling
        print("Directory does not exist.")
        return

    for root, _, files in os.walk(directory_path):#loops through directories
        for file in files: #loops through files in each directory
            file_path = os.path.join(root, file) #stores file path and verifies it
            if os.path.isfile(file_path):
                _, file_extension = os.path.splitext(file) #split filename and extension
                file_extension = file_extension[1:].lower() #store lowercase extension
                
                if file_extension: #verify real extension
                    destination_folder = os.path.join(directory_path, file_extension)# make destination folder path
                    os.makedirs(destination_folder, exist_ok=True)#make folder and check if it already exists
                    
                    destination_path = os.path.join(destination_folder, file)#make path for file that will go in this specific extension folder
                    shutil.move(file_path, destination_path)#move the file there
                    print(f"Moved '{file}' to '{destination_path}'")#tell the user that it was moved

if __name__ == "__main__": #run the function when program is run, copy paste the directory that the user wants to organize
    target_directory = input("Enter the target directory path: ")
    organize_files_by_extension(target_directory)
