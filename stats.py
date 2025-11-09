def get_total_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    lower_char = text.lower()

    for char in lower_char:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count

def sort_on_dictionary(dictionary):
    char_list = []

    for char, value in dictionary.items():
        sort_list = {"char": char, "num": value}
        char_list.append(sort_list)
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
    

