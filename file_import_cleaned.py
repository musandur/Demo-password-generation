import json


def clean_file(file_path, min_word_len=4, max_word_len=6):

    '''
    The function opens the file containing the universe of words that we will use to build the two factor authentication codes 
    and returns a list of these words

    Inputs:
    file_path: path to the file
    min_word_len: minimal length allowed for a word to be appended in the list
    max_word_len: maximum length allowed for a word to be appended in the list

    return: 
    list of words with length between min_word_len and max_word_len

    '''

    with open(file_path, "r") as f:
        word_data = json.load(f)

    list_words = list(word_data.keys())
    set_words = set(list_words)
    return list(filter(lambda word: min_word_len <= len(word) <=
                            max_word_len, set_words))


if __name__ == "__main__":
    
    print("*"*20)
    print('function called')
    print(help(clean_file))