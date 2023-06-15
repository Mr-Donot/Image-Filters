from PIL import Image
from filters import *
from movements import *
import os
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()

filePath = filedialog.askopenfilename()
monImage=Image.open(filePath)

#choix entre filtre ou rotation :

while True :
    print ("\nWhat do you want to do with your loaded image ? : \n")
    print (" -Apply a filter ? (f)")
    print (" -Apply a movement ? (r)")

    choix=input()

    while choix!="f" and choix!="F" and choix!="r" and choix!="R" and choix!="exit" :
        choix=input("\nDidn't understand, try again :")

#filtre :

    if choix == "f" or choix == "F" :
        while True :
            print ("\nWhich filter do you want to use ? : ")
            print ("Available filters : \n")
            print ("  -Green (1)")
            print ("  -Negative (2)")
            print ("  -Black and white (3)")
            choix=input()

            while choix!="1" and choix!="2" and choix!="3" and choix!="exit" :
                choix=input("\nDidn't understand, try again :")

            if choix == "1":
                filterWithMask(monImage, [0,1,0])

            elif choix == "2":
                filtreNegative(monImage)

            elif choix == "3":
                filterBlackAndWhite(monImage)
            elif choix == "exit":
                break
#rotation :

    elif choix == "R" or choix == "r" :
        while True :
            print ("Which movement do you want to use ? : ")
            print ("\nAvailable movements :")
            print ("\n  -Vertical Mirror (m)")
            print ("\n  -Rotate 180 degrees (d)")
            choix=input()

            while choix!="m" and choix!="d" and choix!="M" and choix!="D" and choix!="exit":
                choix=input("\nJe n'ai pas compris, veuillez répéter :")

            if choix == "m" or choix == "M" :
                verticalMirror(monImage)

            elif choix == "d" or choix == "D" :
                rotateCustomAngle(monImage, 180)

            elif choix =="exit":
                break
    elif choix =="exit":
        break
