import  random
print("Enter your name")
name= input()
compcount = 0
usercount = 0
drawcount = 0


i=0

def winner(userchhoice,name):
    lst = ["snake", "water", "gun"]
    chance = random.choice(lst)
    print(chance)
    if userchhoice == "snake" and chance == "water":
     level = name
    if userchhoice == "snake" and chance == "gun":
     level = "computer"
    if userchhoice == "snake" and chance == "snake":
     level = "draw"
    if userchhoice == "gun" and chance == "water":
     level = "computer"
    if userchhoice == "gun" and chance == "gun":
     level = "draw"
    if userchhoice == "gun" and chance == "snake":
     level = name
    if userchhoice == "water" and chance == "water":
     level = "draw"
    if userchhoice == "water" and chance == "gun":
     level = name
    if userchhoice == "water" and chance == "snake":
     level = "computer"

    return  level

    # snake > water
    # water > gun
    # gun > snake

while ( i < 10):

    print("Enter your Entry:")
    userchhoice = input()
    winrresult = winner(userchhoice,name)
    sample = f"the winner is {winrresult}"
    print(sample)
    if winrresult == "computer":
     compcount = compcount + 1
    if winrresult == name:
     usercount = usercount + 1
    else:
        drawcount = drawcount +1
    i = i + 1
    if i == 10 :
     if compcount > usercount:
        print("computer wins the Tournament")
        print("comuter :", compcount)
        print("user :", usercount)
     elif compcount < usercount:
        print("user wins the tournament")
        print("computer :", compcount)
        print("user :", usercount)
     else:
        print("Tournament is a draw")
        print("comuter :", compcount)
        print("user :", usercount)


