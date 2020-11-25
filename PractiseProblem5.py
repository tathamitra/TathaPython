'''
You are given a list which contains some numbers.You have to print a list of next pallindromes only
if the number is greater than 10 otherwise you print that number
'''

def pallindrome(num):
    reverse = num[::-1]
    if reverse == num:
        return True
    else:
        return False


def nextpallindrome(inputnumber):
    while inputnumber > 0:
        if pallindrome(str(inputnumber)):
            break;
        else:
            inputnumber += 1
    return inputnumber

if __name__ == "__main__":
 l1 =[12,7,11,56,102]

 for index,value in enumerate(l1):
    if value<=10:
        value = value
    else:
        k = nextpallindrome(value)
        l1[index] = k

print("this is",l1)