#Take all 'exe' files and put them into a labeled folder, remove any non picture file older than X days/weeks/months, put all pictures into a labeled folder
#ToDo make the lists updatable, make the lists stored in a resource file to be parsed at startup
import os
import shutil
#Initializing global vars
requiredDirs = ["Programs", "Pictures", "Documents", "ISOs"]

progCheck = False
executableFiles = ["exe","bat"]
progPath = os.path.expanduser('~/Downloads/Programs/')

docCheck = False
documentFiles = ["doc","docx","txt","pdf"]
docPath = os.path.expanduser('~/Downloads/Documents/')

imgCheck = False
imageFiles = ["iso","img"]
imgPath = os.path.expanduser('~/Downloads/ISOs')

picCheck = False
pictureFiles = ["jpg","png","gif"]
picPath = os.path.expanduser('~/Downloads/Pictures')

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
            if dir in requiredDirs[2]:
                docCheck = True
                print("Programs exsist")
            if dir in requiredDirs[4]:
                isoCheck = True
                print("Programs exsist")
    if not progCheck:
        print("Programs doesn't exsist, making it now...")
        os.mkdir(path+"Programs")
    if not picCheck:
        print("Pictures doesn't exsist, making it now...")
        os.mkdir(path+"Pictures")
    if not docCheck:
        print("Pictures doesn't exsist, making it now...")
        os.mkdir(path+"Documents")
    if not isoCheck:
        print("Pictures doesn't exsist, making it now...")
        os.mkdir(path+"ISOs")

def scanDir():
    dirInfo = os.walk(path)
    for fullPath, dirName, files in dirInfo:
        for filename in files:
            extention = filename[-6:]
            extention = extention.split(".",1)[-1]
            created = os.path.getmtime(fullPath+"/"+files)
            if extention in executableFiles:
                print("its a bat")
                shutil.move(fullpath+filename, progPath)
            if extention in pictureFiles:
                print("its a pic")   
                shutil.move(fullpath+filename, picPath)
            if extention in imageFiles:
                print("its an image file") 
                shutil.move(fullpath+filename, isoPath)
            if extention in documentFiles:
                print("its a document")
                shutil.move(fullpath+filename, docPath)
                
    

#Program
dirCheck()
scanDir()


#def checkDate():

#def removeOld():

#def moveFiles():
