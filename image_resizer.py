
import os
import sys
from pathlib import Path

from PIL import Image

new_size = (1280, 720)  # width, height to resize to
myDir = os.getcwd()

for root, dirs, files in os.walk(myDir): # TODO: Set command line options to specify dir
    
    for file in files:        
        if file.endswith(".png"):
            full_path = os.path.join(root, file)
            outfile = os.path.splitext(file)[0] + ".jpg"  # rename to jpeg
            processedPath = Path(f"{root}/{new_size[0]}x{new_size[1]}") # full path required
            processedPath.mkdir(parents=True, exist_ok=True) # create subfolder

            if file != outfile:
                 
                try:
                    with Image.open(full_path) as im:
                        im = im.resize(new_size)  # set new size
                        im.save(os.path.join(processedPath, outfile), "JPEG") # save as jpeg
                        print(f"Saved {outfile} at {im.size[0]} x {im.size[1]} pixels.")
                        
                except IOError:
                    print(f"Cannot create jpeg for {file}. It may already exist.")
