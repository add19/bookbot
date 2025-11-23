from stats import get_num_words_in_text
from stats import get_char_freq_in_text
from stats import sort_characters_in_map
import sys

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words_in_text(text=text)
    freq_list = sort_characters_in_map(get_char_freq_in_text(text))
    """
    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found 75767 total words
    --------- Character Count -------
    """
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in freq_list:
        if not dict["char"].isalpha():
            continue
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()