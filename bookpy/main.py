from builders import BookBuilder, ScientificBookBuilder, NovelBuilder, ManualBuilder
from random_book_generator import generate_random_book

if __name__ == "__main__":
    random_book = generate_random_book(5)
    
    print("Random Book:")
    print(random_book)
    random_book.print_pages()
    
    scientific_builder = ScientificBookBuilder()
    scientific_builder.create_book()
    scientific_builder.set_title("Scientific Book")
    scientific_builder.add_reference("Reference 1")
    scientific_builder.add_reference("Reference 2")
    scientific_builder.add_glossary_term("Term 1", "Definition 1")
    scientific_builder.add_glossary_term("Term 2", "Definition 2")
    scientific_book = scientific_builder.get_book()
    
    print("\nScientific Book:")
    print(scientific_book)
    
    novel_builder = NovelBuilder()
    novel_builder.create_book()
    novel_builder.set_title("Novel Book")
    novel_builder.add_character("Character 1", "Description 1")
    novel_builder.add_character("Character 2", "Description 2")
    novel_book = novel_builder.get_book()
    
    print("\nNovel Book:")
    print(novel_book)
    
    manual_builder = ManualBuilder()
    manual_builder.create_book()
    manual_builder.set_title("Textbook")
    manual_builder.add_image("Image 1")
    manual_builder.add_image("Image 2")
    textbook = manual_builder.get_book()
    
    print("\nTextbook:")
    print(textbook)
