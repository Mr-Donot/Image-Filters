from PIL import Image
from utils import *


def filtreNegative(img):
    
    (largeur,hauteur)=img.size
    newImg = Image.new('RGB', (largeur,hauteur), color = (0, 0, 0))
    for i in range (largeur):
        for j in range (hauteur):
            p=img.getpixel((i,j))
            newImg.putpixel((i,j),((255-p[0]),(255-p[1]),(255-p[2])))
    newImg.show()
    saveImg(newImg)

def filterWithMask(img, mask):
    mask = normalizeMask(mask)
    print(mask)
    (largeur,hauteur)=img.size
    newImg = Image.new('RGB', (largeur,hauteur), color = (0,0,0))
    for i in range (largeur):
        for j in range (hauteur):
            p=img.getpixel((i,j))
            newImg.putpixel((i,j),(int(p[0]*mask[0]),int(p[1]*mask[1]),int(p[2]*mask[2])))
    newImg.show()
    saveImg(newImg)


def filterWithHexadecimal(img, hexa):
    if not isHexa(hexa):
        print("Wrong hexadecimal format.")
        return isHexa(hexa)
    
    if len(hexa)==7:
        hexa = hexa[1:]
    mask = list(map(lambda x : int(x, 16), [hexa[0:2],hexa[2:4], hexa[4:]]))
    filterWithMask(img, mask)

def filterBlackAndWhite(img):
    
    (largeur,hauteur)=img.size
    newImg = Image.new('RGB', (largeur,hauteur), color = (0, 0, 0))
    for i in range (largeur):
        for j in range (hauteur):
            p=img.getpixel((i,j))
            couleur=int((p[0]+p[1]+p[2])/3)
            newImg.putpixel((i,j),(couleur,couleur,couleur))
    newImg.show()
    saveImg(newImg)




