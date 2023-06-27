import json
import random
import string
from password import BookTicket


class TwoFactor(BookTicket):

    letters = ('a', 'A', 'O', 't', 'E', 'I', 'S')  # potential class attribute
    transformed_letters = ('@', '4', '0', '+', '3', '1', '5')   # potential class attribute
    dict_trans = {letter: tran for letter, tran in zip(letters, transformed_letters)}
    
    def __init__(self, list_words, min_word_len, max_word_len, num_words, first, last, middle=None):
        super().__init__(first, last, middle)
        self.min_word_len = min_word_len
        self.max_word_len = max_word_len
        self.num_words = num_words
        self.list_words = list_words

    

    def generate_twofac_password(self):

        draft_password = random.sample(self.list_words, self.num_words)
        upper_lower_char_psw = ''.join(map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), draft_password))

        dict_transform = {letter: tran for letter, tran in zip(TwoFactor.letters, TwoFactor.transformed_letters)}
        xform = str.maketrans(dict_transform)

        return upper_lower_char_psw.translate(xform) + random.choice(string.punctuation)
    
    def confirm_employee_ticket(self):
        print(f"Two factor authentication password: {self.generate_twofac_password()}")
        return super().confirm_employee_ticket()

        

f = open("words/words.txt")
print(f.name)
# i = 0
# for file in f:
#     print(file)
#     i += 1
#     if i == 5:
#         break

with open("words/words_dictionary.json", "r") as file:
    word_data = json.load(file)

j = 0
for key, val in word_data.items():
    print(key, val)
    j += 1
    if j == 5:
        break


min_word_len = 4
max_word_len = 6
num_words = 3
list_words = list(word_data.keys())  # potential class attribute
set_words = set(list_words)
cleaned_words = list(filter(lambda word: min_word_len <= len(word) <=
                            max_word_len, set_words))

print(cleaned_words[:10])

# generate a password.
sample_words = random.sample(cleaned_words, num_words)
print(sample_words)
test_psw = ''.join(sample_words)
print(test_psw)

# Now we can write the algorithm

# text = 'apple'


def upper_lower_func(psw):
    return ''.join(map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), psw))


upper_lower_psw = upper_lower_func(test_psw)
print(upper_lower_psw)
# print(random.choice(string.punctuation))
dict_trans = dict()
letters = ('a', 'A', 'O', 't', 'E', 'I', 'S')  # potential class attribute
trans = ('@', '4', '0', '+', '3', '1', '5')   # potential class attribute
dict_trans = {letter: tran for letter, tran in zip(letters, trans)}
print(dict_trans)


def letter_to_char(upper_lower_word):
    dict_trans = {letter: tran for letter, tran in zip(letters, trans)}
    xform = str.maketrans(dict_trans)

    return upper_lower_word.translate(xform) + random.choice(string.punctuation)


end_psw = letter_to_char(upper_lower_psw)
print(end_psw)

# xform = str.maketrans(dict_trans)
# print(xform)

# end_psw = upper_lower_psw.translate(xform) + random.choice(string.punctuation)
# print(end_psw)
