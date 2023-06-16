from booking import BookTicket
import random

# c1 = BookTicket('musa', 'ndur')
# print(c1.ticket_code)
# c2 = BookTicket('mbay', 'diop')
# print(c2.ticket_code)
# c3 = BookTicket('demba', 'sy')
# print(c3.ticket_code)
# c4 = BookTicket('sira', 'ba')
# print(c4.ticket_code)


# Next write an interactive code for the user to input
# there data. Then check if the event is sold out.
# then sell a ticket to the customer or inform sold out decision

print("++++++++++++++++++++++++++++")
while BookTicket.number_of_seats < BookTicket.last_seat:
    try:
        first_name = input("Enter your first name: ")
        middle_name = input(
            "Enter your middle name. (write x if you do not have a middle name) ")
        if middle_name == 'x':
            middle_name = None

        last_name = input("Enter your last name: ")

        new_ticket = BookTicket(first_name, last_name, middle_name)
        new_ticket.confirm_employee_ticket()
    except StopIteration:
        print("No more seats available.")
        break
print("No more seats available")