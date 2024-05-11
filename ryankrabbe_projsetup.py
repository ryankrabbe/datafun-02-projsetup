''' This module provides a reusable byline for the author's services. '''

# Import Dependencies
import pathlib
import time
import ryankrabbe_utils

def create_folders_for_range(start, end):
    """
    Create folders for a given range (e.g., years).
    """
    for i in range(start, end + 1):
        pathlib.Path(f"{i}").mkdir(exist_ok=True)

def create_folders_from_list(folder_list):
    """
    Create folders from a list of names.
    """
    for folder in folder_list:
        pathlib.Path(folder).mkdir(exist_ok=True)

def create_prefixed_folders(folder_list, prefix):
    """
    Create prefixed folders by transforming a list of names and combining each with a prefix.
    """
    for folder in folder_list:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

def create_folders_periodically(duration):
    """
    Create folders periodically (e.g., one folder every 5 seconds).
    """
    folder_count = 0
    while True:
        folder_count += 1
        folder_name = f"Folder_{folder_count}"
        folder_path = pathlib.Path.cwd().joinpath(folder_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")
        time.sleep(duration)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Pring byline from imported module
    print(f"byline:{ryankrabbe_utils}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start=2020, end=2024)  # Updated function call

    # Call function 2 to create folders given a list
    folder_names = ['West', 'Midwest', 'East']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['temperature', 'rainfall', 'wind']
    prefix = 'weather-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 1000  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options to force lowercase and remove spaces to function 2
    states = [
        "Illinois",
        "Missouri",
        "Florida",
        "Texas",
        "California",
        "Maine",
        "Kentucky"
    ]
    create_folders_from_list(states, to_lowercase=True, remove_spaces=True)

if __name__ == "__main__":
    main()
