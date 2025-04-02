import os
import subprocess

def get_filenames_in_directory(directory_path):
    try:
        filenames = os.listdir(directory_path)
        return filenames
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return []
    except NotADirectoryError:
        print(f"Error: '{directory_path}' is not a directory.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
        return []
    except OSError as e: 
        print(f"An OS error occured: {e}")
        return []

directory = "coverage_files" 
files = get_filenames_in_directory(directory)

if files:
    for filename in files:
        print(filename)
else:
    print("No files found or an error occurred.")
command_arr = ['sailcov',  '-a', 'coverage_files/all_branches']
for filename in files:
    if filename  == "all_branches":
        continue
    command_arr.append('-t')
    command_arr.append(os.path.join(directory, filename))

command_arr.append('decoder/instructions.sail')

subprocess.run(command_arr)

