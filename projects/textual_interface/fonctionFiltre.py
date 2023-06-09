from PIL import Image

def saveImg(img):
    nameToSave = input("Choose the file name to save the image, including the extension : ")
    img = img.save("samples/"+nameToSave)

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

def normalizeMask(mask):
    temp = max(mask)
    return [mask[0]/temp, mask[1]/temp, mask[2]/temp]


def filtreVert(monImage):
  
    (largeur,hauteur)=monImage.size
    img = Image.new('RGB', (largeur,hauteur), color = (0, 1, 0))
    for i in range (0,largeur):
        for j in range (0,hauteur):
            pTemp = img.getpixel((i,j))
            p=monImage.getpixel((i,j))
            img.putpixel((i,j),(p[0]*pTemp[0],p[1]*pTemp[1],p[2]*pTemp[2]))
    img.show()
    saveImg(img)

def filtreVertOld(monImage):
  
    (largeur,hauteur)=monImage.size
    img = Image.new('RGB', (largeur,hauteur), color = (0, 0, 0))
    for i in range (0,largeur):
        for j in range (0,hauteur):
            p=monImage.getpixel((i,j))
            img.putpixel((i,j),(0,p[1], 0))
    img.show()
    saveImg(img)

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

def rotation(img):

    img.rotate(180).show()
    img = img.rotate(180)
    saveImg(img)

def miroir (img):

    img.transpose(Image.FLIP_LEFT_RIGHT).show()
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    saveImg(img)

