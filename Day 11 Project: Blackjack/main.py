############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import random
from art import logo
print(logo)
con_tinue='y'
while con_tinue=='y':
  con_tinue=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  user_cards=[]
  comp_cards=[]
  
  def deal_cards():
    return random.choice(cards)
  
  def calculate_score(cardss):
    sum=0
    for i in cardss:
      sum=sum+i
    return sum
  
  def compare_score(comp_score,user_score):
    if comp_score==user_score:
      print(f"YOUR SCORE IS: {user_score} COMPUTER'S SCORE IS: {comp_score} \nIts a draw")
    elif user_score==21:
      print(f"YOUR SCORE IS: {user_score} COMPUTER'S SCORE IS: {comp_score}\nYOU WON")
    elif user_score==21:
      print(f"YOUR SCORE IS: {user_score} COMPUTER'S SCORE IS: {comp_score}\nYOU WON")
    if comp_score>21:
      if cards[-4] in comp_cards:
        comp_cards.remove(cards[-4])
        comp_cards.append(1)
        if comp_score>21:
          print(f"YOUR SCORE IS: {user_score} COMPUTER'S SCORE IS: {comp_score}\n COMPUTER WENT OVER.\nYOU WON.")
      else:
        print(f"YOUR SCORE IS: {user_score} COMPUTER'S SCORE IS: {comp_score}\n.COMPUTER WENT OVER.\nYOU WON.")
    elif user_score>21:
      if cards[0] in user_cards:
        user_cards.remove(cards[0])
        user_cards.append(1)
        if user_score>21:
          print(f"YOUR SCORE IS: {user_score} COMPUTER'S SCORE IS: {comp_score}\nYOU WENT OVER.\nYOU LOSE.")
      else:
        print(f"YOUR SCORE IS: {user_score} COMPUTER'S SCORE IS: {comp_score}\nYOU WENT OVER.\nYOU LOSE.")
    elif comp_score>user_score:
      print(f"YOUR SCORE IS: {user_score} COMPUTER'S SCORE IS: {comp_score}.\nYOU LOSE.")
    elif comp_score<user_score:
      print(f"YOUR SCORE IS: {user_score} COMPUTER'S SCORE IS: {comp_score}.\nYOU WIN.")
    
  
  user_cards.append(deal_cards())
  user_cards.append(deal_cards())
  
  comp_cards.append(deal_cards())
  print(f"COMPUTER'S FIRST CARD IS {comp_cards}")
  comp_cards.append(deal_cards())
  
  user_score=calculate_score(user_cards)
  comp_score=calculate_score(comp_cards)
  
  print(f'   YOUR CARDS: {user_cards}, YOUR SCORE: {user_score}')
  answer=input('Do you want to draw another card?\nType y or  n :').lower()
  while answer=='y':
    user_cards.append(deal_cards())
    user_score=calculate_score(user_cards)
    print(f'  YOUR CARDS: {user_cards}, YOUR SCORE : {user_score}')
    user_score=calculate_score(user_cards)
    if user_score>21:
      print(f"  YOUR CARDS: {user_cards} AND YOUR SCORE: {user_score}\n  COMPUTER'S SCORE: {comp_score} YOU WENT OVER.\n YOU LOSE.")
      break
    answer=input('Do you want to draw another card?\nType y or n ').lower()
  
  if answer=='n':
    while comp_score<17:
      comp_cards.append(deal_cards())
      comp_score=calculate_score(comp_cards)
    compare_score(comp_score,user_score)
   
         
 
    
 
  

 
   
