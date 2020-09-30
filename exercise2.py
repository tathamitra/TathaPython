# Faulty Calculator
# 45*3 =555,56+9= 77, 56/6 =4

print("Enter first number")
inpnum1 = int(input())
print("Enter second number")
inpnum2 = int(input())
print("Enter operator")
operator = input()

s = set([45, 3, 56, 9, 6])
s1 = set([inpnum1, inpnum2])
if inpnum1 == 45 and inpnum2 == 3 and operator == "*":
    print("555")
elif inpnum1 == 56 and inpnum2 == 9 and operator == "+":
    print("77")
elif inpnum1 == 56 and inpnum2 == 6 and operator == "/":
    print("4")
elif operator == "*":
        print(inpnum1 * inpnum2)
elif operator == "+":
        print(inpnum1 + inpnum2)
elif operator == "-":
        print(inpnum1 - inpnum2)
elif operator == "/":
        print(inpnum1 / inpnum2)
else:
    print("answer is wrong")
