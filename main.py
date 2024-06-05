"""Main"""
import ai_word
import interface
import word_processing
# word characteristics 
language = input('Qual o idioma da palavra? ')
characters = input('A palavra deve ter quantos caracteres? ')
difficult = input('Qual a dificuldade do jogo? ')
# Begin by allowing user to select language and handling errors
while True:
    language_setting = input("Select language setting (ENG or PORT) ").upper()
    if language_setting != "ENG" and language_setting != "PORT":
        print(f"{language_setting} is and Invalid setting!!\n")
    else:
        break

random_word = ai_word.generate_word(language_setting)
chosen_letters = []
lives = 6
min_lives = 0

progress = interface.show_progress(random_word,chosen_letters)
word_processing.character_validation(random_word, chosen_letters, progress, lives, min_lives)