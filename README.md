# File Gatherer

A python script for searching and gathering all the .todo files of a main folder to a destination folder. The main folder should be the place with all your projects or something like this. The script copies the **tasks.todo** files from all the folders in a folder with __tasks__ name, which is located in the main folder, and converts them in __.md__ files. Also, the scripts copies only old __.todo__ files so you can edit the new __.md__ files without the fear of overwriting them if you run the script again on the same folder.

---

#### <u>Requirements</u>

The requiments for the script to run are in the `requirements.txt` file. You can install all the requirements at once with `pip install -r requirements`. Obviously, you need first to check that you've got the Python version 3.8 on your system and you've got pip installed. The program was built with these versions of the required libraries but maybe it'll work with versions greater than the required.

#### <u>Usage</u>

```bash
python3 gatherer.py
```

> Run the script with the above command and enter the path of the main folder in the `/path/for/folder` format
