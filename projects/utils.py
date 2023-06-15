def isHexa(hexa):
    if len(hexa)!= 6 and len(hexa)!= 7:
        return False

    if len(hexa) == 7 and hexa[0] != '#':
        return False
    if len(hexa)==7:
        hexa = hexa[1:]
    possibleChar = 'aAbBcCdDeEfF0123456789'
    for i in hexa:
        if i not in possibleChar:
            return False
    return True

def normalizeMask(mask):
    temp = max(mask)
    return [mask[0]/temp, mask[1]/temp, mask[2]/temp]

def saveImg(img):
    nameToSave = input("Choose the file name to save the image, including the extension : ")
    img = img.save("samples/"+nameToSave)