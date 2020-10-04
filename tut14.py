#function
# print("Enter first number")
# a = int(input())
# print("Enter second number")
# b = int(input())
#
# def function1(a,b):
#     print(a+b)
# print(function1(a,b))
#
# def function2(a,b):
#     '''This is a fucntion to calculate the average'''
#     c = (a+b)/2
#     return  c
# print(function2(a,b))
# print(function2.__doc__)

#try and Exception

print("Enter first number")
a = input()
print("Enter second number")
b = input()

def function1(a,b):
    print(int(a)+int(b))
try:
 print(function1(a,b))
except Exception as e:
    print("check your inputs")
