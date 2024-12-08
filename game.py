# game.py

class Game:

    def __init__(self, max_incorrect_guesses):
        self.max_incorrect_guesses = max_incorrect_guesses
        self.incorrect_guesses = 0

    def new_game(self):
        self.incorrect_guesses = 0

    def has_incorrect_guesses_remaining(self):
        return self.incorrect_guesses < self.max_incorrect_guesses
