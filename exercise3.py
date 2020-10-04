i=0
n=18
while (i < 9):
    print("enter the number")
    inp= int(input())
    if(inp < 18 ):
        print("number is less")
        i = i+1
        print("number of attempts left is ", 9-i)
        continue
    elif (inp > 18):
        print("number is greater")
        i = i + 1
        print("number of attempts left is ", 9 - i)
        continue
    else :
        print("congrats you guessed correctly")
        break

print("you have exhasuted your attempt")
