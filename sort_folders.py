import os
import shutil
from collections import Counter

def move_folders_based_on_file_type(src_folder):
    # Get the absolute path of the script's directory
    script_directory = os.path.abspath(os.path.dirname(__file__))

    # Destination folder for the solutions
    solutions_folder = os.path.join(script_directory, 'solutions')

    # Create the solutions folder if it doesn't exist
    os.makedirs(solutions_folder, exist_ok=True)

    # Iterate through all folders in the source directory
    for folder_name in os.listdir(src_folder):
        folder_path = os.path.join(src_folder, folder_name)

        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Look for files inside the directory
            files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

            # Exclude .md files from determining file types
            files_without_md = [file for file in files if not file.endswith('.md')]

            # If there are files, determine the most common file extension
            if files_without_md:
                file_extensions = [os.path.splitext(file)[1] for file in files_without_md]
                most_common_extension = max(set(file_extensions), key=file_extensions.count)

                # Use the most common extension to determine the destination folder
                destination_folder = f"{most_common_extension[1:]}-solutions"
                destination_path = os.path.join(solutions_folder, destination_folder)

                # Create the destination folder if it doesn't exist
                os.makedirs(destination_path, exist_ok=True)

                # Move the entire folder to the destination
                shutil.move(folder_path, os.path.join(destination_path, folder_name))
                print(f"Moved '{folder_name}' to '{destination_path}'")

def main():
    # Set the source folder path as './solutions'
    src_folder = './solutions'

    # Get the absolute path of the script's directory
    script_directory = os.path.abspath(os.path.dirname(__file__))
    src_folder = os.path.join(script_directory, src_folder)

    # Create the source folder if it doesn't exist
    os.makedirs(src_folder, exist_ok=True)

    move_folders_based_on_file_type(src_folder)

if __name__ == "__main__":
    main()
