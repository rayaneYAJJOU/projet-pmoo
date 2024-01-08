class Queue:
    """Classe file pour le système des pages"""

    def __init__(self, queue: list = None) -> None:
        
        # Initialisation
        self.__queue: list = queue if queue else []
        self.__size: int = len(self.__queue)
    
    def queue(self, element = None) -> None:
        if element:
            self.__queue.append(element)
    
    def dequeue(self):
        if self.__size > 0:
            return self.__queue.pop(0)
    
    def contains(self, element = None) -> bool:
        return element in self.__queue
    
    def get_first_element(self):
        if self.__size > 0:
            return self.__queue[0]
    
    def clear(self) -> None:
        self.__queue = []
        self.__size = 0
    
    # Getters/Setters
        
    def get_size(self) -> int:
        return self.__size
    
    def get_stack(self) -> list:
        return self.__queue