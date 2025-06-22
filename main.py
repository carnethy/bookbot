from stats import word_count, character_count, sorted_character_count
import sys
if len(sys.argv)  != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
def get_book_text (file_path: str):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
def main():
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    words = word_count(book_text)
    characters = character_count(book_text)
    sorted_characters = sorted_character_count(characters)
    #print(words)
    #print(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        char = character["char"]
        num = character["num"]
        
        if char.isalpha():
            print(f"{char}: {num}")

           
main()