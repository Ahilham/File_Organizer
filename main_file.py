import os
import sys
import shutil
import easygui
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from File_Organizer_class import FileOrganizer
from animation import animation
import time
import pystray
from pystray import MenuItem as item
from PIL import Image
import threading
import atexit
import ctypes
import platform




observers = []


def get_directory():
    return easygui.diropenbox(title = "Select a directory to organize")

def clear_term():
    return os.system("clear" if os.name == "posix" else "cls")

def minimize_term():
    if platform.system() == "Windows":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)


def on_exit_wrapper(icon, item):
   on_exit()

def on_exit():
    print("Exiting")
    
    for observer in observers:
        observer.stop()
        observer.join()

    os._exit(0)
    
    

def run_program(icon, item):
    global observer
    path = get_directory()

    if path is None:
        print("No directory selected.")
        return   
    else:
        event_handler = FileOrganizer()

    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        event_handler.organize_file(path, file_path)

    observer = Observer()
    observer.schedule(event_handler, path, recursive = False)
    observer.start()
    observers.append(observer)
    


def create_system_tray_icon():
    
    image = Image.open(r"iconic.png")#insert picture for tray icon
    menu = (item('Run', run_program), item('Exit', on_exit))

    icon = pystray.Icon("FileOrganizer", image, "FileOrganizer", menu)
    icon.run()



atexit.register(on_exit)

if __name__ == "__main__":

    animate_text = animation()
    animate_text.print_moving_text()
    time.sleep(0.5)
    clear_term()

    print("Do not close the terminal.")
    print("Program will appear on the system tray.")
    time.sleep(1)
    minimize_term()
    

    if threading.current_thread().name == "MainThread":
        create_system_tray_icon()
    else:
        print("Please run the script from the main thread.")
    

    

    
    