from page import Page
from stack import Stack
from pqueue import Queue
from os import walk

class PageHandler:
    """Classe pour gérer les pages de l'application"""

    page_stack: Stack = Stack()
    page_queue: Queue = Queue()
    page_cache: dict[str, Page] = dict()
    EXIT_CODE: list[str] = ["Success", "Fail"]
    root = None

    @staticmethod
    def init(root = None):
        # S'assurer que root n'est pas None
        assert root != None, "Expected a root object, got None."

        if not PageHandler.root:
            PageHandler.root = root
        
        for _, __, files in walk(Page.PAGES_PATH):
            for filename in files:
                if filename.endswith(".py"):
                    PageHandler.preload_pages(filename)
    
    @staticmethod
    def preload_pages(*filenames) -> None:
        for filename in filenames:
            PageHandler.page_cache.update({filename: Page(PageHandler.root, filename)})

    @staticmethod
    def load_page(filename: str = "") -> int:
        page: Page = Page.BlankPage()

        if filename in PageHandler.page_cache.keys():
            page = PageHandler.page_cache[filename]
            if page != PageHandler.page_queue.get_first_element():
                PageHandler.page_queue.clear()
        else:
            PageHandler.page_queue.clear()
            page: Page = Page(PageHandler.root, filename)
            PageHandler.page_cache.update({filename: page})
        
        PageHandler.clear_current_page()
        PageHandler.page_stack.push(page)
        print(PageHandler.page_stack)
        return page.load()
    
    @staticmethod
    def clear_current_page() -> None:
        page = PageHandler.page_stack.get_last_element()
        if page:
            print("clear")
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