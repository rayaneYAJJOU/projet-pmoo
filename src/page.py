from importlib import util

class Page:
    """Classe d'une page à charger"""

    PAGES_PATH = "pages"

    def __init__(self, root = None, filename: str = "") -> None:

        # Initialisation
        self.__filename: str = filename
        self.__root = root

        try:
            spec = util.spec_from_file_location(filename, Page.PAGES_PATH+"\\"+filename)
            self.__module = util.module_from_spec(spec)
            spec.loader.exec_module(self.__module)
        except ImportError as e:
            print(f"Error importing '{filename}': {e}")
        except Exception as e:
            print(f"Error executing '{filename}': {e}")
        
        if self.__module:
            self.__name: str = self.__module.name
            self.__widgets: list = self.__module.widgets

    def load(self) -> int:
        try:
            self.__module.func(self.__root)
        except Exception as e:
            print(f"Error executing '{self.__filename}': {e}")
            return 1
        
        return 0
    
    def clear(self) -> None:
        for widget in self.__widgets:
            widget.destroy()

    # Getters/Setters
    
    def get_name(self) -> str:
        return self.__name
    
    def get_widgets(self) -> list[list]:
        return self.__widgets