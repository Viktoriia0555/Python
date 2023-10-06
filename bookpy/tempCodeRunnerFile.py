from books import Book
from pageSingleton import PageSingleton
from builders import BookBuilder, ScientificBookBuilder, NovelBuilder, ManualBuilder
from random_book_generator import generate_random_book

if __name__ == "__main__":
    random_book = generate_random_book(5)
    
    builder = BookBuilder()
    builder.create_book()
    builder.set_title("My Random Book")
    for page_content in random_book.pages:
        builder.add_page(page_content)
    my_random_book = builder.get_book()
    
    print(random_book)
    print("\n")
    print(my_random_book)
