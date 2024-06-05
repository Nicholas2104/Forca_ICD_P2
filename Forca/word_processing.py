"""tratamento da palavra / resposta do usuario"""
#take input must verify if guess is not duplicated and is in alphabet - returns character
def check_for_win(random_word,guessed_letters):
    progress = "_"*len(random_word)
    for index,each_letter in enumerate(random_word):
        if each_letter in guessed_letters:
            temp_progress = list(progress)
            temp_progress[index]=each_letter
            progress = "".join(temp_progress)
    return (random_word.lower() == progress.lower())

def take_input(guessed_letters):
    while True:
        guessed_char = input("Give a letter from a-z: ")
        if guessed_char in guessed_letters or len(guessed_char) > 1:
            print("Try again")
        elif guessed_char.isalpha() == True:
            return guessed_char
        else:
            print("Try again -- input not in alphabet")