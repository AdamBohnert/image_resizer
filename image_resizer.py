
import getopt
import os
import sys
from tkinter import Tk
from pathlib import Path

from PIL import Image


def main():
    root = Tk() # Used for default resolution

    # Set Defaults
    USE_SUBDIRECTORIES = True
    INPUT_EXTENSION = ".png"
    OUTPUT_EXTENSION = ".jpg"
    WIDTH = int(root.winfo_screenwidth()/2)
    HEIGHT = int(root.winfo_screenheight()/2)
    myDir = os.getcwd()
    sysargs = sys.argv[1:]

    try:
        opts, args = getopt.getopt(sysargs, "?ni:o:w:h:t:", ["help", "inputextension=", "outputextension", "width=", "height=", "toplevel="])
    except getopt.GetoptError:
        print("Usage: image_resizer.py -n -i inputextension -o outputextension -w width -h height -t 'top_directory'")
        print("Use -? or --help for the help menu.")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-?', '--help'):
            print("Usage: image_resizer.py -n -i inputextension -o outputextension -w width -h height -t 'top_directory'")
            print("-n: Do not place resized images in width x height subfolders")
            print("-i, -o: Specify image type file extensions ie .jpg, .png, .bmp")
            print("-w, -h: Pixel dimensions for the resized file. Default is half of primary monitor resolution.")
            print("-t: Use quotation marks when specifying the directory. All images in this directory and EVERY subdirectory will be targeted for resizing.")
        elif opt == '-n':
            USE_SUBDIRECTORIES = False
        elif opt in ("-i", "--inputextension"):
            INPUT_EXTENSION = str(arg)
        elif opt in ("-o", "--outputextension"):
            OUTPUT_EXTENSION = str(arg)
        elif opt in ("-w", "--width"):
            WIDTH = int(arg)
        elif opt in ("-h", "--height"):
            HEIGHT = int(arg)
        elif opt in ("-t", "--toplevel"):
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


if __name__ == "__main__":
    main()
