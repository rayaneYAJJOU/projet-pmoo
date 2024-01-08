class Application:
    """Classe application"""
    
    def __init__(self, root = None, **kwargs):
        
        # S'assurer que root n'est pas None
        assert root != None, "Expected a root object, got None."

        misc_dict = {"title": "Placeholder", "width": 640, "height": 480}

        for _, (k, v) in enumerate(kwargs.items()):
            misc_dict.update({k: v})

        # Set-up du "root"
        self.__root = root
        self.__title: str = misc_dict["title"]
        self.__width: int = misc_dict["width"]
        self.__height: int = misc_dict["height"]

        # Set-up d'autres propriétés divers
        self.__root.title(self.__title)
        self.__root.wm_minsize(width = self.__width, height = self.__height)
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