import os

def add_jpg_suffix(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "douban" in dirpath.lower():
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                new_filename = filename + ".jpg"
                new_file_path = os.path.join(dirpath, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed {file_path} to {new_file_path}")

root_dir = "."  # specify the root directory to start searching from
add_jpg_suffix(root_dir)
