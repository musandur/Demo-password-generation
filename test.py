from itertools import combinations, permutations
import random


first_seat = 1
last_seat = 3
num_seats = 3
confidential_list = list(range(0, 100)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#confidential_list = range(1, 2+1)

seats = list(range(first_seat, last_seat + 1))
#num_code = permutations(list(confidential_list))
num_code = random.sample(confidential_list, 3)

# number_of_seats = 0
# num_code = range(1, 3+1)
# print(list(num_code))

# num_code = random.sample(range(101, 999), 3)
# print(num_code)

# str_code = ' '.join(str(element) for element in num_code)
# print(list(str_code))

print(num_code)
str_code = ''.join(str(element) for element in num_code)
print(str_code)
list_str_code = list(str_code)

print(list_str_code)

lst_copy = list_str_code.copy()
random.shuffle(lst_copy)
print(lst_copy)

#list(permutations())