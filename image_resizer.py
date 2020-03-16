
import os
import sys
import getopt
from pathlib import Path

from PIL import Image

# Set Defaults
USE_SUBDIRECTORIES = True
INPUT_EXTENSION = ".png"
OUTPUT_EXTENSION = ".jpg"
WIDTH = 1280
HEIGHT = 720
myDir = os.getcwd()
sysargs = sys.argv[1:]

try:
    opts, args = getopt.getopt(sysargs, "ni:o:w:h:t:", ["inputextension=", "outputextension", "width=", "height=", "toplevel="])
except getopt.GetoptError:
    print("Usage: image_resizer.py -n -i inputextension -o outputextension -w width -h height -t toplevel_directory")
    sys.exit(2)

for opt, arg in opts:
    if opt == '-n':
        USE_SUBDIRECTORIES = False
    if opt in ("-i", "--inputextension"):
        INPUT_EXTENSION = str(arg)
    if opt in ("-o", "--outputextension"):
        OUTPUT_EXTENSION = str(arg)
    if opt in ("-w", "--width"):
        WIDTH = int(arg)
    if opt in ("-h", "--height"):
        HEIGHT = int(arg)
    if opt in ("-t", "--toplevel"): # TODO: Fix spaces in filepaths breaking stuff
        myDir = arg


new_size = (WIDTH, HEIGHT)  # width, height for resized output

for root, dirs, files in os.walk(myDir):
    
    for file in files:        
        if file.endswith(INPUT_EXTENSION):
            full_path = os.path.join(root, file)
            outfile = os.path.splitext(file)[0] + OUTPUT_EXTENSION  # rename
            

            if USE_SUBDIRECTORIES:
                processedPath = Path(f"{root}/{new_size[0]}x{new_size[1]}") # full path required
                processedPath.mkdir(parents=True, exist_ok=True) # create subfolder
            else:
                processedPath = Path(f"{root}")

            if file != outfile:
                 
                try:
                    with Image.open(full_path) as im:
                        im = im.resize(new_size)  # set new size
                        im.save(os.path.join(processedPath, outfile)) # save as jpeg
                        print(f"Saved {outfile} at {im.size[0]} x {im.size[1]} pixels.")
                        
                except IOError:
                    print(f"Cannot resize {file}.")
