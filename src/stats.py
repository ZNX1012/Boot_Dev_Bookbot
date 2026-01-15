def count_book_words(book_text):
    words_number = len(book_text.split())
    return words_number

def count_book_characters(book_text):
    #first create a dictionary for the <char: count> values
    character_count = {}
    
    #convert the book_text string into a list of characters
    character_list = list(book_text.lower())

    #go through all characters and add +1 to each find
    for i in character_list:
        # i is each single character in the book
        # each character i itself is a key in the dictionary
        # first check the current number saved in the dictionary
        try:
            current_number = character_count[i]
        except KeyError:
             # if there is no key for that character then the number is 0
            current_number = 0
        character_count[i] = current_number + 1
    return character_count

#Create a sorted list of dictionarys.
#Structure should look like this:
#[{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]
def sort_dict(character_dict):
    new_sorted_list = []
    for key in character_dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = character_dict[key]
        new_sorted_list.append(new_dict)


    new_sorted_list.sort(reverse=True, key=sort_on)
    return new_sorted_list

#A helper function to be able to sort each dictionary on the key="num"
#.sort() will call this fuction on each dictionary and get the key.
def sort_on(items):
    return items["num"]