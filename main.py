def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    print(f"The text contains {num_words} words.")
    print(chars_dict)


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_chars_dict(text):
    lowered_text = text.lower()
    char_dict = {}

    for char in lowered_text:

        if char in char_dict:
            char_dict[char] += 1

        else:
            char_dict[char] = 1

    return char_dict


main()
