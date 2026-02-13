#Requirements
'''Design a Recharge class. 
Methods to think about: 
• do recharge (object method) 
• check validity (object method) 
• show balance (object method) 
• update recharge plans (class method) '''

import logging
from datetime import datetime, timedelta

logging.basicConfig(
    filename="Recharge.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Recharge:
    recharge_plan = 300  
    default_validity_days = 30

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.balance = 0
        self.valid_until = None
        self.last_recharge_time = None


    def do_recharge(self, amount):
        if amount <= 0:
            logging.warning("%s tried to recharge with an invalid amount: %s", self.name, amount)
            return False
        self.balance += amount
        self.valid_until = datetime.now() + timedelta(days=Recharge.default_validity_days)
        self.last_recharge_time = datetime.now()
        logging.info("%s topped up %s INR. Current balance: %s", self.name, amount, self.balance)
        return True

    def check_validity(self):
        if self.valid_until and datetime.now() <= self.valid_until:
            logging.info("%s's recharge is still valid until %s", self.name, self.valid_until.strftime('%Y-%m-%d'))
            return True
        logging.info("%s has no valid recharge or it has expired", self.name)
        return False

  
    def show_balance(self):
        logging.info("%s checked their balance. Current balance: %s INR", self.name, self.balance)
        return self.balance

    @classmethod
    def update_recharge_plan(cls, new_plan):
        if new_plan > 0:
            cls.recharge_plan = new_plan
            logging.info("Recharge plan updated to %s INR", new_plan)
            return True
        logging.warning("Attempted to set an invalid recharge plan: %s", new_plan)
        return False

r = Recharge("Sanjana", "9876543210")
r.do_recharge(300)
r.show_balance()
r.check_validity()
Recharge.update_recharge_plan(400)
