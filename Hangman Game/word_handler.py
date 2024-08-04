# word_handler.py

import random

class WordHandler:

    def __init__(self, words):
        self.words = words
        self.word = ""
        self.guessed_letters = set()

    def new_word(self):
        self.word = random.choice(self.words)
        self.guessed_letters = set()

    def get_display_word(self):
        return ''.join(
            [letter if letter in self.guessed_letters else '_' for letter in self.word]
        )

    def is_word_guessed(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return False, "You've already guessed that letter."

        self.guessed_letters.add(letter)

        if letter in self.word:
            return True, "Good guess!"
        else:
            return False, "Incorrect guess!"
