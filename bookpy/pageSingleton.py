class PageSingleton:
    _instance = None
    _page_id = 1
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PageSingleton, cls).__new__(cls)
            cls._instance.pages = {}
        return cls._instance

    def add_page(self, content):
        page_id = self._page_id
        self.pages[page_id] = content
        self._page_id += 1
        return page_id