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
    print ("\nTrès bien. Vous allez maintenant pouvoir choisir le changement a appliquer a votre image : ")
    print ("\n -filtre de couleur (f)")
    print (" -rotation (r)")

    choix=input()

    while choix!="f" and choix!="F" and choix!="r" and choix!="R" and choix!="exit" :
        choix=input("\nJe n'ai pas compris, veuillez répéter :")

#filtre :

    if choix == "f" or choix == "F" :
        while True :
            print ("\nTrès bien. Vous allez maintenant pouvoir choisir le filtre a appliquer a votre image : ")
            print ("Veuillez choisir un filtre parmi ceux proposés : ")
            print ("\n  -vert (1)")
            print ("  -négatif (2)")
            print ("  -noir et blanc (3)")
            choix=input()

            while choix!="1" and choix!="2" and choix!="3" and choix!="exit" :
                choix=input("\nJe n'ai pas compris, veuillez répéter :")

#filtre vert :
            if choix == "1":
                filterWithMask(monImage, [0,1,0])

            elif choix == "2":
                filtreNegatif(monImage)

            elif choix == "3":
                filtreNoirBlanc(monImage)
            elif choix == "exit":
                break
#rotation :

    elif choix == "R" or choix == "r" :
        while True :
            print ("Très bien. Vous allez maintenant pouvoir choisir le changement a appliquer a votre image : ")
            print ("\nVeuillez choisir un changement parmi ceux proposés :")
            print ("\n  -miroir (m)")
            print ("\n  -180 degrés (d)")
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
