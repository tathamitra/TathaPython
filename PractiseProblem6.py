'''
A nd B are inputs taken from user.You and your friend have to guess a number between A nd B.
player 1 and plays first.player 2 and plays second.
person with least attempts to guess wins
'''
import random

def playgame():
 noOfguess = 0
 while True:
    print("Enter the guess")
    guess = int(input())
    if guess < A:
        raise ValueError(f'{guess} is less than {A} the lower limit')
    if guess > B:
        raise ValueError(f'{guess} is greater than {B} the upper limit')
    elif guess > Result:
        print("You guessed a greater number")
        noOfguess+=1
    elif guess < Result:
        print("You guessed a smaller number")
        noOfguess+=1
    else:
        noOfguess += 1
        print(f"you solved in in {noOfguess} trials")
        break
 return noOfguess

if __name__ == "__main__":
    try:
        print("Enter A ")
        A = int(input())
        print("Enter B ")
        B = int(input())
    except ValueError:
        print("Enter integer only")
        exit()

Result = random.randint(A, B)
print(Result)


print("Player 1 ,Let's start")
Player1Result1 = playgame()
print("Player 2 ,Let's start")
Player1Result2 = playgame()
if Player1Result2 > Player1Result1:
    print("Player 2 Won")
elif Player1Result1 > Player1Result2:
    print("Player 2 Won ")
else :
    print("It's a Tie")