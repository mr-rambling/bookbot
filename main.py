def main():
    book_path = "books/frankenstein.txt"
    book = get_text(book_path)
    report(count_words(book), count_char(book))

def count_words(book) -> int:
    words = book.split()
    return len(words)

def get_text(path) -> str:
    with open(path) as f:
        return f.read()    
    
def count_char(book) -> dict:
    lowercase_book = book.lower()
    count = {}
    for char in lowercase_book:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def report(word_count, char_counts):
    character_data = []
    print("--- Begin Report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document \n")

    for key in char_counts.keys():
        if key.isalpha():
            character_data.append({"char": key, "count":char_counts[key]})

    character_data.sort(reverse=True, key=sort_on)

    for character in character_data:
        print(f"The '{character["char"]}' character was found {character["count"]} times")

    print("--- End Report ---")

def sort_on(dict):
    return dict["count"]

main()