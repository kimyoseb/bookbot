from stats import get_word_count, get_character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    path_to_file = "books/frankenstein.txt"

    book_text = get_book_text(path_to_file)
    book_words = get_word_count(book_text)
    book_characters = get_character_count(book_text)

main()
