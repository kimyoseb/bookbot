from stats import get_word_count, get_character_count, sort_character_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    path_to_file = sys.argv[1]
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    # Read the whole text file and find # of total words
    book_text = get_book_text(path_to_file)
    book_words = get_word_count(book_text)
    print("--------- Character Count -------")
    # Look at text and make dictionary of character/#
    book_characters = get_character_count(book_text)
    sorted_list = sort_character_count(book_characters)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
