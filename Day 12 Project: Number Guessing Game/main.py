#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
 
from art import logo
import random

def guess_number():
  number=random.randint(1,100)
  return number
number=0
guess=0
level=''
def difficulty():
  global guess
  global level 
  level=input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level=="easy":
    print('You have 10 attempts remaining to guess the number.')
    guess=int(input('Make a guess:'))
    return 10
  else:
    print('You have 5 attempts remaining to guess the number.')
    guess=int(input('Make a guess:'))
    return 5

def check_answer(): 
  global guess
  global number
  if guess>number:
    return 'too high'
  elif guess<number:
    return 'too low'
  else:
    return ''


def game():
  global number
  global guess
  global level
  global guess
  print(logo)
  print('Welcome to the Number Guessing Game! \nI\'m thinking of a number between 1 and 100.')
  num=difficulty()
  number=guess_number()
  for i in range(num-1): 
    print(check_answer())
    if guess!=number:
      print('guess again')
      print(f'you have {num-i-1} attempts remaining to guess the number')
      guess=int(input('Make a guess:'))
  if guess!=number:
    print("The number was {guess}\nYou've run out of guesses, you lose.")
  else:
    print('YOU WIN!!\n')


game()

    
    
    
  
    
