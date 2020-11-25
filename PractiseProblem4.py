
'''
You have to take the number as a input from userYiu have to find the next pallindrome corresponding to that number.
Your input should be 'number of test cases' and then all the test cases as input from the user.
'''
def pallindrome(num):
     reverse = num[::-1]
     if reverse == num:
         return True
     else:
         return False

def nextpallindrome(inputnumber):
    g = inputnumber
    while inputnumber >0:
        if pallindrome(str(inputnumber)):
            print(f"the next pallindrome  of {g} is {inputnumber}")
            break;
        else:
            inputnumber+= 1

if __name__ == "__main__":
 print(" Enter the number of input or number of test cases")
inp = input()
intinp = int(inp)
number = []
for i in range(intinp):
    print(f" Enter the {i} th number")
    num = int(input())
    number.append(num)


for i in number:
    nextpallindrome(i)