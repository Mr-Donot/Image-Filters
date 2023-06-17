from PIL import Image
from PyQt5.QtWidgets import QApplication, QFileDialog
from filters import *
from movements import *

class MenuManager:
    def __init__(self):
        self.img = None
        self.function_dict = None
        self.tree = None
        self.loadImg()

    def displayMenu(self, depth=0, tree=None, menuName="Menu"):
        dict = self.tree if tree is None else tree
        print("\n"+"==="*(3*depth)+"========"+menuName+"========"+"==="*(3*depth))
        for index in dict:
            branch = dict[index]
            print("\t" * depth + f"-{branch['name']} ({list(dict.keys())[list(dict.values()).index(branch)]})")
        listener = input("\nYour choice: ")
        if listener in dict.keys():
            if dict[listener]["type"] == "function":
                dict[listener]["function"](self.img)
                self.displayMenu()
            elif dict[listener]["type"] == "speFunction":
                dict[listener]["function"]()
                self.displayMenu()
            elif dict[listener]["type"] == "folder":
                self.displayMenu(depth + 1, dict[listener]["children"], dict[listener]["name"])
        else:
            quit = input("Do you want to quit? (Y/n): ")
            quits = ["y", "yes", "ouais", "q", "quit", "quitter", "exit", "bye", "o", "oui", "si", "return"]
            if quit.lower() not in quits:
                self.displayMenu()

    def loadImg(self):
        _ = QApplication([])
        filePath, _ = QFileDialog.getOpenFileName()
        extension = filePath[-4:]
        if extension == ".png":
            self.img = Image.open(filePath)
            self.loadTree()
            self.displayMenu()
        elif filePath != "":
            self.tree = {"1": {"type": "speFunction", "function": self.loadImg, "name": "Load image (png)"}}
            self.displayMenu()
            
    def loadTree(self):
        self.tree = {
            "1": {"type": "folder", "name": "Filters", "children": {
                "1": {"type": "function", "function": filterNegative, "name": "Negative filter"},
                "2": {"type": "function", "function": filterBlackAndWhite, "name": "Black and White filter"},
                "3": {"type": "function", "function": filterWithHexadecimal, "name": "Custom filter"},
                "4": {"type": "speFunction", "function": self.displayMenu, "name": "Retour au menu principal"},
            }},
            "2": {"type": "folder", "name": "Movements", "children": {
                "1": {"type": "function", "function": verticalMirror, "name": "Vertical mirror"},
                "2": {"type": "function", "function": horizontalMirror, "name": "Horizontal mirror"},
                "3": {"type": "function", "function": rotate, "name": "Rotate"},
                "4": {"type": "speFunction", "function": self.displayMenu, "name": "Retour au menu principal"},
            }},
            "3": {"type": "speFunction", "function": self.loadImg, "name": "Load another image (png)"}
        }
