class Person:
    def __init__(self,name):
        self.name=name
    def get_info(self):
        print("Aty:",self.name)

class Employee(Person):
    def job(self,job_name):
        print("Aty:",self.name,"Zhumys:", job_name)
Employee_obj=Employee("Nurs")
Employee_obj.job("programmer")