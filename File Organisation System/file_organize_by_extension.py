import os
import shutil

def organize_files(source_dir, dest_dir):
    # Get all files in the source directory
    files = os.listdir(source_dir)

    for file in files:
        # Get the full path of the file
        file_path = os.path.join(source_dir, file)

        # Check if it is a file
        if os.path.isfile(file_path):
            # Get the file extension
            _, ext = os.path.splitext(file)

            # Remove the leading dot from the extension and convert to lowercase
            ext = ext[1:].lower()

            # Create a destination directory for the file extension if not exists
            dest_folder = os.path.join(dest_dir, ext)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            # Move the file to the destination directory
            shutil.move(file_path, os.path.join(dest_folder, file))

if __name__ == "__main__":
    source_directory = "path/to/source/directory"
    destination_directory = "/path/to/destination/directory"

    organize_files(source_directory, destination_directory)
    print("File organization completed!")
