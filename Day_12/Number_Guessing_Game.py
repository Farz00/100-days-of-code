import random
from art import logo

def game(life, num):
    endgame = False
    while endgame != True:
        if life != 0:
            print(f"You have {life} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > num:
                print("Too high")
                life -= 1
            elif guess < num:
                print("Too low")
                life -= 1
            elif guess == num:
                endgame = True
                print(f"You got it! The answer was {guess}.")
        else:
            endgame = True
            print("You've run out of guesses, you lose.")
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
num = random.randint(1,100)

if diff == "easy":
    life = 10
elif diff == "hard":
    life = 5

game(life, num)


    


