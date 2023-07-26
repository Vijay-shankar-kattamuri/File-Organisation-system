import os
import shutil

def organize_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)

        # Create a directory with the extension name if it doesn't exist
        destination_subdir = os.path.join(destination_dir, extension[1:])  # Ignore the dot in the extension
        if not os.path.exists(destination_subdir):
            os.makedirs(destination_subdir)

        # Move the file to the destination directory
        destination_path = os.path.join(destination_subdir, filename)
        shutil.move(source_path, destination_path)

    print("File organization complete!")

# Example usage
source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"
organize_files(source_directory, destination_directory)

