from email.header import Header
from multiprocessing.dummy import Array
import os
from pathlib import Path
import string
from turtle import width
from PIL import Image
from os import path, mkdir, walk, listdir
import shutil


def makeImgObjArray(PATH):
    ArrayWithImgObjects = []
    class ImageObj():
        def __init__(self, name, width, height):
            self.name = name
            self.width = width
            self.height = height
            self.ratio = width/height
                
    for i in listdir(PATH):
        if i.endswith(".png") or i.endswith(".jpg"):
            img = Image.open("{0}/{1}".format(PATH,i))
            w, h  = img.size
            ArrayWithImgObjects.append(ImageObj(i, w, h))
            img.close()
    
    return ArrayWithImgObjects

def sort(PATH):
    try:

        def createFolders():
            mkdir("{0}\\portrait".format(PATH))
            mkdir("{0}\\square".format(PATH))
            mkdir("{0}\\landscape".format(PATH))
            
        if "portrait" not in listdir(PATH) or "landscape" not in listdir(PATH) or "square" not in listdir(PATH):    
            createFolders()
        else:
            return 2
            
        ArrayWithImgObjects = makeImgObjArray(PATH)
            

        for image in ArrayWithImgObjects:
            # print("Ratio: {0}     Width: {1}    Height: {2}    Name: {3}".format(image.ratio, image.width, image.height, image.name))
            if image.ratio < 0.9:
                shutil.move("{0}/{1}".format(PATH, image.name), "{0}/{1}".format(PATH, "portrait"))
            elif image.ratio >= 0.9 and image.ratio <= 1.1:
                shutil.move("{0}/{1}".format(PATH, image.name), "{0}/{1}".format(PATH, "square"))
            else:
                shutil.move("{0}/{1}".format(PATH, image.name), "{0}/{1}".format(PATH, "landscape"))
        
        return 1
    except:
        return 0
    
def sortWideToTall(PATH):
    # sort the images by ratio and puts an ascii characet infromt
    # try:
        ArrayWithImgObjects = makeImgObjArray(PATH)
        
        ArrayWithImgObjects.sort(key=lambda x: x.ratio)
        asciiList = []
        
        for letter1 in list(string.ascii_letters):
            for letter2 in list(string.ascii_letters):
                for letter3 in list(string.ascii_letters):
                    asciiList.append("{0}{1}{2}".format(letter1, letter2, letter3))
        for i in range(len(ArrayWithImgObjects)):
            os.rename("{0}/{1}".format(PATH, ArrayWithImgObjects[i].name), "{0}/{1}_{2}".format(PATH, asciiList[i], ArrayWithImgObjects[i].name))
            print(ArrayWithImgObjects[i].ratio)
        return 1
    # except:
    #     return 0
