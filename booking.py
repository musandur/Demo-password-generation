from itertools import combinations
import random

class BookTicket:
    first_seat = 1
    last_seat = 3
    confidential_list = list(range(0, 100))
    number_of_seats = 0
    list_participants = []
    special_char = ['#', '%', '@', '$', '&']
    

    def __init__(self, first, last, middle=None):
        self.name = first
        self.last = last
        if middle:
            self.middle = middle
        else:
            self.middle = ''
        #tuple_code = next(BookTicket.num_code)
        tuple_code = random.sample(BookTicket.confidential_list, 5)
        full_code = list(''.join(str(element) for element in tuple_code)) + \
            random.sample(list(self.name + self.middle + self.last), 2) + random.sample(BookTicket.special_char, 2)
        random.shuffle(full_code)
        self.ticket_code = ''.join(full_code)
        BookTicket.number_of_seats += 1
        self.number_of_seat = BookTicket.number_of_seats
        BookTicket.list_participants.append(self.__dict__)

    def is_event_sold_out(self):
        return BookTicket.number_of_seats > BookTicket.last_seat

    def confirm_employee_ticket(self):
        print(f"Name: {self.name}")
        if self.middle:
            print(f"Middle name: {self.name}")
        print(f"Surname: {self.last}")
        print(f"Seat number: {self.number_of_seat}")
        print(f"Ticket code: {self.ticket_code}")

        

if __name__ == '__main__':
    print("BookTicket class created successfully!")

    test1 = BookTicket('musa', 'ndur')
    test1.confirm_employee_ticket()

    print(BookTicket.list_participants)
    # print(random.sample(BookTicket.special_char, 2))