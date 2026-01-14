def get_book_text(path):
    text = ""
    with open(path) as file:
        text = file.read()
    return text

def get_book_text_words(book_text):
    words_number = len(book_text.split())
    return words_number

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_number = get_book_text_words(book_text)
    print(f"Found {word_number} total words")

if __name__ == "__main__":
    main()