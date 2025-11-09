import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path_to_book = sys.argv[1]


from stats import get_total_words
from stats import get_character_count
from stats import sort_on_dictionary 

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(path_to_book)
    total_words = get_total_words(text)
    character_count = get_character_count(text)
    char_list = sort_on_dictionary(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char in char_list:
        letter = char["char"]
        count = char["num"]
        if not letter.isalpha():
            continue
        print(f"{letter}: {count}")
    print("============= END ===============")
if __name__ == "__main__":
    main()