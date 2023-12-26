# Classe application

class Application:

    def __init__(self, ttk = None, tk = None, **kwargs):

        # Vérifier si tk est passer comme "None" ou non
        assert tk != None, "Expected Tk class as argument, got None."
        assert ttk != None, "Expected ttk class as argument, got None."

        # Séparer les dictionnaires, un pour le "root", l'autre pour les propriétes divers
        rootDict = {}
        miscDict = {"title": "Placeholder", "width": 640, "height": 480}

        # Pour éviter d'appeler la fonction chaque tour de boucle
        keysMisc = miscDict.keys()

        for _, (k, v) in enumerate(kwargs.items()):
            if k in keysMisc:
                miscDict.update({k: v})
            else:
                rootDict.update({k: v})

        # Set-up du "root"
        self.__root = tk(**rootDict)
        self.__title = miscDict["title"]
        self.__width = miscDict["width"]
        self.__height = miscDict["height"]

        # Set-up d'autres propriétés divers
        self.__root.title(self.__title)
        self.__root.geometry(f"{self.__width}x{self.__height}")
    
    # Boucle d'évènements de l'application
    def mainloop(self, n: int = 0) -> None:
        self.__root.mainloop(n)


    # Getters/Setters
    
    def get_root(self):
        return self.__root
    
    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height
    
    def get_title(self) -> str:
        return self.__title


    def set_width(self, width: int = None) -> None:
        self.__width = width if width != None else self.__width
        self.__root.geometry(f"{self.__width}x{self.__height}")
    
    def set_height(self, height: int = None) -> None:
        self.__height = height if height != None else self.__height
        self.__root.geometry(f"{self.__width}x{self.__height}")
    
    def set_title(self, title: str = None) -> None:
        self.__title = title if title != None else self.__title
        self.__root.title(self.__title)
