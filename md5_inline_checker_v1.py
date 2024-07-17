import os
import hashlib

# Define a function to calculate the MD5 hash of a file
def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Prompt the user for a folder path
folder_path = input("Please enter the folder path: ")

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    # If the file is a .md5 file
    if filename.endswith('.md5'):
        # Get the base name of the file (without the .md5 extension)
        base_name = filename[:-4]
        # Look for files with the same base name and different extensions
        for other_filename in os.listdir(folder_path):
            if other_filename.startswith(base_name) and other_filename != filename:
                # Calculate the MD5 hash of the other file
                other_md5 = calculate_md5(os.path.join(folder_path, other_filename))
                # Read the MD5 hash from the .md5 file
                with open(os.path.join(folder_path, filename), 'r') as f:
                    md5_file = f.read().strip()
                # Compare the two MD5 hashes
                if other_md5 == md5_file:
                    print(f"The MD5 hash of {other_filename} matches the hash in {filename}.")
                else:
                    print(f"The MD5 hash of {other_filename} does not match the hash in {filename}.")

