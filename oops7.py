#Elecronic device
#pocket gadget
# phone
class Elecronic_device():
    old = 9
    electric_source = "A.C"
    def name_Elecronic_device(self):
        print(f"this electronic device is {self.old} years old")

class pocket_gadget(Elecronic_device):
     old = 21
     electric_source = "Battery"
     def name_pocket_gadget(self):
         print(f"this gadget is {self.old} years old")

class phone(pocket_gadget):
    company = "xiomi"
    def name_phone(self):
        print(f"this phone is {self.old} years old")

first = Elecronic_device
first.name_Elecronic_device(first)

second = pocket_gadget
second.name_Elecronic_device(second)
second.name_pocket_gadget(second)

third = phone

third.name_Elecronic_device(second)
third.name_pocket_gadget(second)
third.name_phone(third)