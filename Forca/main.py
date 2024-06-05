"""Main"""
import ai_word
import interface

random_word = ai_word.generate_word()
guessed_letters = []

interface.show_progress(random_word,guessed_letters)