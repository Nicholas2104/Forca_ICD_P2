"""Interface e Progresso do Jogo"""
def show_guess(random_word, guessed_letters):
    progress = "_"*len(random_word)
    for index,each_letter in enumerate(random_word):
        if each_letter in guessed_letters:
            temp_progress = list(progress)
            temp_progress[index]=each_letter
            progress = "".join(temp_progress)
    print(f"Progress: {progress}\nGuessed Letters: {guessed_letters}")
def show_game_state(lives,random_word,guessed_letters):
    HANGMAN_ASCII = ['''
      +---+
          |
          |
          |
         ===''', '''
      +---+
      O   |
          |
          |
         ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\  |
     / \  |
         ===''']
    print(HANGMAN_ASCII[6-lives]+"\n")
    show_guess(random_word, guessed_letters)
    print(f"You have {lives} lives left!!!")
