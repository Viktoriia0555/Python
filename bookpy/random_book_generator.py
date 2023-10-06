import string
from books import Book
import random

random_words = [
    "apple", "banana", "cherry", "tomato", "blueberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "pear", "quince"
]


def generate_random_book(num_pages):
    book = Book()
    for _ in range(num_pages):
        num_paragraphs = random.randint(1, 3)  
        page_content = ""
        for _ in range(num_paragraphs):
            num_sentences = random.randint(1, 4)  
            paragraph = ""
            for _ in range(num_sentences):
                sentence_length = random.randint(5, 15)  
                sentence = ' '.join(random.sample(random_words, sentence_length))
                paragraph += sentence + '. '
            page_content += paragraph  
        book.add_page(page_content)
    return book
