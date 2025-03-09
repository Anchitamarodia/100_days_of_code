rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice=int(input("what do you choose 0 for rock, 1 for paper or 2 for scissor?"))
print('you choose')
if user_choice==0:
    print(rock)
elif user_choice==1:
    print(paper)
else:
     print(scissors)
computer_choice=random.randint(0,2)
print("\n")
print('the computer chooses')
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
else:
     print(scissors)

if user_choice==computer_choice:
    print("its a draw")
elif user_choice==1 and computer_choice==0:
    print('you win')
elif user_choice==0 and computer_choice==1:
    print('you lose')

elif user_choice==1 and computer_choice==2:
    print('you lose')
elif user_choice==2 and computer_choice==1:
    print('you win')

elif user_choice==0 and computer_choice==2:
    print('you win')
elif user_choice==2 and computer_choice==0:
    print('you lose')
else:
    ('sorry wrong output!')











                
                
                            

