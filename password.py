from itertools import combinations
import random

class Password:
    '''
    Parent class designed to define the first password encapsulation.

    Class attributes:
    confidential_list: the list of integers chosend to build the password
    special_char: special characters that will be used to build the password.
    

    Instance attributes: 
    first_name: User first name
    middle_name: user middle name. It is optional.
    last_name: user last name

    '''
    confidential_list = list(range(0, 100))
    special_char = ['#', '%', '@', '$', '&']
    

    def __init__(self, first_name, last_name, middle_name=None):
        self.first_name = first_name
        self.last_name = last_name
        if middle_name:
            self.middle_name = middle_name
        else:
            self.middle_name = ''
        

    def first_password(self):
        '''
        This method generates the first password as combination of randomly chosen 
        numbers from the class attribute confidential_list, randomly chosen characters 
        from the user full name, and randmly chosen special characters

        Return:
        the password string
        '''
        list_code = random.sample(Password.confidential_list, 5)
        full_code = list(''.join(str(element) for element in list_code)) + \
            random.sample(list(self.first_name + self.middle_name + self.last_name), 2) + random.sample(Password.special_char, 2)
        random.shuffle(full_code)

        return ''.join(full_code)

        

        

if __name__ == '__main__':
    
    print("BookTicket class created successfully!")

    test1 = Password('musa', 'ndur')
    print(test1.first_password())
    

    test2 = Password("Kemn", "amin", "diop")
    print(test2.first_password())
    
    