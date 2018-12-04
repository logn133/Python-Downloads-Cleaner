# Python-Downloads-Cleaner

## Description
You can customize this script to your liking. Changing which file types go where by changing the main `requiredDirs` dictionary. Any new directory added to the list will be checked at startup and created if needed. Then if given any file types, will automatically search and move matching file types to their directory.

## Installation
Take this script and run it with the task scheduler in windows.

## Usage
To edit the script how you like, set the boolean `debug` to True so no files will be moved or deleted when you run it(make sure you set this back to False when you're done so the script can actually work).
```Python
debug = True
```
The other main boolean is `keepOldFiles`, set this to true if you want to move all old files to a folder called **OLD** instead of deleting them.
```Python
keepOldFiles = True
```
To change file types and edit folder names, edit the dictionary named `requiredDirs`, say you wanted to add a new folder called **CAD** for CAD files such as **.cad** and **.ipt**. All you have to do is add it to the end, so take this

```Python
requiredDirs = {"Programs":["exe","bat","msi"], "Pictures":["jpg","png","gif","bmp"], "Documents":["doc","docx","txt","pdf","pptx","ppt"], "ISOs":["bz2","zip","gz"], "Archives":["iso","img"], "OLD":[],"Installers":[], "Logs":["log"]}
```

and add this to the dictionary

```Python
"CAD-Files":["cad","ipt"]
```

to make it look like this

```Python
requiredDirs = {"Programs":["exe","bat","msi"], "Pictures":["jpg","png","gif","bmp"], "Documents":["doc","docx","txt","pdf","pptx","ppt"], "ISOs":["bz2","zip","gz"], "Archives":["iso","img"], "OLD":[],"Installers":[], "Logs":["log"], "CAD-Files":["cad","ipt"]}
```

and Bob's your uncle, you're set!

## ToDo
1. Do not check for and create **OLD** directory
