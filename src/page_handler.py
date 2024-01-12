from page import Page
from stack import Stack
from pqueue import Queue
from tkinter import Widget
from os import walk

class PageHandler:
    """Classe pour gérer les pages de l'application"""

    page_lstack: Stack = Stack()
    page_rstack: Stack = Stack()
    page_cache: list[str] = []
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
                    PageHandler.page_cache.append(filename)
        
        root.bind("<Button>", PageHandler.handle_mouse)
    
    @staticmethod
    def handle_mouse(e):
        match e.num:
            case 4:
                PageHandler.previous_page()
            case 5:
                PageHandler.next_page()
    
    @staticmethod
    def preload_page(page: Page = None) -> int:
        if page and isinstance(page, Page):
            page.load(True)
    
    @staticmethod
    def preload_pages(*filenames) -> None:
        for filename in filenames:
            page: Page = Page(PageHandler.root, filename)
            page.load(preload = True)
            PageHandler.page_cache.append(filename)

    @staticmethod
    def load_page(filename: str = "", new: bool = True) -> int:

        if not filename in PageHandler.page_cache:
            return -1
        
        page: Page = Page(PageHandler.root, filename)

        if new:
            if PageHandler.page_lstack.get_last_element():
                PageHandler.clear_page(PageHandler.page_lstack.get_last_element())
            PageHandler.page_lstack.push(page)
            if not page in PageHandler.page_rstack:
                PageHandler.page_rstack.clear()

        return page.load()
    
    @staticmethod
    def clear_page(page: Page = None) -> None:
        if page and isinstance(page, Page):
            page.clear()
        
    
    @staticmethod
    def previous_page() -> int:
        #print(PageHandler.page_lstack, PageHandler.page_rstack)
        if len(PageHandler.page_lstack) > 1:
            last = PageHandler.page_lstack.get_last_element()
            PageHandler.clear_page(last)
            PageHandler.preload_page(last)
            PageHandler.page_rstack.push(PageHandler.page_lstack.pop())
            return PageHandler.load_page(PageHandler.page_lstack.get_last_element().get_filename(), False)
        return 0
    
    @staticmethod
    def next_page() -> int:
        if len(PageHandler.page_rstack) > 0:
            PageHandler.clear_page(PageHandler.page_lstack.get_last_element())
            PageHandler.page_lstack.push(PageHandler.page_rstack.pop())
            return PageHandler.load_page(PageHandler.page_lstack.get_last_element().get_filename(), False)
        return 0