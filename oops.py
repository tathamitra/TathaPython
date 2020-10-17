class Employee:
    no_of_leaves = 8
    def details(self):
        return f"the details for {self.name} is Empid:{self.empid},age: {self.age},salary:{self.salary},"

harry = Employee()
larry = Employee()

harry.salary =200
harry.empid = 12
harry.age =34
harry.name = "harry"

larry.salary =500
larry.empid = 51
larry.age =23
larry.name = "larry"

print(harry.__dict__)
print(Employee.__dict__)
print(harry.no_of_leaves)
print(harry.details())
print(larry.details())