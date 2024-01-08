from page import Page
from stack import Stack
from pqueue import Queue

class PageHandler:
    """Classe pour gérer les pages de l'application"""

    page_stack: Stack = Stack()
    page_queue: Queue = Queue()
    EXIT_CODE: list[str] = ["Success", "Fail"]

    @staticmethod
    def load_page(root = None, filename: str = "", clear: bool = False) -> int:

        # S'assurer que root n'est pas None
        assert root != None, "Expected a root object, got None."

        if clear:
            PageHandler.page_queue.clear()
        page: Page = Page(root, filename)
        PageHandler.clear_page()
        PageHandler.page_stack.push(page)
        return page.load()
    
    @staticmethod
    def clear_page() -> None:
        page = PageHandler.page_stack.get_last_element()
        if page:
            page.clear()
        
    
    @staticmethod
    def previous_page() -> int:
        current = PageHandler.page_stack.pop()
        PageHandler.clear_page(current)
        PageHandler.page_queue.queue(current)
        return PageHandler.load_page(PageHandler.page_stack.get_last_element())
    
    @staticmethod
    def next_page() -> int:
        current = PageHandler.page_stack.get_last_element()
        PageHandler.clear_page(current)
        current = PageHandler.page_queue.dequeue()
        PageHandler.page_stack.push(current)
        return PageHandler.load_page(current)