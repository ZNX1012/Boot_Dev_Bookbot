from stats import count_book_words, count_book_characters, sort_dict
import sys

def main():
    #get book path from argv[1]
    book_path = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py ../books/<path_to_book> OR any <path_to_book> in .txt format")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    # get book text as string
    book_text = get_book_text(book_path)

    # get the word number of the text
    word_number = count_book_words(book_text)

    # get the number of each character as a dictionary
    char_number = count_book_characters(book_text)

    # sort the dictionary and get a sorted list of dicrionarys
    sorted_list = sort_dict(char_number)

    # print everything to the screen
    print_report(book_path, word_number, sorted_list)

# Read the text from the given book and return it as a string
def get_book_text(path):
    text = ""
    with open(path) as file:
        text = file.read()
    return text

# Print the report to sdtout
def print_report(book_path, word_number, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_number} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        #each i is a dictionary: {"char": "b", "num": 4868} sorted by "num"
        if i["char"].isalpha(): #check either the character is a alphabetical letter or something else
            print(f"{i["char"]}: {i["num"]}")
        else:
            #skip anything else besides alphabetical letters
            continue

# Starting point of the project
main()