# Requirements for Hospital Patient Management
'''Design a Patient class. 
Methods to think about: 
• admit patient (object method) 
• discharge patient (object method) 
• calculate bill (object method) 
• update consultation fee (class method) '''

import logging
logging.basicConfig(
    filename="Hospital.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)
class Patient:
    consultationfee=1000
    def __init__(self,name,age,disease,phone):
        self.name = name
        self.age = age 
        self.disease = disease 
        self.admitted=False
        self.days_admitted=0
        self.bill_amount=0
        self.phone= phone
    def admit(self,days):
        if not self.admitted:
            self.admitted=True
            self.days_admitted=days
            logging.info("admitted successful for %s for %d days",self.name,days)
        else:
            logging.info("Not admitted")


    def discharge(self):
        if self.admitted:
            self.admitted=False
            logging.info("%s is discharged",self.name)
        else:
            logging.info("%s is not admitted")


    def calculate_bill(self):
        if self.admitted:
            self.bill_amount=self.days_admitted*1000 + Patient.consultationfee
            logging.info("total bill is : %s",self.bill_amount)
        else:
            logging.info("patient not admitted")


    def display(self):
        logging.info("Patient Name: %s", self.name)
        logging.info("Age: %d", self.age)
        logging.info("Disease: %s", self.disease)
        logging.info("Phone: %s", self.phone)
        logging.info("Admitted: %s", self.admitted)
        logging.info("Days Admitted: %d", self.days_admitted)
        logging.info("Bill Amount: %s", self.bill_amount)
        logging.info("Consultation Fee: %s", Patient.consultationfee)

        
    @classmethod
    def update_fee(cls,new_fee):
        cls.consultationfee=new_fee
    
p=Patient("sanjana",21,"fever",1234567890)
p.admit(4)
p.calculate_bill()
p.display()
Patient.update_fee(2000)
p.calculate_bill()
p.discharge()
p.display()
