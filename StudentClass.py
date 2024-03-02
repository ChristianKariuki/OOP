import random
from datetime import datetime

class Student:
    def __init__(self):
        self.student_id = self.random_student_id()
        self.name = self.random_name()
        self.dob = self.random_dob()
        self.classification = self.random_classification()

    def random_student_id(self):
        return f"{random.randint(10000, 99999)}"

    def random_name(self):
        names = ["John Doe", "Jane Smith", "Alice Johnson", "Robert Brown"]
        return random.choice(names)

    def random_dob(self):
        year = random.randint(1990, 2005)
        month = random.randint(1, 12)
        day = random.randint(1, 28) 
        return datetime(year, month, day)

    def random_classification(self):
        classifications = ["Fr", "So", "Jr", "Sr"]
        return random.choice(classifications)

    def calculate_age(self):
        today = datetime.now()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

    def registration_dates(self):
        dates = {
            'Sr': '4/1 thru 4/3',
            'Jr': '4/4 thru 4/6',
            'So': '4/7 thru 4/9',
            'Fr': '4/10 thru 4/12'
        }
        return dates.get(self.classification, "Unknown classification")

    def get_age(self):
        return self.calculate_age()

    def get_registration_dates(self):
        return self.registration_dates()
