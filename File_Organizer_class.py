import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

class FileOrganizer(FileSystemEventHandler):

    def organize_file(self, path, file_path):
        if os.path.isfile(file_path):
            file_type = file_path.split('.')[-1].lower()
            destination_directory = f"{path}/{file_type}_files"
            os.makedirs(destination_directory, exist_ok = True)
            shutil.move(file_path, os.path.join(destination_directory, os.path.basename(file_path)))

    def organize_files(self, path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                self.organize_file(path, file_path)

    def on_created(self, event):
        time.sleep(10)
        self.organize_files(os.path.dirname(event.src_path))
        
        

    def on_modified(self, event):
        self.organize_files(os.path.dirname(event.src_path))

            
