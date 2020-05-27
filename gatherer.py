import os
import re
import sys


# Get the source directory
while True:
    try:
        pwd = input("Choose the main folder with the tasks files: ")
        if re.match(re.compile(r'/[a-zA-z0-9]+/*'), pwd):
            break
        else:
            print("\nThis is not a folder! " +
                  "Try something like /path/of/folder\n")
    except Exception:
        pass

# Return an iterator for all the folders in the main folder
f = (file for file in os.listdir(pwd))

# For every folder, check if there is a tasks.todo file and copy it to
# the destination folder
for folder in f:
    item = os.listdir(f"{pwd}/{folder}")
    if 'tasks.todo' in item:
        try:
            # Copy .todo files and convert them in .md files
            # Make sure to copy only old files. That will prevent
            # newer, edited files, to be overwriten by old ones
            p = os.system(
                "cp -p -u " +
                f"{pwd}/{folder}/tasks.todo " +
                f"{pwd}/tasks/{folder}_tasks.md"
            )

            # If not successful, print the error output of the command
            if p != 0:
                print(sys.stderr)
        except Exception as e:
            print(e)
