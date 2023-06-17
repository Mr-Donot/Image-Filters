class MenuManager:
    def __init__(self, tree):
        self.tree = tree

    def displayMenu(self):
        dict = self.tree
        for index in dict:
            branch = dict[index]
            print(f"{branch['name']} ({list(dict.keys())[list(dict.values()).index(branch)]})")
        listener = input("Your choice : ")
        if listener in dict.keys():
            if dict[listener]["type"] == "function" : 
                dict[listener]["function"]()
        else :
            quit = input("Do you want to quit ? (Y/n)")
            quits  = ["y", "yes", "ouais", "q", "quit", "quitter", "exit", "bye", "oui", "si"]
            if quit.lower() in quits:
               return
        self.displayMenu()