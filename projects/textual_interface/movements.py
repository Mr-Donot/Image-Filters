from PIL import Image
from utils import *

def rotateCustomAngle(img, angle):
    img = img.rotate(angle)
    img.show()
    saveImg(img)

def verticalMirror(img):
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.show()
    saveImg(img)

def horizontalMirror(img):
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.show()
    saveImg(img)