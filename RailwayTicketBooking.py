#requirements
"""Design a Ticket class. 
Methods to think about: 
• book ticket (object method) 
• cancel ticket (object method) 
• calculate fare (object method) 
• update base fare (class method) """


import logging
from datetime import datetime

logging.basicConfig(
    filename="Ticket.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Ticket:
    base_fare = 500 

    def __init__(self, passenger_name, train_no, seats):
        self.passenger_name = passenger_name
        self.train_no = train_no
        self.seats = seats
        self.booked = False
        self.booking_time = None

    def book_ticket(self):
        if not self.booked:
            self.booked = True
            self.booking_time = datetime.now()
            logging.info("%s booked %s seat(s) on train %s", self.passenger_name, self.seats, self.train_no)
            return True
        logging.warning("Ticket already booked for %s on train %s", self.passenger_name, self.train_no)
        return False

    def cancel_ticket(self):
        if self.booked:
            self.booked = False
            logging.info("%s canceled ticket on train %s", self.passenger_name, self.train_no)
            return True
        logging.warning("No booking found to cancel for %s on train %s", self.passenger_name, self.train_no)
        return False

    def calculate_fare(self):
        if self.booked:
            fare = self.seats * Ticket.base_fare
            logging.info("Fare for %s for %s seat(s) on train %s is %s", self.passenger_name, self.seats, self.train_no, fare)
            return fare
        logging.warning("Cannot calculate fare, ticket not booked for %s on train %s", self.passenger_name, self.train_no)
        return 0

    @classmethod
    def update_base_fare(cls, new_fare):
        if new_fare > 0:
            cls.base_fare = new_fare
            logging.info("Base fare updated to %s", new_fare)
            return True
        logging.warning("Attempted to set invalid base fare: %s", new_fare)
        return False

t = Ticket("Sanjana", "12345", 2)
t.book_ticket()
t.calculate_fare()
Ticket.update_base_fare(600)
t.calculate_fare()
t.cancel_ticket()
