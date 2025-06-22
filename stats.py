def word_count(book_string: str):
        book_split = book_string.split()
        num_of_words = len(book_split)
        return num_of_words

def character_count(book_string: str):
        book_lower_case = book_string.lower()
        character_dictionary = {}
        for character in book_lower_case:
                if character not in character_dictionary:
                        character_dictionary[character] = 1
                else:
                        character_dictionary[character] += 1
        return character_dictionary
def sorted_character_count(dictionary):
        dictionary_list = []
        for character in dictionary:
                character_dictionary = {"char" : character, "num": dictionary[character]}
                dictionary_list.append(character_dictionary)
        dictionary_list.sort(reverse=True, key=sort_on)
        return dictionary_list
def sort_on(items):
    return items["num"]