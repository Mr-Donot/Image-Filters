class MenuManager:
    def __init__(self, tree):
        self.tree = tree

    def displayMenu(self, tree=None):
        dict = self.tree if tree == None else tree
        for index in dict:
            branch = dict[index]
            print(f"{branch['name']} ({list(dict.keys())[list(dict.values()).index(branch)]})")
        listener = input("Your choice : ")
        if listener in dict.keys():
            if dict[listener]["type"] == "function" : 
                dict[listener]["function"]()
                self.displayMenu()
            elif dict[listener]["type"] == "folder" :
                self.displayMenu(dict[listener]["children"])

        else :
            quit = input("Do you want to quit ? (Y/n) : ")
            quits  = ["y", "yes", "ouais", "q", "quit", "quitter", "exit", "bye", "oui", "si"]
            if quit.lower() not in quits:
                self.displayMenu()
