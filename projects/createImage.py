from PIL import Image
from utils import *

def createUniformImageWithHexa(hexa, largeur, hauteur):
    if not isHexa(hexa):
        print("Wrong hexadecimal format.")
        return isHexa(hexa)
    
    if len(hexa)==7:
        hexa = hexa[1:]

    hexaInInt = list(map(lambda x : int(x, 16), [hexa[0:2],hexa[2:4], hexa[4:]]))

    img = Image.new('RGB', (largeur,hauteur), color = (int(hexaInInt[0]),int(hexaInInt[1]),int(hexaInInt[2])))
    
    img.show()
    saveImg(img)
    return img