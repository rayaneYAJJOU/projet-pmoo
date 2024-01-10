from importlib import util

class Page:
    """Classe d'une page à charger"""

    PAGES_PATH: str = "pages"

    def __init__(self, root = None, filename: str = "", blank: bool = False) -> None:

        # Initialisation
        self.__filename: str = filename
        self.__root = root

        if blank:
            self.__name: str = "Blank"
            self.__widgets: dict = dict()
            return

        try:
            spec = util.spec_from_file_location(filename, Page.PAGES_PATH + "\\" + filename)
            self.__module = util.module_from_spec(spec)
            spec.loader.exec_module(self.__module)
        except ImportError as e:
            print(f"Error importing '{filename}': {e}")
        except Exception as e:
            print(f"Error executing '{filename}': {e}")
        
        if self.__module:
            self.__name: str = self.__module.name
            self.__module.root = self.__root
    
    @staticmethod
    def BlankPage():
        return Page(None, "", True)
    
    def __str__(self) -> str:
        return f"Page: {self.__name}, in file: {self.__filename}, in memory address: {hex(id(self))}"

    def load(self, preload: bool = False) -> int:
        try:
            self.__module.func(preload)
            self.__widgets: dict[str] = self.__module.widgets
        except Exception as e:
            print(f"Error executing '{self.__filename}': {e}")
            return 1
        return 0
    
    def clear(self) -> None:
        for widget in self.__widgets.values():
            widget.destroy()
        self.__widgets.clear()
        self.__module.widgets.clear()

    # Getters/Setters
    
    def get_filename(self) -> str:
        return self.__filename

    def get_name(self) -> str:
        return self.__name
    
    def get_widgets(self) -> list[list]:
        return self.__widgets