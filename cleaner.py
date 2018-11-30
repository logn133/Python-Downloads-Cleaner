#Take all 'exe' files and put them into a labeled folder, remove any non picture file older than X days/weeks/months, put all pictures into a labeled folder
#ToDo make the lists updatable, make the lists stored in a resource file to be parsed at startup
import os
#Initializing global vars
requiredDirs = ["Programs", "Pictures"]
progCheck = False
picCheck = False
pictureFiles = ["jpg","png","gif"]
executableFiles = ["exe","bat"]
path = os.path.expanduser('~/Downloads/')


def dirCheck():
    #Checks to see if the folders required are present
    global progCheck, picCheck
    dirs = os.listdir(path)
    for dir in dirs:
        if dir in requiredDirs:
            if dir in requiredDirs[0]:
                progCheck = True
                print("Programs exsist")
            if dir in requiredDirs[1]:
                picCheck = True
                print("Programs exsist")
    if not progCheck:
        print("Programs doesn't exsist, making it now...")
        os.mkdir(path+"Programs")
    if not picCheck:
        print("Pictures doesn't exsist, making it now...")
        os.mkdir(path+"Pictures")

def scanDir():
    dirInfo = os.walk(path)
    for fullPath, dirName, files in dirInfo:
        for filename in files:
            extention = filename[-6:]
            extention = extention.split(".",1)[-1]
            if extention in executableFiles:
                print("its a bat")
            if extention in pictureFiles:
                print("its a pic")

#Program
dirCheck()
scanDir()


#def checkDate():

#def removeOld():

#def moveFiles():
