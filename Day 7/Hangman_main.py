import random
import hangman_arts
from hangman_words import word_list,game_result

end_game = False
chosen_word = random.choice(word_list)
word_num = len(chosen_word)
lives = 6

display = []
for i in range(word_num):
    display+= "_"

#def game_result():      #to print letter guess in the words and the hangman
#    print(f"{"".join(display)}")
#    print(hangman_arts.stages[lives])
#
#    if end_game == True and lives != 0:     #condition if game ended yet or not
#        print("You Won!")
#    elif end_game == True and lives == 0:
#        print("You Lose!")

print(hangman_arts.logo) #print logo at start
#====================================================================================================================================
while end_game != True:    #check game ended yet or not
    game_result(end_game,lives,display)
    guess = input("Guess a letter: ").lower()

    for pos in range(word_num):     #Check guessed letter
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
   
    if guess not in chosen_word:    #check if letter guessed is corret or not
        lives -= 1
        if lives == 0:              #no live anymore
            end_game = True
            game_result(end_game,lives,display)

    if "_" not in display:          #no "_" and other words guess is correct
        end_game = True
        game_result(end_game,lives,display)       