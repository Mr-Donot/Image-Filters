from PIL import Image
from fonctionFiltre import *
from utils import *

def createUniformImageWithHexa(hexa, largeur, hauteur):
    if not isHexa(hexa):
        print("Wrong hexadecimal format.")
        return isHexa(hexa)
    
    if len(hexa)==7:
        hexa = hexa[1:]

    hexaInInt = list(map(lambda x : int(x, 16), [hexa[0:2],hexa[2:4], hexa[4:]]))

    img = Image.new('RGB', (largeur,hauteur), color = (0,0,0))
    for i in range (0,largeur):
        for j in range (0,hauteur):
            img.putpixel((i,j),(int(hexaInInt[0]),int(hexaInInt[1]),int(hexaInInt[2])))
    img.show()
    saveImg(img)
    return img