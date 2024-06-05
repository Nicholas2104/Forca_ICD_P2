"""tratamento da palavra / resposta do usuario"""
def character_validation(random_word, chosen_letters, progress, lives, min_lives):
    while lives > min_lives:
        print(f"GUESSED CHARACTERS {chosen_letters}")
        print(f"Current Progress: {progress}\nLives left: {lives}")
        guessed_char = str(input("Give a random letter from a-z: ")).lower()
        if guessed_char in chosen_letters:
            print("!--That character has already been chosen--!")
        elif guessed_char in random_word:
            chosen_letters.append(guessed_char)
            if (progress == random_word):
                print(f"YOU WON - the word was {random_word}")
                break
        else:
            chosen_letters.append(guessed_char)
            lives -=1
            if(lives == 0):
                print(f"You Lost the word was: {random_word}")
                break
            print("Wrong!\n")
