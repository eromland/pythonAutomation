import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

dirToWatch = "/home/erlend/Downloads"
dirToMove = "/home/erlend/Videos"

class myHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f" {event.src_path} has been modified!")
        for filename in os.listdir(dirToWatch):
            if os.path.isdir(filename):
                print("1")
                for file in os.listdir(filename):
                    if file.endswith(".mkv"):
                        oldFilename = dirToWatch + "/" + filename
                        newFilename = dirToMove + "/" + filename
                        os.rename(oldFilename, newFilename)
                        print(filename + " has been moved to: " + dirToMove)

            else:
                if filename.endswith(".mkv"):
                    oldFilename = dirToWatch + "/" + filename
                    newFilename = dirToMove + "/" + filename
                    os.rename(oldFilename, newFilename)
                    print(filename + " has been moved to: " + dirToMove)


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

