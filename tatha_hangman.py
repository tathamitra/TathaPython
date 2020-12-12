'''
HANGMAN
'''

import random
l1 = ["Greater","Amazing","students"]
totalAttempts =10
wrong=[]
right =[]
selectedWord = random.choice(l1).lower()
shownWord = ['_']*len(selectedWord)


def check_word(word):
  global totalAttempts
  if word in selectedWord:
      right.append(word)
      for index in (idx for idx,l in enumerate(selectedWord) if l==word):
       shownWord[index] = word
      return shownWord
  else:
     totalAttempts -= 1
     wrong.append(word)
     print(f"you have {totalAttempts} attempts left")
     return shownWord

if __name__ == '__main__':
 print("Start to play")


while totalAttempts>0:
  print("Enter a word")
  word = input().lower()
  if word in wrong:
      print(f"you have already guessed this wrongly,still {totalAttempts} attepmts left")
  if word in right:
      print(f"you have already guessed this correctly,choose some other character")
  else:
   print(check_word(word))
   print(wrong)

  if "_" not in shownWord:
      print("congratulations")
      break;
print("you lost")
