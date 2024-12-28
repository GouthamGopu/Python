import os

# Specify the directory path
directory_path = '/VSCode'  

# List the contents of the specified directory
try:
    contents = os.listdir(directory_path)
    print("Contents of the directory:", directory_path)
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory {directory_path} was not found.")
except PermissionError:
    print(f"You do not have permission to access {directory_path}.")
