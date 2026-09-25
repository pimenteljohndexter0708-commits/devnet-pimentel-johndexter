"""
Module 2 — Activity: File Sorting with os and shutil
Student: Pimentel, John Dexter
Date: 25/09/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


So in this activity I bullt a simple File sorting with os and shutil. The script automatically 
organizes the file base on its extension or file type. I used os module to list all file in the (sample_folder). Using os.path.splitext(), 
it gets the file extension like .txt or .jpg, and then it will look in the EXTENSIONS where I have the dictionary for all the extensions I put. If it matches on any of the category 
or the extensions, the program will create a destination folder using os.makedirs(). 
then using shutil.move() file is move into the folder. Then the script prints a message "moved".

============================================
KEY VOCABULARY
============================================
- os module: This is a built-in module. It does so many things. It is used to interact with the opearting system.
- shutil module: This is used to move files into their category or folder.
- file path: This the location of a file.
- directory: Just like a folder or container. It is used for organiztion.
- extension: The type of file (.txt, .jpg, .pdf)
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

target_dir = "./sample_folder"

EXTENSIONS = {
  ".txt" : "Documents",
  ".pdf" : "Documents",
  ".png" : "Images",
  ".jpg" : "Images",
  ".py"  : "Codes",
}

if os.path.exists(target_dir):
  for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)

    if os.path.isfile(file_path):
      _, ext = os.path.splitext(filename)
      ext = ext.lower()

      if ext in EXTENSIONS:
        folder_name = EXTENSIONS[ext]
        dest_folder = os.path.join(target_dir, folder_name)

        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_folder, filename))
        print(f"Moved {filename} -> {folder_name}/")
else:

  print(f"Target directory '{target_dir}' does not exist.")

# 
# 
#  ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

First of all, I didn't know it is possible to create a file using python. Knowing the syntax or what a certain word does gives me a hard time. 
Even now, I don't fully understand it. WHen it works, I struggled in adding files, because I didn't know what to put, but after researching I managed to test the code, I've added files, 
and the code does what it need to do, it sorted the file for me.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
