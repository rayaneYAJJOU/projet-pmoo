class Queue:
    """Classe file pour le système des pages"""

    def __init__(self, queue: list = None) -> None:
        
        # Initialisation
        self.__queue: list = queue if queue else []

    def __str__(self) -> str:
        if len(self.__queue) > 0:
            return "Queue: [" + ", ".join(map(str, self.__queue[:-1])) + f", {self.__queue[-1]}]"
        return f"Queue: [{self.__queue[0]}]" if len(self.__queue) > 0 else "Queue: []"
    
    def __len__(self) -> int:
        return len(self.__queue)
    
    def queue(self, element = None) -> None:
        if element:
            self.__queue.append(element)
    
    def dequeue(self):
        if len(self.__queue) > 0:
            return self.__queue.pop(0)
    
    def __contains__(self, element = None) -> bool:
        return element in self.__queue
    
    def get_first_element(self):
        if len(self.__queue) > 0:
            return self.__queue[0]
    
    def get_last_element(self):
        if len(self.__queue) > 0:
            return self.__queue[-1]
    
    def clear(self) -> None:
        self.__queue = []
    
    # Getters/Setters
    
    def get_stack(self) -> list:
        return self.__queue