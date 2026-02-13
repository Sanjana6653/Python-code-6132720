# Requirements
'''Design an Order class. 
Methods to think about: 
• place order (object method) 
• cancel order (object method) 
• calculate total price (object method) 
• update tax percentage (class method)'''

import logging

logging.basicConfig(
    filename="Order.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Order:
    tax_percentage = 20

    def __init__(self, order_id, name):
        self.order_id = order_id
        self.name = name
        self.items = {}
        self.placed = False

    def place_order(self, items):
        if not self.placed:
            self.items = items
            self.placed = True
            logging.info("Order placed successfully for %s with items: %s", self.name, self.items)
            return True
        logging.warning("Attempted to place order for %s but order is already placed", self.name)
        return False

    def cancel_order(self):
        if self.placed:
            self.placed = False
            self.items = {}
            logging.info("Order canceled for %s", self.name)
            return True
        logging.warning("Attempted to cancel order for %s but no order was placed", self.name)
        return False

    def cal_total_price(self):
        if self.placed:
            sub_total = sum(self.items.values())
            tax_amount = sub_total * (Order.tax_percentage / 100)
            total = sub_total + tax_amount
            logging.info("Total amount for %s is %s (including %s%% tax)", self.name, total, Order.tax_percentage)
            return total
        logging.warning("Attempted to calculate total for %s but order is not placed", self.name)
        return 0

    @classmethod
    def update_tax(cls, new_tax):
        if new_tax >= 0:
            cls.tax_percentage = new_tax
            logging.info("Tax percentage updated to %s%%", new_tax)
            return True
        logging.warning("Attempted to set invalid tax percentage: %s", new_tax)
        return False


o=Order(101,"sanjana")
o.cancel_order()     
o.place_order({"Laptop":70000,"Phone":30000})  
o.cal_total_price()
