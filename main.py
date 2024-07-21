def read_file(file_path):   
    with open(file_path) as f:
        return f.read()

def count_words(text):
    words_inLowerCase = (text.lower()).split()
    return len(words_inLowerCase)
    
def count_characters(text):
    text_lowered = text.lower()
    character_count = {}
    for character in text_lowered:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count    

def sort_on(dict):
    return dict["num"]

def main():
    file_path = "books/frankenstein.txt"     
    file_contents = read_file(file_path)

    WordCount = count_words(file_contents) # number of words found in the text

    character_num = count_characters(file_contents) #dictionary with key being character, and value is its occurence

    char_list = []
    for char, count in character_num.items(): #.items turn the dictionary into a list of tuples ('p', 6121)...
        if char.isalpha(): #only do the following if char is a letter
            char_dict = {"character": char, "num": count}
            char_list.append(char_dict) # after this we have a list of new dictionary with two keys "character" and "num"
    
    char_list.sort(key=sort_on, reverse=True)
    print(char_list)
    print(f"--- Begin report of {file_path} ---\n{WordCount} words found in the document")
    print()
    for dict in char_list:
        print(f"The '{dict['character']}' character was found {dict['num']}")
    print()
    print("---End of report---")


main()