import os
import shutil
import time
import random 
import sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/thesl/OneDrive/Desktop/DAVID A.K.A COOL_D/Project_103/Source"
destination="C:/Users/thesl/OneDrive/Desktop/DAVID A.K.A COOL_D/Project_103/Destination"

dirtree={
    "Image_Files":[".gif",".png",".jpg"],
    "Video_Files":[".mp4",".mov",".avi"],
    "Document_Files":[".ppt",".txt",".csv"],
    "SetUp_Files":[".exe",".bin",".cmd"]
}

class Filemovementhandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey {event.src_path} has been created!")

    def on_deleted(self,event):
        print(f"oops someone deleted {event.src_path} !")    

    def on_modified(self,event):
        print(f"oopsie {event.src_path} has been modiied!")  

    def on_moved(self,event):
        print(f" {event.src_path} has been moved!")        

       

eventhandler=Filemovementhandler()
observer=Observer()
observer.schedule(eventhandler,from_dir,recursive=True)
observer.start()
try:
    while True :
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()

   


