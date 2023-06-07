#!/usr/bin/env python3
import os
import shutil


class CategorizeLangFilesHelper:
    def __init__(self):
        self.current_directory = None
        self.files_directory = None

    def move_file_to_specific_location(self, source, destination):
        shutil.move(source, destination)

    def create_new_directory(self, sub_folder_name):
        os.makedirs(f'{self.files_directory}/{sub_folder_name}', exist_ok=True)

    def get_files_dir(self):
        """
        This function gets the files directory (in this case, it's in the app root folder)
        """
        self.current_directory = os.getcwd()
        self.files_directory = os.path.join(self.current_directory, "files")

    def grouping_files(self):
        """
        This function gets all files and groups them
        """
        files = os.listdir(self.files_directory)
        files = [file for file in files if file.endswith(".txt")]
        groups = {}
        patch_size = 100

        for i in range(0, len(files), patch_size):
            patch_files = files[i:i + patch_size]
            for file in patch_files:
                language = file.split("-")[0]
                groups.setdefault(language, []).append(file)

            # Create sub-folders if they don't exist for each language and move the files
            for language, files in groups.items():
                self.create_new_directory(language)

                # Getting sub-folder path
                subfolder = os.path.join(self.current_directory, self.files_directory, language)

                # Move the files to the sub-folders
                for file in files:
                    source = os.path.join(self.files_directory, file)
                    destination = os.path.join(subfolder, file)
                    self.move_file_to_specific_location(source, destination)

            groups = {}  # Reset the groups dictionary for the next patch

        print("Files have been grouped into sub-folders based on language.")


categorize_files = CategorizeLangFilesHelper()
categorize_files.get_files_dir()
categorize_files.grouping_files()
