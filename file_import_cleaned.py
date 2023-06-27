import json


def clean_file(file_path, min_word_len=4, max_word_len=6):
    with open(file_path, "r") as f:
        word_data = json.load(f)

    list_words = list(word_data.keys())
    set_words = set(list_words)
    return list(filter(lambda word: min_word_len <= len(word) <=
                            max_word_len, set_words))


if __name__ == "__main__":
    
    print("*"*20)
    print('function called')