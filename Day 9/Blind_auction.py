import os
from art import logo
print(logo)
print("Welcome tp the secret auction program")

loop = True
bid_dict= {}

def add_bid(name, bid): #adding name and bid to dictionary
    bid_dict[name] = bid

def comp(bid_dict): #comparing the bid on who put highest
    current_high = 0
    for name in bid_dict:
        if bid_dict[name] > current_high:
            current_high = bid_dict[name]
            name_high = name
    print(f"The winner is {name_high} with a bid of ${current_high}")

while loop != False: #check whether user want to add another bidder or not
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_bid(name, bid) #adding bidder to the dictionary
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n")
    
    if another_bidder == 'no':
        loop = False
        comp(bid_dict) #comparing each bid after completing fill up
    else:
        os.system('cls') #clear screen after each input