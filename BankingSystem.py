# Requirements
'''Design a BankAccount class. 
Methods to think about: 
• withdraw money (object method) 
• deposit money (object method) 
• display account details (object method) 
• update minimum balance (class method)'''

class Bank:
    bank_name="SBI"
    bank_loc="Hyderabad"
    bank_num=12345
    bank_mgr="scottt"
    min_balance=1000
    def __init__(self,name,age,location,pan,phone,balance):
        self.name=name 
        self.age=age
        self.location=location 
        self.pan=pan 
        self.phone=phone 
        self.balance=balance 

    def withdraw(self,amount):
        if self.balance-Bank.min_balance>=amount:
            self.balance=self.balance-amount
            print(f'Balance amount is {self.balance}')
        else:
            print("Balance not available")

    def deposit(self,money):
        if money>0:
            self.balance=self.balance+money
            print(f'money deposited successfully and total available amount is {self.balance}')
        else:
            print("Enter valid amount to deposit")
    def display(self):
        print(self.name,self.age,self.phone,self.balance)
    @classmethod
    def update_balance(cls,new_minimum):
        old_min_balance=cls.min_balance
        cls.min_balance=new_minimum
        print(f'Updated minimum balance from {old_min_balance} to {new_minimum}')

b1=Bank("Sanjana",21,"Hyderabad","pzip345",1234567890,10000)
print(b1.bank_name,b1.bank_loc,b1.bank_mgr,b1.bank_name)
b1.display()
b1.deposit(1)
b1.display()
b1.withdraw(2000)
b1.display()
b1.update_balance(200000)
b1.display()

b2 = Bank("Ravi", 25, "Delhi", "abcd1234", 9876543210, 5000)
print(b2.bank_name,b2.bank_loc,b2.bank_mgr,b2.bank_name)
b2.display()
b2.deposit(1)
b2.display()
b2.withdraw(5002)
b2.display()
b2.update_balance(9999)
b2.display()

    
