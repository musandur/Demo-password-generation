import random
import string
from password import Password


class TwoFactorPassword(Password):

    '''
    The sub class inherits the class Password and encapsulates the two factor authentication code 

    Class attributes:
    letters: chosen letters to mapped to special characters 
    transformed_letters: special characters that replacing selected letters
    dict_trans: dictionary of letters and transfomed_letters
    number_of_registered: it records  in the fly the number of registered users.

    Instance attributes:
    list_words: the list containing the universe of words that we will use to build the two fac passwords
    num_words: Number of words chosen to build a two fac password
    '''



    number_of_registered = 0
    letters = ('a', 'A', 'O', 't', 'E', 'I', 'S')  
    transformed_letters = ('@', '4', '0', '+', '3', '1', '5')   
    dict_trans = {letter: tran for letter, tran in zip(letters, transformed_letters)}
    
    
    def __init__(self, list_words, num_words, first_name, last_name, middle_name=None):
        super().__init__(first_name, last_name, middle_name)
        self.num_words = num_words  
        self.list_words = list_words 
        TwoFactorPassword.number_of_registered += 1

    

    def generate_twofac_password(self):
        '''
        This method generates the two factor authentication password

        Return:
        the two fac password string.
        '''

        draft_password = random.sample(self.list_words, self.num_words)
        upper_lower_char_psw = ''.join(map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), draft_password))

        dict_transform = {letter: tran for letter, tran in zip(TwoFactorPassword.letters, TwoFactorPassword.transformed_letters)}
        xform = str.maketrans(dict_transform)

        return upper_lower_char_psw.translate(xform) + random.choice(string.punctuation)
    
    
    def store_registration_info(self, first_pwd, twofac_pwd):
        '''
        This method build the dictionary containg the total registration info including the full name and the two passwords.

        Inputs:
        first_pwd: the first password generated from the parent class Password
        two fact_pwd: the second password called two factor authentication generated from the child class TwoFactorPassword

        Return:
        dict_info: the dictionary containg the total registration info 

        '''

        dict_info = {}
        dict_info["Name"] = self.first_name
        if self.middle_name:
            dict_info["Middle name"] = self.middle_name
        dict_info["Surname"] =  self.last_name
        dict_info["First password"] = first_pwd
        dict_info["Two Factor password"] = twofac_pwd
        dict_info["Total number of registered users"] = self.number_of_registered
        
        return dict_info


    def print_registration_details(self, first_pwd, twofac_pwd):

        '''
        This method print the registration information.
        '''
        print(f"Name: {self.first_name}")
        if self.middle_name:
            print(f"Middle name: {self.middle_name}")
        print(f"Surname: {self.last_name}")
        print(f"First password: {first_pwd}")
        print(f"Two factor Authentication: {twofac_pwd}")
        print(f"Total number of registered users: {self.number_of_registered}")
    


if __name__ == "__main__":
    
    print("Two factor authentication class created successfully!")
