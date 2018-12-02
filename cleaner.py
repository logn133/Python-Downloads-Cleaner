#Take all 'exe' files and put them into a labeled folder, remove any non picture file older than X days/weeks/months, put all pictures into a labeled folder
import os
import shutil
from datetime import datetime, timedelta


#Initializing global vars
requiredDirs = {"Programs":["exe","bat","msi"], "Pictures":["jpg","png","gif","bmp"], "Documents":["doc","docx","txt","pdf","pptx","ppt"], "ISOs":["bz2","zip","gz"], "Archives":["iso","img"], "OLD":[],"Installers":[], "Logs":["log"]}
toDelete = []
path = os.path.expanduser('~/Downloads/')

#Set to True for testing
debug = False

#Set to true if you don't want your old files being deleted
keepOldFiles = True

def dirCheck():
    #Checks to see if the folders required are present
    global requiredDirs
    dirs = os.listdir(path)
    for dir in requiredDirs:
        if not dir in dirs:
            print(dir+" doens't exsist, making it now...\n")
            os.mkdir(path + dir)
        else:
            print("All directories are present...\n")

def checkDate(fullFilePath):
    global toDelete
    try:
        created = os.path.getmtime(fullFilePath)
    except:
        print("An error occured, trying creation date...\n")
        try:
            created = os.path.getctime(fullFilePath)
        except:
            print("Another error man, it's broke I don't know...\nSetting datetime to '0'\n")
            created = 0
    monthAgo = datetime.utcnow() - timedelta(days=30)
    fileUTC = datetime.utcfromtimestamp(created)
    if fileUTC < monthAgo:
        if not debug:
            toDelete.append(fullFilePath)
        return True
    elif fileUTC > monthAgo:
        return False

def scanDir():
    global toDelete, requiredDirs, removeFiles
    dirInfo = os.listdir(path)
    for filename in dirInfo:
        fullFilePath = path + "/" + filename
        extention = filename.rsplit(".",1)[-1]
        for dir in requiredDirs:
            if extention in requiredDirs[dir]:
                if not debug:
                    if dir == "Programs" and "install" in filename or dir == "Programs" and "Install" in filename:
                        print("\n"+filename+" is an installer and will be moved to the 'Installers' directory...\n")
                        shutil.move(fullFilePath, path+"Installers")
                    else:
                        print("\n"+filename+" is a " + extention + " and will be moved to the '"+ dir + "' directory...\n")
                        shutil.move(fullFilePath, path+dir)
        if checkDate(fullFilePath):
            print("\n" + filename + " is older than a month, it has been set for removal...\n")

def deleteOld():
    for x in toDelete:
        if not debug:
            if keepOldFiles:
                shutil.move(x, path+"OLD/")
            elif not keepOldFiles:
                os.remove(x)

#Program
dirCheck()
scanDir()
deleteOld()
