import random

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
choices = [rock,paper,scissors]

user = int(input("What do you choose? Type 0 for Rock; 1 for Paper: 2 for Scissors.\n"))

com = random.choice(choices)

com_index = int(choices.index(com))
if user >= 3 or user < 0:                   #Check for invalid number
    print("Invalid Number, You lose!\n")
else:
    print("Your Choice:\n"+choices[user])   #Print Image if input is valid
    print("Computer Choose:\n"+com)
    
#Game decission by rule
    if  user == com_index:
        print("DRAW!\n")
    elif user == 0 and com_index == 2:
        print("You Win!!\n")
    elif user == 2 and com_index == 0:
        print("You lose!!\n")
    elif user>com_index:
        print("You Win!!\n")
    elif com_index>user:
        print("You lose!!\n")

