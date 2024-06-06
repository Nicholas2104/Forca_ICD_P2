"""Main"""
import ai_word
import word_processing
import interface

continue_play = True

while continue_play:

    random_word = ai_word.generate_word().lower()
    guessed_letters = []
    lives = 6 
    win_condition = False 
    while lives > 0 and win_condition == False:
        #take_input must verify if guess is not duplicated and is in alphabet - returns character
        guessed_char = word_processing.take_input(guessed_letters).lower()
        guessed_letters.append(guessed_char)
        #checking if guess is valid
        is_correct_guess = (guessed_char in random_word)
        if not is_correct_guess:
            lives -= 1
            interface.show_game_state(lives,random_word,guessed_letters)
            if lives == 0:
                print("You LOST!!!!! HAHAHAHAH")
        else:
            interface.show_game_state(lives,random_word,guessed_letters)
            win_condition = word_processing.check_for_win(random_word,guessed_letters)
            if win_condition:
                print("YOU WON!!\n")
            else:
                print("CORRECT!!!")
    while True:
        check = input("Would you like to continue playing? (Y/N): ").upper()
        if check != "Y" and check != "N":
            print("invalid input!!")
        elif(check =="Y"):
            continue_play = True
            break
        else:
            continue_play = False
            print("Bye")
            break

