'''
Take age or year as input from user and tell them when will they be 100 years old.
Don't use module like datetime and dateutils.
They can then optionally provide a year and your program must tell their age in that year

'''

print(" Enter your age or the year of birth")
inp = input()
if len(inp) == 4 and int(inp) <= 2019:
    Age = 2020 - int(inp)
elif len(inp) <= 2:
    Age = int(inp)
elif len(inp) == 3:
    print("You are the oldest person alive")
elif int(inp) >= 2020:
    print("you are not born yet")
else:
    print("Enter a valid age or year")
    exit()

print("DO you want to know your age in a year YES/NO")
option = input()

if option == 'YES':
    print("Print the Year")
    year = int(input())
    yearsAway =  year - 2020
    AgeOnYear = Age + yearsAway
    if yearsAway >=0:
     print(f"In years {year} you will be {AgeOnYear} years old")
    else:
        print(f"In years {year} you were {AgeOnYear} years old")
elif option == 'NO':
    print("Thanks for playing")
    exit()
else:
    print("Not a valid option")
    exit()