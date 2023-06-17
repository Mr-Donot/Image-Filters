from PIL import Image
from utils import *

def rotate(img):
    angle = input("How much angle ? : ")
    try:
        angle = int(angle)
        img = img.rotate(angle)
        img.show()
        saveImg(img)
    except:
        return

def verticalMirror(img):
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.show()
    saveImg(img)

def horizontalMirror(img):
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.show()
    saveImg(img)