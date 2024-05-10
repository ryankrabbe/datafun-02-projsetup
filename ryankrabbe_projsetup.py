''' This module provides a reusable byline for the author's services. '''

# Import Dependencies
import pathlib
import time

def create_folders_for_range(start, end):
    """
    Create folders for a given range (e.g., years).
    """
    folder_paths = []
    for year in range(start, end + 1):
        folder_name = str(year)
        folder_path = pathlib.Path.cwd().joinpath(folder_name)
        folder_path.mkdir(parents=True, exist_ok=True)
        folder_paths.append(folder_path)
    return folder_paths

def create_folders_from_list(folder_list):
    """
    Create folders from a list of names.
    """
    folder_paths = []
    for name in folder_list:
        folder_path = pathlib.Path.cwd().joinpath(name)
        folder_path.mkdir(parents=True, exist_ok=True)
        folder_paths.append(folder_path)
    return folder_paths

def create_prefixed_folders(folder_list, prefix):
    """
    Create prefixed folders by transforming a list of names and combining each with a prefix.
    """
    folder_paths = [pathlib.Path.cwd().joinpath(f"{prefix}{name}") for name in folder_list]
    for path in folder_paths:
        path.mkdir(parents=True, exist_ok=True)
    return folder_paths

def create_folders_periodically(duration):
    """
    Create folders periodically (e.g., one folder every 5 seconds).
    """
    folder_count = 0
    while True:
        folder_count += 1
        folder_name = f"Folder_{folder_count}"
        folder_path = pathlib.Path.cwd().joinpath(folder_name)
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")
        time.sleep(duration)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=1995, end_year=2024)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 10  # duration in seconds
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
