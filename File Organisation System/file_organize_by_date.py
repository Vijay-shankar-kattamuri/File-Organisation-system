import os
import shutil
from datetime import datetime

def organize_files_by_datetime(source_dir, destination_dir):
    # Get a list of files in the source directory
    files = os.listdir(source_dir)

    for file_name in files:
        source_path = os.path.join(source_dir, file_name)

        # Get the modification timestamp of the file
        timestamp = os.path.getmtime(source_path)

        # Convert the timestamp to a datetime object
        file_datetime = datetime.fromtimestamp(timestamp)

        # Create the destination directory based on the year and month
        year = file_datetime.strftime("%Y")
        month = file_datetime.strftime("%m")
        destination_subdir = os.path.join(destination_dir, year, month)

        # Create the destination subdirectory if it doesn't exist
        os.makedirs(destination_subdir, exist_ok=True)

        # Move the file to the destination directory
        destination_path = os.path.join(destination_subdir, file_name)
        shutil.move(source_path, destination_path)

        print(f"Moved '{file_name}' to '{destination_path}'")

if __name__ == "__main__":
    source_directory = "/path/to/source/directory"
    destination_directory = "/path/to/destination/directory"

    organize_files_by_datetime(source_directory, destination_directory)


