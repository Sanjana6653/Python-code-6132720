#Requirements
'''Design a HostelRoom class. 
Methods to think about: 
• allocate room (object method) 
• vacate room (object method) 
• calculate monthly fee (object method) 
• update room rent (class method) '''

import logging

logging.basicConfig(
    filename="HostelRoom.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class HostelRoom:
    room_rent = 1000  # default rent per month

    def __init__(self, name, rollno, clas):
        self.name = name
        self.rollno = rollno
        self.clas = clas
        self.allocated = False
        self.months = 0

    # Object method: Allocate room
    def allocate(self, months):
        if not self.allocated:
            self.allocated = True
            self.months = months
            logging.info("Room allocated to %s for %s months", self.name, self.months)
            return True
        logging.warning("Attempted to allocate room to %s but room already allocated", self.name)
        return False

    # Object method: Vacate room
    def vacate(self):
        if self.allocated:
            self.allocated = False
            logging.info("Room vacated by %s", self.name)
            return True
        logging.warning("Attempted to vacate room for %s but room was not allocated", self.name)
        return False

    # Object method: Calculate monthly fee
    def calculate_fee(self):
        if self.allocated:
            fee = self.months * HostelRoom.room_rent
            logging.info("Rent for %s for %s months is %s", self.name, self.months, fee)
            return fee
        logging.warning("Attempted to calculate fee for %s but room is not allocated", self.name)
        return 0

    # Class method: Update room rent
    @classmethod
    def update_room(cls, new_rent):
        if new_rent > 0:
            cls.room_rent = new_rent
            logging.info("Hostel room rent updated to %s", new_rent)
            return True
        logging.warning("Attempted to set invalid room rent: %s", new_rent)
        return False


h = HostelRoom("Sanjana", 53, 9)
h.allocate(8)
h.calculate_fee()
HostelRoom.update_room(5000)
h.calculate_fee()
h.vacate()
