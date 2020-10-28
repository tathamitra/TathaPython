import random
from time import sleep

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
def wait():
     for i in range(15):
         print('.',end='')
         sleep(.5)


chosenword = random.chosenword(words)

right = ['_'] * len(chosenword)
wrong = []

def update():
    for i in right:
        print(i,end = ' ')


print("let me think of a word")
wait()
print("\nthe word has ", len(chosenword) , "letters")
update()

while True:
    print("\nchoose a letter")
    letter = input()

    if letter in chosenword:
        index = 0
        for i in chosenword:
            if i == letter:
                right[index] = letter
            index = index +1
        update()
    else:
        if letter not in wrong:
            wrong.append(letter)
        else:
            print("you already guessed that")
        update()
    if len(wrong)>5:
        print("you loose")
        print("the correct answer is :", chosenword)
        break;
    if '_' not in right:
        print("\nyou win")
        break;