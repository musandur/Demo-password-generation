from itertools import combinations, permutations
import random
# random.seed(42)

from twofactor import TwoFactorPassword
from file_import_cleaned import clean_file
from password import Password


psw_object = Password("musa", "ndur")
first_pwd = psw_object.first_password()
print(f"First password: {first_pwd}")

file_path = "words/words_dictionary.json"

list_words = clean_file(file_path)
number_of_words = 3

two_fac_object = TwoFactorPassword(list_words, number_of_words, "musa", "ndur")
twofac_pwd = two_fac_object.generate_twofac_password()
print(f"Two fac password: {twofac_pwd}")

print("*"*50)
two_fac_object.print_registration_details(first_pwd, twofac_pwd)

print("*"*50)
print(two_fac_object.store_registration_info(first_pwd, twofac_pwd))