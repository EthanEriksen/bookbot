def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict)
    print(f"The text contains {num_words} words.\n")
    print("=====Begin character count report=====")

    for entry in sorted_chars_list:
        if entry["char"].isalpha():
            print(f"The letter {entry['char']} was found {entry['count']} times.")

    print("==============End report==============")


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


def sort_on(dict):
    return dict["count"]


def chars_dict_to_sorted_list(chars_dict):
    chars_sorted_list = []
    for char in chars_dict:
        entry_dict = {
            "char": char,
            "count": chars_dict[char]
        }

        chars_sorted_list.append(entry_dict)

    chars_sorted_list.sort(reverse=True, key=sort_on)
    
    return chars_sorted_list


main()
