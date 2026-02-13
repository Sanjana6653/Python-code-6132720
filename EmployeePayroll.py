#Requirements
'''. Employee Payroll System (Corporate Domain) 
Design an Employee class. 
Methods to think about: 
• calculate salary (object method) 
• apply leave deduction (object method) 
• display payslip (object method) 
• update hra percentage (class method)'''

import logging

logging.basicConfig(
    filename="Employee.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Employee:
    hra_percentage = 20 

    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.leave_days = 0
        self.salary = 0

    def calculate_salary(self):
        hra_amount = self.basic_salary * (Employee.hra_percentage / 100)
        self.salary = self.basic_salary + hra_amount - self.leave_days * (self.basic_salary / 30)
        logging.info("Salary calculated for %s: %s (HRA %s%%, leave days %s)", 
                     self.name, self.salary, Employee.hra_percentage, self.leave_days)
        return self.salary

    def apply_leave_deduction(self, leave_days):
        self.leave_days += leave_days
        logging.info("Applied %s leave day(s) deduction for %s", leave_days, self.name)
        
        self.calculate_salary()
        return self.salary

    def display_payslip(self):
        logging.info("Payslip for %s: Basic Salary %s, HRA %s%%, Leave Days %s, Net Salary %s",
                     self.name, self.basic_salary, Employee.hra_percentage, self.leave_days, self.salary)
        return {
            "Employee": self.name,
            "Basic Salary": self.basic_salary,
            "HRA %": Employee.hra_percentage,
            "Leave Days": self.leave_days,
            "Net Salary": self.salary
        }

    @classmethod
    def update_hra_percentage(cls, new_hra):
        if new_hra >= 0:
            cls.hra_percentage = new_hra
            logging.info("HRA percentage updated to %s%%", new_hra)
            return True
        logging.warning("Attempted to set invalid HRA percentage: %s", new_hra)
        return False

e = Employee(101, "Sanjana", 50000)
e.calculate_salary()
e.apply_leave_deduction(2)
e.display_payslip()
Employee.update_hra_percentage(25)
e.calculate_salary()
e.display_payslip()
