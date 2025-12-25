from stats import get_num_words
from stats import get_num_chars
from stats import sort_dictionaries
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_content = file.read()
    return file_content

def print_report(my_list,num):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for entry in my_list:
        print(f"{entry['name']}: {entry['num']}")
    print("============= END ===============")



def main():
    #path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    res = get_book_text(sys.argv[1])
    ans = get_num_words(res)
    chars_dict = get_num_chars(res)
    uttar = sort_dictionaries(chars_dict)
    print_report(uttar,ans)

main()    
        