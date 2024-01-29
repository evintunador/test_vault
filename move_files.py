import os
import shutil
import argparse

def contains_string(file_path, search_string):
    """
    Check if the given .md file contains the specified string.
    
    :param file_path: Path to the file to be checked.
    :param search_string: String to search for within the file.
    :return: True if the file contains the string, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return search_string in file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return False

def move_files(source_dir, dest_dir, search_string=None, file_type=None):
    """
    Move .md files containing a specific string and files of a specified type from source_dir to dest_dir.
    
    :param source_dir: Directory to search for files.
    :param dest_dir: Directory to move the matching files to.
    :param search_string: String to search for within .md files. If None, this criteria is ignored.
    :param file_type: File extension to search for. If None, this criteria is ignored.
    """
    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        raise FileNotFoundError(f"The destination directory '{dest_dir}' does not exist.")

    # List all files in the source directory
    for filename in os.listdir(source_dir):
        # Construct full file path
        file_path = os.path.join(source_dir, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move .md file if it contains the search string
        if search_string and filename.endswith('.md') and contains_string(file_path, search_string):
            shutil.move(file_path, os.path.join(dest_dir, filename))
            print(f"Moved: {filename}")

        # Move file if it matches the specified file type
        elif file_type and filename.endswith(file_type):
            shutil.move(file_path, os.path.join(dest_dir, filename))
            print(f"Moved: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move .md files containing a specific string and files of a specified type.")
    parser.add_argument("--source", help="Source directory (defaults to the current directory of this script)", default=os.path.dirname(os.path.realpath(__file__)))
    parser.add_argument("--dest", help="Destination directory", required=True)
    parser.add_argument("--string", help="String to search within .md files", default=None)
    parser.add_argument("--type", help="File type to move, e.g., '.txt'", default=None)

    args = parser.parse_args()

    move_files(args.source, args.dest, args.string, args.type)






