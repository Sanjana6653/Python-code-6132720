# Requirements
'''Design a LibraryBook class. 
Methods to think about: 
• issue book (object method) 
• return book (object method) 
• calculate fine (object method) 
• update fine per day (class method)'''

class LibraryBook :
    fine_per_day=5
    def __init__(self,book_name,book_author,book_publication):
        self.book_name=book_name
        self.book_author=book_author 
        self.book_publication = book_publication
        self.days_issued=0
        self.issued=False
        self.borrower=None
    def issue_book(self,borrower_name,days):
        if not self.issued:
            self.borrower=borrower_name
            self.days_issued=days
            self.issued=True
            print("Book is issued")
        else:
            print("Book is already issued")
    def return_book(self,days_kept):
        if self.issued:
            self.issued=False
            print("book is returned")
        else:
            print("Book is not issued")
        
    def calculate_fine(self, actual_days_kept):
        if actual_days_kept > self.days_issued:
            fine = (actual_days_kept - self.days_issued) * LibraryBook.fine_per_day
            print("fine for book is",fine)
            
        else:
            print("No fine")
            
    @classmethod
    def update_fine(cls,new_fine):
        cls.fine_per_day=new_fine
        print("new fine is ",new_fine)

b1=LibraryBook("python","sanjana","bvrit")
b1.issue_book("sanjana",5)
b1.issue_book("rachu",8)
b1.return_book(8)
b1.calculate_fine(8)

LibraryBook.update_fine(10)
            
