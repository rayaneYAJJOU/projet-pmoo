from page import Page
from stack import Stack
from pqueue import Queue
from tkinter import Widget
from os import walk

class PageHandler:
    """Classe pour gérer les pages de l'application"""

    current_page: Page = Page.BlankPage()
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
        
        root.bind("<Button>", PageHandler.handle_mouse)
    
    @staticmethod
    def handle_mouse(e):
        if len(PageHandler.page_stack) > 1:
            match e.num:
                case 4:
                    PageHandler.previous_page()
                case 5:
                    PageHandler.next_page()
    
    @staticmethod
    def preload_pages(*filenames) -> None:
        for filename in filenames:
            page: Page = Page(PageHandler.root, filename)
            page.load(True)
            PageHandler.page_cache.update({filename: page})

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
        PageHandler.current_page = page
        return page.load()
    
    @staticmethod
    def clear_current_page() -> None:
        page = PageHandler.page_stack.get_last_element()
        if page:
            page.clear()
        
    
    @staticmethod
    def previous_page() -> int:
        print(PageHandler.page_stack)
        print(PageHandler.page_queue)
        print(PageHandler.current_page, PageHandler.page_stack.get_last_element())
        if PageHandler.current_page != PageHandler.page_stack.get_last_element():
            PageHandler.clear_current_page()
            PageHandler.page_queue.queue(PageHandler.page_stack.pop())
            PageHandler.current_page = PageHandler.page_queue.get_first_element()
            return PageHandler.load_page(PageHandler.current_page.get_filename())
        return 0
    
    @staticmethod
    def next_page(allowed: bool = True) -> int:
        if allowed and PageHandler.current_page != PageHandler.page_queue.get_first_element():
            PageHandler.clear_current_page()
            PageHandler.page_stack.push(PageHandler.page_queue.dequeue())
            PageHandler.current_page = PageHandler.page_stack.get_last_element()
            return PageHandler.load_page(PageHandler.current_page.get_filename())
        return 0