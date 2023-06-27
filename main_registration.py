from file_import_cleaned import  clean_file
from password import Password
from twofactor import TwoFactorPassword


Data_base_users = []  # this the our internal database to store the registration summary

file_path = "words/words_dictionary.json"  
list_words = clean_file(file_path)

number_of_words = 3

while True:
    
 
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name (optional): ")
    last_name = input("Enter your last name: ")

    while not (first_name.isalpha() and last_name.isalpha()):
        print("Invalid input. Please enter alphabetic characters only.")

        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

    print("*"*108)
    print("You entered:")
    print("First name:", first_name)

    if middle_name:
        while not middle_name.isalpha():
            print("Invalid input. Please enter alphabetic characters only.")

            middle_name = input("Enter your middle name (optional): ")

        print("Middle name:", middle_name)

    print("Last name:", last_name)

    registration_summary = "*" * 45 + "Registration summary" + "*" * 45
    print(registration_summary)

    # Now build the first password:
    password_object = Password(first_name, last_name, middle_name)
    first_password = password_object.first_password()

    # Now build the two factor authentication password
    two_fac_pwd_object = TwoFactorPassword(list_words, number_of_words, first_name, last_name, middle_name)
    two_fac_pwd = two_fac_pwd_object.generate_twofac_password()

    # here we print the registration details
    two_fac_pwd_object.print_registration_details(first_password, two_fac_pwd)

    # here we store the registration details our database
    Data_base_users.append(two_fac_pwd_object.store_registration_info(first_password, two_fac_pwd))

    # here we can choose to halt the registration or continue by entering 'X'
    print("\n")
    Input = input("Press 'X' if you want to end the registration:  ")
    if Input == "X":
        break


