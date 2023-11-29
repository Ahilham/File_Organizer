import os
import sys
import shutil
import easygui
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from File_Organizer_class import FileOrganizer

def get_directory():
    return easygui.diropenbox(title = "Select a directory to organize")

if __name__ == "__main__":
    path = get_directory()

    if path is None:
        print("No directory selected.")
        exit()
    else:
        event_handler = FileOrganizer()

    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        event_handler.organize_file(path, file_path)

    observer = Observer()
    observer.schedule(event_handler, path, recursive = False)
    observer.start()
    print("Enter Ctrl + C to end.")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()