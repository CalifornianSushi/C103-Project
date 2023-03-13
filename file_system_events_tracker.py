import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Step 2

from_dir = "/Users/nimaigarg/Downloads"

#Step 3

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops ! Someone deleted {event.src_path} ! ")
    
    def on_moved(self, event):
        print(f"Someone has renamed or moved {event.src_path} ! ")
    
    def on_modified(self, event):
        print(f"Someone has modified {event.src_path} ! ")

# Step 4

x = FileEventHandler()
y = Observer()

y.schedule(x, from_dir, recursive=True)

y.start()

# Step 5

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
        print("stopped!")
        y.stop()