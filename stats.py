def get_word_count(file_contents):
    num_words = 0

    words = file_contents.split()
    for word in words:
        num_words += 1

    print(f"Found {num_words} total words")

def get_character_count(file_contents):
    characters = {}

    lower_file_contents = file_contents.lower()

    for letter in lower_file_contents:
        if letter in characters:
            characters[letter] = characters[letter] + 1

        else:
            characters[letter] = 1

    print(characters)