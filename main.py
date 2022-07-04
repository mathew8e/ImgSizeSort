from email.header import Header
from pathlib import Path
from turtle import width
from PIL import Image
from os import listdir, path
import shutil


PATH = path.abspath(r"C:\Users\mathe\Downloads\OrientalitstPhotos")


ArrayWithImgObjects = []


class ImageObj():
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.ratio = width/height
        


for i in listdir(PATH):
    img = Image.open("{0}/{1}".format(PATH,i))
    w, h  = img.size
    ArrayWithImgObjects.append(ImageObj(i, w, h))
    

for image in ArrayWithImgObjects:
    # if (image.ratio =)
    print("Ratio: {0}     Width: {1}    Height: {2}    Name: {3}".format(image.ratio, image.width, image.height, image.name))
