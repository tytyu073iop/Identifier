from is_right_length import is_right_length
import os
import re

def process_files_in_folder(folder_path, show_name):
    compiled_pattern = re.compile(r'S(\d{2})E(\d{2})')
    
    for file_name in os.listdir(folder_path):
        match = compiled_pattern.search(file_name)
        if match:
            season_number = int(match.group(1))
            episode_number = int(match.group(2))
            file_path = os.path.join(folder_path, file_name)
            if not is_right_length(file_path, show_name, season_number, episode_number):
                print(f"file {file_name} is incorrect")
                            
if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    show_name = input("Enter the show name: ")

    # Check if the episode length is correct
    process_files_in_folder(folder_path, show_name)