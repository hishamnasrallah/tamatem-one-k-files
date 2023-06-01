#!/usr/bin/env python3

import os
import shutil

# Define the directory where the text files are
# located and in this case its in the app root folder
current_directory = os.getcwd()
files_directory = os.path.join(current_directory, "files")

# create a list of all the text files in the directory
files = os.listdir(files_directory)

# here to make sure only .txt file are detected
files = [file for file in files if file.endswith(".txt")]

# grouping the files by language
groups = {}
for file in files:
    language = file.split("-")[0]
    groups.setdefault(language, []).append(file)

# create sub-folders if not exists for each language and move the files
for language, files in groups.items():

    # create sub-folder
    os.makedirs(f'{files_directory}/{language}', exist_ok=True)

    # getting sub-foldet path
    subfolder = os.path.join(current_directory, files_directory, language)

    # move the files to the sub-folders
    for file in files:
        source = os.path.join(files_directory, file)
        destination = os.path.join(subfolder, file)
        shutil.move(source, destination)

print("Files have been grouped into sub-folders based on language.")
