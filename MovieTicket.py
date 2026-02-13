#reuirements
'''
Design a MovieTicket class. 
Methods to think about: 
• book seat (object method) 
• cancel booking (object method) 
• calculate ticket price (object method) 
• update ticket price (class method) 
'''

import logging
from datetime import datetime

logging.basicConfig(
    filename="MovieTicket.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class MovieTicket:
    ticket_price = 150

    def __init__(self, movie_name, total_seats):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.booked_seats = 0
        self.booking_time = None

    
    def book_seat(self, seats):
        if seats <= 0:
            print("Enter a valid number of seats to book.")
            return
        if self.booked_seats + seats <= self.total_seats:
            self.booked_seats += seats
            self.booking_time = datetime.now()
            logging.info("%d seat(s) booked for %s", seats, self.movie_name)
        else:
            logging.warning("Not enough seats available for %s", self.movie_name)
            logging.info("not enough seats available.")

    
    def cancel_booking(self, seats):
        if seats <= 0:
            logging.warning("Enter a valid number of seats to cancel.")
        if seats <= self.booked_seats:
            self.booked_seats -= seats
            logging.info("%d seat(s) cancelled for %s", seats, self.movie_name)
        else:
            logging.warning("Cannot cancel more seats than booked for %s", self.movie_name)
            

    def calculate_ticket_price(self):
        total_price = self.booked_seats * MovieTicket.ticket_price
        logging.info("Total ticket price for %s: %d", self.movie_name, total_price)
        
        return total_price

    
    @classmethod
    def update_ticket_price(cls, new_price):
        cls.ticket_price = new_price
        logging.info("Ticket price updated to %d", new_price)



m = MovieTicket("Avatar 2", 100)
m.book_seat(5)
m.calculate_ticket_price()
m.cancel_booking(2)
m.calculate_ticket_price()
MovieTicket.update_ticket_price(200)
m.calculate_ticket_price()
