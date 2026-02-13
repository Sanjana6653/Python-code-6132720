# Requirements
'''Design a LibraryBook class. 
Methods to think about: 
• issue book (object method) 
• return book (object method) 
• calculate fine (object method) 
• update fine per day (class method)'''

import logging

logging.basicConfig(
    filename="LibraryBook.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class LibraryBook:
    fine_per_day = 5

    def __init__(self, book_name, book_author, book_publication):
        self.book_name = book_name
        self.book_author = book_author
        self.book_publication = book_publication
        self.days_issued = 0
        self.issued = False
        self.borrower = None

    def issue_book(self, borrower_name, days):
        if not self.issued:
            self.borrower = borrower_name
            self.days_issued = days
            self.issued = True
            logging.info("Book '%s' issued to %s for %s days", self.book_name, self.borrower, self.days_issued)
            return True
        logging.warning("Attempted to issue book '%s' to %s but it is already issued", self.book_name, borrower_name)
        return False

    def return_book(self):
        if self.issued:
            self.issued = False
            logging.info("Book '%s' returned by %s", self.book_name, self.borrower)
            self.borrower = None
            self.days_issued = 0
            return True
        logging.warning("Attempted to return book '%s' but it was not issued", self.book_name)
        return False

    def calculate_fine(self, actual_days_kept):
        if actual_days_kept > self.days_issued:
            fine = (actual_days_kept - self.days_issued) * LibraryBook.fine_per_day
            logging.info("Fine for book '%s' kept %s days by %s is %s", self.book_name, actual_days_kept, self.borrower, fine)
            return fine
        logging.info("No fine for book '%s' returned by %s", self.book_name, self.borrower)
        return 0

    @classmethod
    def update_fine(cls, new_fine):
        if new_fine >= 0:
            cls.fine_per_day = new_fine
            logging.info("Fine per day updated to %s", new_fine)
            return True
        logging.warning("Attempted to set invalid fine per day: %s", new_fine)
        return False


b1=LibraryBook("python","sanjana","bvrit")
b1.issue_book("sanjana",5)
b1.issue_book("rachu",8)
b1.return_book()
b1.calculate_fine(8)

LibraryBook.update_fine(10)
            
