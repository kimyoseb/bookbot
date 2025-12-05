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

    return characters

def sort_character_count(characters):
    sorted_list = []

    def sort_on(items):
        return items["num"]

    for character in characters:
        count = characters[character]

        if character.isalpha() == True:
            entry = {"char": character, "num": count}
            sorted_list.append(entry)

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list