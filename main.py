def main():
    book_path = "books/frankenstein.txt"
    texts = get_book_text(book_path)
    characters = get_character_count(texts)
    sorted_char = sorted(characters.items(), reverse=True, key=lambda i: i[1])

    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(texts)} words found in the document")
    #Sorted ver
    for character in sorted_char:
        print(f"The {character[0]} was found {character[1]} times")
    print("---End Report---")
    
    '''
    A-Z Ver
    for character in characters:
        print(f"The {character} was found {characters[character]} times")
    '''
def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_character_count(file_contents):
    characters = {"a": 0,"b": 0,"c": 0,"d": 0,"e": 0,"f": 0,"g": 0,"h": 0,"i": 0,
                  "j": 0,"k": 0,"l": 0,"m": 0,"n": 0,"o": 0,"p": 0,"q": 0,"r": 0,
                  "s": 0,"t": 0,"u": 0,"v": 0,"w": 0,"x": 0,"y": 0,"z": 0}
    lower_case_text = file_contents.lower()
    for character in characters:
        char_count = 0
        for i in lower_case_text:
            if i in character:
                char_count += 1
        characters[character] = char_count
    return characters    

main()