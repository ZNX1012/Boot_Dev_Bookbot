from stats import count_book_words, count_book_characters, sort_dict

def main():
    # get book text as string
    book_text = get_book_text("../books/frankenstein.txt")

    # get the word number of the text
    word_number = count_book_words(book_text)

    # get the number of each character as a dictionary
    char_number = count_book_characters(book_text)

    # sort the dictionary and get a sorted list of dicrionarys
    sorted_list = sort_dict(char_number)

    # print everything to the screen
    print_report(word_number, sorted_list)


def get_book_text(path):
    text = ""
    with open(path) as file:
        text = file.read()
    return text

def print_report(word_number, sorted_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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


main()