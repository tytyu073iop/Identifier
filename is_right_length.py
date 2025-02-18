import os
import subprocess
from tvdb_v4_official import TVDB as Tvdb
import re
from API_KEY import API_KEY

episodes = []

def extract_number(s):
    # Find all sequences of digits in the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the found sequences to integers
    numbers = [int(num) for num in numbers]
    
    return numbers[0]

# Function to get episode length from TVDB
def get_tvdb_episode_length(api_key, show_name, season_number, episode_number):
    global episodes
    if not episodes:
        tvdb = Tvdb(apikey=api_key)
        show = tvdb.search(show_name)[0]
        show_id = extract_number(show["objectID"])
        episodes = tvdb.get_series_episodes(show_id)["episodes"]
    episode = episodes[season_number*episode_number - 1 + 2] #Kolhoz inside 
    return episode['runtime']

# Function to get episode length using ffprobe
def get_ffprobe_length(file_path):
    cmd = [
        'ffprobe', '-v', 'error', '-show_entries',
        'format=duration', '-of',
        'default=noprint_wrappers=1:nokey=1', file_path
    ]
    output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(output.stdout)

def is_right_length(file_path, show_name, season_number, episode_number, proximity = 1):

    # Get lengths
    tvdb_length = get_tvdb_episode_length(API_KEY, show_name, season_number, episode_number)
    ffprobe_length = get_ffprobe_length(file_path) / 60

    # Check if the lengths match
    if abs(tvdb_length - ffprobe_length) < proximity:
        # print("The episode length is correct.")
        return True
    else:
        # print(f"The episode length is incorrect. TVDB: {tvdb_length} mins, File: {ffprobe_length} mins.")
        return False

# Test the function
if __name__ == "__main__":
    # Ask for user input
    file_path = input("Enter the path to your episode file: ")
    show_name = input("Enter the show name: ")
    season_number = int(input("Enter the season number: "))
    episode_number = int(input("Enter the episode number: "))

    # Check if the episode length is correct
    is_right_length(file_path, show_name, season_number, episode_number)