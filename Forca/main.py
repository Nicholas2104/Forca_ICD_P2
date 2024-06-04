"""Main"""
import ai_word
import interface
# Begin by allowing user to select language and handling errors
while True:
    language_setting = input("Select language setting (ENG or PORT) ").upper()
    if language_setting != "ENG" and language_setting != "PORT":
        print(f"{language_setting} is and Invalid setting!!\n")
    else:
        break

random_word = ai_word.generate_word(language_setting)
guessed_letters = []

interface.show_progress(random_word,guessed_letters)