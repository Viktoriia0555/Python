from books import Book, NovelBook, ScientificBook, TextBook
from pageSingleton import PageSingleton
class BookBuilder:
    def __init__(self):
        self.book = None
    
    def create_book(self):
        self.book = Book()
    
    def set_title(self, title):
        self.book.title = title
    
    def add_page(self, content):
        page_id = PageSingleton().add_page(content)
        self.book.add_page(page_id)
    
    def get_book(self):
        return self.book

class ScientificBookBuilder(BookBuilder):
    def create_book(self):
        self.book = ScientificBook()
    
    def add_reference(self, reference):
        self.book.references.append(reference)
    
    def add_glossary_term(self, term, definition):
        self.book.glossary[term] = definition

class NovelBuilder(BookBuilder):
    def create_book(self):
        self.book = NovelBook()
    
    def add_character(self, name, description):
        self.book.characters[name] = description

class ManualBuilder(BookBuilder):
    def create_book(self):
        self.book = TextBook()
    
    def add_image(self, image):
        self.book.add_image(image)