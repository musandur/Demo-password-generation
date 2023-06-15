from itertools import combinations
import random


class BookTicket:
    first_seat = 1
    last_seat = 3
    seats = list(range(first_seat, last_seat + 1))
    num_code = combinations(seats, 3)
    number_of_seats = 0

    def __init__(self, first, last, middle=None):
        self.name = first
        self.last = last
        if middle:
            self.middle = middle
        else:
            self.middle = ''
        tuple_code = next(BookTicket.num_code)
        full_names = list(''.join(str(element) for element in tuple_code)) + \
            random.sample(list(self.name + self.middle + self.last), 2)
        random.shuffle(full_names)
        self.ticket_code = ''.join(full_names)
        BookTicket.number_of_seats += 1

    def is_event_sold_out(self):
        return BookTicket.number_of_seats > BookTicket.last_seat

    def confirm_employee_ticket(self):
        for key, val in self.__dict__.items():
            print(f"{key}: {val}")
        print("+++++++++++++++++++++")


if __name__ == '__main__':
    print("BookTicket class created successfully")
