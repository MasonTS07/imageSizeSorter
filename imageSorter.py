import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os 
import json

class MyHandler(FileSystemEventHandler):
    i=1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg')):
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)

folder_to_track = '/Users/Mason/Documents/Downloads'
folder_destination = '/Users/Mason/Documents/Downloads2'
image_small = '/Users/Mason/Pictures/Wallpapers/1920x1080'
image_large = '/Users/Mason/Pictures/Wallpapers/2560x1440'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()