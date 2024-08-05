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
import os
import random
from art import logo

def add_score(p1, card_num):
    total = 0
    for i in range(0,card_num):
        total = p1[i] + total
    return total

def check_burst(scorep1):
    if scorep1 > 21:
        burst = True
    else:
        burst = False
    return burst

def check_result(scorep1, scorecom):
    if scorep1 == scorecom:
        result = "Draw!"
    elif scorep1 > scorecom:
        result = "You Win!"
    elif scorecom > scorep1:
        result = "You Lose!"
    return result
        
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#start again condition
while start != 'n':
    os.system('cls')
    print(logo)
    p1_cardcount = 2
    c1_cardcount = 2
    add_card = True
    com_turn = True
    player_card = []
    com_card = []
    for i in range (0,p1_cardcount):
        choices = random.choice(cards)
        player_card.append(choices)
    for i in range (0,c1_cardcount):
        choices = random.choice(cards)
        com_card.append(choices)   

    scorep1 = add_score(player_card,p1_cardcount)
    burst = check_burst(scorep1)
    if burst == True: #check burst before adding card
        print(f"Your final hand: {player_card}, current score: {scorep1}\n")
        print(f"Computer's Final Hand: {com_card[0]}")
        print(f"You went over. You lose\n")
        add_card = False
        start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
       
    while add_card != False:
        print(f"Your cards: {player_card}, current score: {scorep1}")
        print(f"Computer's first card: {com_card[0]}")
        if scorep1 == 21:
            print(f"Your final hand: {player_card}, current score: {scorep1}\n")
            print("Blackjack! You Win!\n")
            start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            add_card = False
            card_input = 'x' #skip condition if add card = 'n' and end the game
        else:
            card_input = input("Type 'y' to get another card, type 'n' to pass: ")
        if card_input == 'y':
            add_card = True
            p1_cardcount += 1
            choices = random.choice(cards)
            player_card.append(choices)
            scorep1 = add_score(player_card,p1_cardcount)
            burst = check_burst(scorep1) #check burst after adding card

            if scorep1 == 20 and player_card[p1_cardcount-1] == 11:
                player_card[p1_cardcount-1] = 1
                print(f"Your final hand: {player_card}, current score: {scorep1}\n")
                print("Blackjack! You Win!\n")
                start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                add_card = False
                card_input = 'x' #skip condition if add card = 'n' and end the game   

            if burst == True:
                print(f"Your final hand: {player_card}, current score: {scorep1}\n")
                print(f"Computer's Final Hand: {com_card[0]}")
                print(f"You went over. You lose\n")
                add_card = False
                start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        elif card_input == 'n':
            add_card = False
########### Computer Turn
            while com_turn != False: #computer turn to fold or add card                    
                scorecom = add_score(com_card, c1_cardcount)
                burst = check_burst(scorecom)

                if scorep1 == 21: #check com blackjack
                    print(f"Your final hand: {com_card}, current score: {scorecom}\n")
                    print("Computer Blackjack! You Lose!\n")
                    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

                elif scorep1 == 20 and com_card[c1_cardcount-1] == 11: #check ace value if 1 or 11
                    com_card[c1_cardcount-1] = 1
                    scorecom = add_score(com_card, c1_cardcount)
                    print(f"Your final hand: {com_card}, current score: {scorecom}\n")
                    print("Blackjack! You Win!\n")
                    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                    com_turn = False

                elif burst == True: #burst check
                    com_turn = False
                    print(f"Your final hand: {player_card}, current score: {scorep1}\n")
                    print(f"Computer's Final Hand: {com_card}, computer score: {scorecom}")
                    print(f"Computer went over. You Win!\n")
                    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

                elif scorecom > 17: #dont add card if more than 17 and check score
                    com_turn = False
                    burst = check_burst(scorecom)
                    if burst == True: #burst check
                        print(f"Your final hand: {player_card}, current score: {scorep1}\n")
                        print(f"Computer's Final Hand: {com_card}, computer score: {scorecom}")
                        print(f"Computer went over. You Win!\n")
                        start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

                    elif burst != True:
                        result = check_result(scorep1,scorecom)                   
                        print(f"Your final hand: {player_card}, current score: {scorep1}\n")
                        print(f"Computer's Final Hand: {com_card}, computer score: {scorecom}")
                        print(f"{result}")
                        start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

                else: #add another card if score less than 17
                    c1_cardcount += 1
                    choices = random.choice(cards)
                    com_card.append(choices)
