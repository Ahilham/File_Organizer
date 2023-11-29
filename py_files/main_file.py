import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from File_Organizer_class import FileOrganizer

if __name__ == "__main__":
    path = input("Enter path that needs to be organized:")
    event_handler = FileOrganizer()

    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        event_handler.organize_file(path, file_path)

    observer = Observer()
    observer.schedule(event_handler, path, recursive = False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()