class Stack:
    """Classe pile pour le système des pages"""

    def __init__(self, stack: list = []) -> None:
        
        # Initialisation
        self.__stack: list = stack
    
    def __str__(self) -> str:
        if len(self.__stack) > 0:
            return "Stack: [" + ", ".join(map(str, self.__stack[:-1])) + f"{self.__stack[-1]}]"
        return "Stack: []"
    
    def __len__(self) -> int:
        return len(self.__stack)
    
    def push(self, element = None) -> None:
        if element:
            self.__stack.append(element)
    
    def pop(self):
        if len(self.__stack) > 0:
            return self.__stack.pop(-1)
    
    def __contains__(self, element = None) -> bool:
        return element in self.__stack
    
    def get_last_element(self):
        if len(self.__stack) > 0:
            return self.__stack[-1]
    
    def clear(self) -> None:
        self.__stack = []

    # Getters/Setters
    
    def get_stack(self) -> list:
        return self.__stack