class A:
    class_var1 = "this is class variable of class A"
    def __init__(self):
        self.instance_var1 = "this is instance variable of class A"

class B(A):
    class_var2 = "this is class variable of class B"
    def __init__(self):
        super().__init__()
        self.instance_var2 = "this is instance variable of class B"

a = A()
b = B()
print(a.instance_var1)
print(b.instance_var1)
print(b.class_var2)