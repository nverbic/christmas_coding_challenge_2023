'''
    Build a ZIP Archive

    Output:

    Subfolders: ['animals']
    Files: ['flowers.jpg', 'formations.png', 'images.txt', 'waterfall.jpg']


    Current folder: .\src\14 Build a Zip Archive\my_stuff\animals
    Subfolders: []
    Files: ['bird.png', 'chipmunks.jpg', 'lizard.jpg', 'pelican.jpg', 'squirrel.png', 'starfish.png', 'turtle.png']


    Created ZIP archive: my_stuff.zip.
'''

import os
import zipfile

# def zip_all(input_dir, extension_list, output_dir):
def zip_all(input_dir, zip_file):
    '''' Build a ZIP Archive '''
    with zipfile.ZipFile(zip_file, 'w') as my_zip:
        # Walk through all files in the directory and its subdirectories
        for foldername, subfolders, filenames in os.walk(input_dir):
            print(f"Current folder: {foldername}")
            print(f"Subfolders: {subfolders}")
            print(f"Files: {filenames}")
            print("\n")
            for filename in filenames:
                # Create the full file path
                file_path = os.path.join(foldername, filename)

                # Add the file to the ZIP archive using its relative path
                file_path_inside_archive = os.path.relpath(file_path, input_dir)

                my_zip.write(file_path, file_path_inside_archive)

    print(f"Created ZIP archive: {zip_file}.")

# commands used in solution video for reference
if __name__ == '__main__':

     # Directory to be zipped
    input_dir = '.\\src\\14 Build a Zip Archive\\my_stuff'

    # Name of the ZIP archive to create
    zip_file = 'my_stuff.zip'

    # Todo: Specify file extensions to be zipped
    zip_all(input_dir, zip_file)
