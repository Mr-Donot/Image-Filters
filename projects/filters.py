from PIL import Image
from utils import *

def filterNegative(img):
    (largeur,hauteur)=img.size
    newImg = Image.new('RGB', (largeur,hauteur), color = (0, 0, 0))
    for i in range (largeur):
        for j in range (hauteur):
            p=img.getpixel((i,j))
            newImg.putpixel((i,j),((255-p[0]),(255-p[1]),(255-p[2])))
    newImg.show()
    saveImg(newImg)


def filterWithHexadecimal(img):
    hexa = input("Enter the hexadecimal code of the color for the filter : ")
    while not isHexa(hexa):
        print("Wrong hexadecimal format.")
        hexa = input("Enter the hexadecimal code of the color for the filter (No to return to the menu): ")
        quits = ["n", "no", "non", "nan", "quit", "quitter", "exit", "return", "bye"]
        if hexa.lower() in quits :
            return
    
    if len(hexa)==7:
        hexa = hexa[1:]
    mask = list(map(lambda x : int(x, 16), [hexa[0:2],hexa[2:4], hexa[4:]]))
    mask = normalizeMask(mask)
    (largeur,hauteur)=img.size
    newImg = Image.new('RGB', (largeur,hauteur), color = (0,0,0))
    for i in range (largeur):
        for j in range (hauteur):
            p=img.getpixel((i,j))
            newImg.putpixel((i,j),(int(p[0]*mask[0]),int(p[1]*mask[1]),int(p[2]*mask[2])))
    newImg.show()
    saveImg(newImg)

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