# Python-Downloads-Cleaner

## Installation
Take this script and run it with the task scheduler in windows.

## Usage
To edit the script how you like, set the boolean `debug` to True so no files will be moved or deleted when you run it(make sure you set this back to False when you're done so the script can actually work).
```Python
debug = True
```
The other main boolean is `keepOldFiles`, set this to true if you want to move all old files to a folder instead of deleting them.
```Python
keepOldFiles = True
```
To change file types and edit folder names, edit the dictionary named `requiredDirs`, say you wanted to add a new folder for CAD files. All you have to do is add it to the end, so from this
```Python
requiredDirs = {"Programs":["exe","bat","msi"], "Pictures":["jpg","png","gif","bmp"], "Documents":["doc","docx","txt","pdf","pptx","ppt"], "ISOs":["bz2","zip","gz"], "Archives":["iso","img"], "OLD":[],"Installers":[], "Logs":["log"]}
```
to this
```Python
requiredDirs = {"Programs":["exe","bat","msi"], "Pictures":["jpg","png","gif","bmp"], "Documents":["doc","docx","txt","pdf","pptx","ppt"], "ISOs":["bz2","zip","gz"], "Archives":["iso","img"], "OLD":[],"Installers":[], "Logs":["log"], "CAD-Files":["cad","ipt"]}
```
and Bob's your uncle, you're set!
