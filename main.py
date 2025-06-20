from stats import get_num_words, get_num_char, get_sorted_list

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    
    return book_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    char_count = get_num_char(book_text)
    sorted = get_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()