from PIL import Image
from utils import *


def filtreNegatif(monImage):
    
    (largeur,hauteur)=monImage.size
    img = Image.new('RGB', (largeur,hauteur), color = (0, 0, 0))
    for i in range (0,largeur):
        for j in range (0,hauteur):
            p=monImage.getpixel((i,j))
            img.putpixel((i,j),((255-p[0]),(255-p[1]),(255-p[2])))
    img.show()
    saveImg(img)

def filterWithMask(monImage, mask):
    mask = normalizeMask(mask)
    print(mask)
    (largeur,hauteur)=monImage.size
    img = Image.new('RGB', (largeur,hauteur), color = (0,0,0))
    for i in range (0,largeur):
        for j in range (0,hauteur):
            p=monImage.getpixel((i,j))
            img.putpixel((i,j),(int(p[0]*mask[0]),int(p[1]*mask[1]),int(p[2]*mask[2])))
    img.show()
    saveImg(img)


def filterWithHexadecimal(img, hexa):
    if not isHexa(hexa):
        print("Wrong hexadecimal format.")
        return isHexa(hexa)
    
    if len(hexa)==7:
        hexa = hexa[1:]
    mask = list(map(lambda x : int(x, 16), [hexa[0:2],hexa[2:4], hexa[4:]]))
    filterWithMask(img, mask)

def filtreNoirBlanc(monImage):
    
    (largeur,hauteur)=monImage.size
    img = Image.new('RGB', (largeur,hauteur), color = (0, 0, 0))
    for i in range (0,largeur):
        for j in range (0,hauteur):
            p=monImage.getpixel((i,j))
            couleur=int((p[0]+p[1]+p[2])/3)
            img.putpixel((i,j),(couleur,couleur,couleur))
    img.show()
    saveImg(img)




