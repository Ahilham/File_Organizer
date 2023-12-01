<<<<<<< HEAD
import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class FileOrganizer(FileSystemEventHandler):

    def organize_file(self, path, file_path):
        if os.path.isfile(file_path):
            file_type = file_path.split('.')[-1].lower()
            destination_directory = f"{path}/{file_type}_files"
            os.makedirs(destination_directory, exist_ok = True)
            shutil.move(file_path, os.path.join(destination_directory, os.path.basename(file_path)))

    def on_created(self, event):
        self.organize_file(event.src_path)

    def on_modified(self, event):
        self.organize_file(event.src_path)

            
=======
import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class FileOrganizer(FileSystemEventHandler):
    # def on_created(self, event):
    #     if event.is_directory:
    #         return
        
    #     file_path = event.src_path
    #     file_type = file_path.split('.')[-1].lower()

    #     destination_directory = f"./{file_type}_files"

    #     os.makedirs(destination_directory, exist_ok = True)
    #     shutil.move(file_path, os.path.join(destination_directory, os.path.basename(file_path)))

    def organize_file(self, path, file_path):
        if os.path.isfile(file_path):
            file_type = file_path.split('.')[-1].lower()
            destination_directory = f"{path}/{file_type}_files"
            os.makedirs(destination_directory, exist_ok = True)
            shutil.move(file_path, os.path.join(destination_directory, os.path.basename(file_path)))

    def on_created(self, event):
        self.organize_file(event.src_path)

    def on_modified(self, event):
        self.organize_file(event.src_path)

            
>>>>>>> 845c3d08770ab4c99dfafd625c41491c1bb831e8
