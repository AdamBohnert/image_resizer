
import sys
import os
from pathlib import Path
from PIL import Image

new_size = (1280, 720)  # width, height to resize to
myDir = os.getcwd()

for root, dirs, files in os.walk(myDir):  # TODO: How do subdirectories work?
    
    for file in files:        
        if file.endswith(".png"):
            
            outfile = os.path.splitext(file)[0] + ".jpg"  # change to jpeg
            
            if file != outfile:
                try:
                    with Image.open(file) as im:
                        im = im.resize(new_size)  # set new size
                        im.save(outfile, "JPEG")
                        print(f"Saved {outfile} at {im.size[0]} x {im.size[1]}")
                        
                except IOError:
                    print(f"Cannot create jpeg for {file}. It may already exist.")

