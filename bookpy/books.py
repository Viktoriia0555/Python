import random
import string

class Book:
    def __init__(self, title=None):
        if title is None:
            self.title = ''.join(random.choices(string.ascii_letters, k=10))
        else:
            self.title = title
        self.pages = []
    
    def add_page(self, page):
        self.pages.append(page)

    def print_pages(self):
        if self.pages:
            for i, page in enumerate(self.pages, start=1):
                print(f'Page {i}:\n{page}\n')
    
    def __str__(self):
        return f'Title: {self.title}'
        
    
class ScientificBook(Book):
    def __init__(self):
        self.references = []
        self.glossary = {}

class NovelBook(Book):
    def __init__(self):
        self.characters = {}

class TextBook(Book):
    def __init__(self):
        self.images = []

    def add_image(self, image):
        self.images.append(image)