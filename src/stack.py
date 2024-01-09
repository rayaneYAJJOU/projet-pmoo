class Stack:
    """Classe pile pour le système des pages"""

    def __init__(self, stack: list = []) -> None:
        
        # Initialisation
        self.__stack: list = stack
        self.__size: int = len(stack)
    
    def push(self, element = None) -> None:
        if element:
            self.__stack.append(element)
    
    def pop(self):
        if self.__size > 0:
            return self.__stack.pop(-1)
    
    def contains(self, element = None) -> bool:
        element in self.__stack
    
    def get_last_element(self):
        if self.__size > 0:
            return self.__stack[-1]
    
    def clear(self) -> None:
        self.__stack = []
        self.__size = 0

    # Getters/Setters
        
    def get_size(self) -> int:
        return self.__size
    
    def get_stack(self) -> list:
        return self.__stack