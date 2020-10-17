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

tatha = Employee(10000,"test")

print(tatha.salary)
print(tatha.no_of_leaves)
tatha.leave_change(34)
print(tatha.no_of_leaves)

tatha1 = Employee.change_constructor("2000-developer")
print(tatha1.salary)
print(tatha1.designation)

tatha1.print_message("tatha")
Employee.print_message("mark")

