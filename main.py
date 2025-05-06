from stats import get_num_words, get_character_count, sort_dictionary
import sys

def sort_on(dict):
    return dict["num"]

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    string = ""
    with open(sys.argv[1]) as f:
        string = f.read()
    num_words = get_num_words(string)
    char_count = get_character_count(string)
    sorted_list = sort_dictionary(char_count)

    print("============ Bookbot ============")
    print("Analyzing book found at books/frankenstein.txt..")
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ---------")
    for i in sorted_list:
         print(f"{i["name"]}: {i["num"]}")
    print("============= END ===============")
main()