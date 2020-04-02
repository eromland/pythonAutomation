import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

dirToWatch = "/home/erlend/Downloads"
dirToMove = "/home/erlend/Videos"

class myHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f" {event.src_path} has been created!")
        if os.path.isdir(event.src_path):
            for file in os.listdir(event.src_path):
                if file.endswith(".mkv"):
                    newFilename = dirToMove + event.src_path
                    os.rename(event.src_path, newFilename)

        else:
            if event.src_path.endswith(".mkv"):
                    newFilename = dirToMove + "/" + event.src_path
                    os.rename(event.src_path, newFilename)


def main():
    event_handler = myHandler()
    observer = Observer()
    observer.schedule(event_handler, path=dirToWatch, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        Observer.stop()
        Observer.join()

if __name__ == "__main__":
    main()

