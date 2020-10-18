class Employee:
    no_of_leaves = 8
    def __init__(self,salary,designation):
        self.salary = salary
        self.designation = designation

    def details(self):
        return f"the details for {self.name} is Empid:{self.empid},age: {self.age},salary:{self.salary},"

    @classmethod
    def leave_change(cls,numberofleaves):
        cls.no_of_leaves = numberofleaves

    @classmethod
    def change_constructor(cls,any):
        return cls(*any.split("-"))
    @staticmethod
    def print_message(name):
        print(f"hi mr {name}")


class programmer(Employee):
    def __init__(self,name,salary,designation,language):
        self.salary = salary
        self.designation = designation
        self.language = language
        self.name = name
    def programmer_details(self):
        print(f"the programmer name is {self.name},salary is {self.salary},languages known are {self.language}")

harry = programmer("Harry","500","programmer 1","[python]")
harry.programmer_details()