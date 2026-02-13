# Requirements
'''Design an Exam class. 
Methods to think about: 
• start exam (object method) 
• submit exam (object method) 
• calculate score (object method) 
• update pass marks (class method)'''


import logging
from datetime import datetime
logging.basicConfig(
    filename="Exam.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)
class Exam:
    pass_marks=21
    def __init__(self,stuname,total_ques,duration=60, marks_per_question=5):
        self.stuname=stuname
        self.total_ques=total_ques
        self.correct=0
        self.submitted=False
        self.marks_per_question = marks_per_question
        self.duration = duration  
        self.score = 0
        self.start_time = None
        self.submit_time = None


    def start_exam(self):
        self.submitted=False
        self.correct=0
        self.score = 0
        self.start_time = datetime.now()
        logging.info("Exam started for %s with %d questions, duration %d mins", 
                     self.stuname, self.total_ques, self.duration)
        print(f'Exam started for {self.stuname} with {self.total_ques} questions.')


    def submit_exam(self, correct_ans):
        if correct_ans <= self.total_ques:
            self.correct = correct_ans
            self.submitted = True
            self.submit_time = datetime.now()
            logging.info("%s submitted exam with %d correct answers", self.stuname, self.correct)
            print(f'Exam submitted by {self.stuname}')
        else:
            logging.warning("%s tried to submit more correct answers than total questions", self.stuname)
            print("Exam not submitted: correct answers cannot exceed total questions")


    def calculate_score(self):
        if self.submitted:
            self.score = self.correct * self.marks_per_question
            result = "passed" if self.score >= Exam.pass_marks else "failed"
            logging.info("%s scored %d and %s the exam", self.stuname, self.score, result)
            print(f'Student {self.stuname} {result} with {self.score} marks')
        else:
            logging.warning("%s tried to calculate score without submitting", self.stuname)
            print("Exam not submitted yet")

            
    @classmethod
    def update_pass(cls,new_marks):
        cls.pass_marks=new_marks
        logging.info("Pass marks updated to %d", new_marks)

e=Exam("sanjana",10)
e.start_exam()
e.submit_exam(6)
e.calculate_score()
Exam.update_pass(21)