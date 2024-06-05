"""tratamento da palavra / resposta do usuario"""
def check_for_win(random_word,guessed_letters):
    progress = "_"*len(random_word)
    for index,each_letter in enumerate(random_word):
        if each_letter in guessed_letters:
            temp_progress = list(progress)
            temp_progress[index]=each_letter
            progress = "".join(temp_progress)
    return (random_word.lower() == progress.lower())
