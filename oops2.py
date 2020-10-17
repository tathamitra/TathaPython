class Employee:
    no_of_leaves = 8
    def __init__(self,salary,designation):
        self.salary = salary
        self.desidnation = designation

    def details(self):
        return f"the details for {self.name} is Empid:{self.empid},age: {self.age},salary:{self.salary},"

    @classmethod
    def leave_change(cls,numberofleaves):
        cls.no_of_leaves = numberofleaves


tatha = Employee(10000,"test")

print(tatha.salary)
print(tatha.no_of_leaves)
tatha.leave_change(34)
print(tatha.no_of_leaves)