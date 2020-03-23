# Image Resizer

This commandline Python 3.6+ application uses the Pillow library to resize and/or change filetypes of *every* specified image type in a directory and **all** subdirectories.

By default, resized images are created in a subdirectory at the original image's location named with the given width x height.

If no width or height is specified the program will use half of your monitor's resolution (as reported by Tkinter).


## Usage

Ensure the required [Pillow library](https://pypi.org/project/Pillow/) is installed. With the command line, use this format:


`python image_resizer.py -n -i inputextension -o outputextension -w width -h height -t 'top_directory'`



**Options**

- -h: Display this usage information
- -n: Do not place resized images in width x height subfolders"
- -i, -o: Specify image type file extensions ie .jpg, .png, .bmp
- -w, -h: Pixel dimensions for the resized file. Default is half of primary monitor resolution.
- -t: Use quotation marks when specifying the directory. All images in this directory and EVERY subdirectory will be targeted for resizing.
