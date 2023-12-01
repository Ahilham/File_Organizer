import time
import shutil
import sys
import os


class animation():

    def print_moving_text(self):
        text = """  
        ______ _____ _      ______    ____  _____   _____          _   _ _____ ____________ _____  
        |  ____|_   _| |    |  ____|  / __ \|  __ \ / ____|   /\   | \ | |_   _|___  /  ____|  __ \ 
        | |__    | | | |    | |__    | |  | | |__) | |  __   /  \  |  \| | | |    / /| |__  | |__) |
        |  __|   | | | |    |  __|   | |  | |  _  /| | |_ | / /\ \ | . ` | | |   / / |  __| |  _  / 
        | |     _| |_| |____| |____  | |__| | | \ \| |__| |/ ____ \| |\  |_| |_ / /__| |____| | \ \ 
        |_|    |_____|______|______|  \____/|_|  \_\\_____/_/    \_\_| \_|_____/_____|______|_|  \_\
                                                                                             
                                                MADE BY: ILHAM                                                           
                                                                                             """
        width, height = shutil.get_terminal_size()
        

        for i in range(height):
            os.system("clear" if os.name == "posix" else "cls")
            padding = "\n" * i
            sys.stdout.write(padding+text)
            sys.stdout.flush()
            time.sleep(0.1)
            
