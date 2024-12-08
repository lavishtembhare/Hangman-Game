# hangman.py

from game import Game
from word_handler import WordHandler

class Hangman(Game, WordHandler):
    def __init__(self):
        words = [
            "message",
            "communication",
            "aspect",
            "income",
            "leader",
            "nation",
            "concept",
            "article",
            "maintenance",
            "operation",
            "queen",
            "tooth",
            "priority",
            "cigarette",
            "recipe",
            "birthday",
            "mud",
            "reality",
            "profession",
            "throat"
        ]
        Game.__init__(self, max_incorrect_guesses=6)
        WordHandler.__init__(self, words=words)
        self.new_game()

    def new_game(self):
        Game.new_game(self)
        self.new_word()

    def guess_letter(self, letter):
        correct_guess, message = WordHandler.guess_letter(self, letter)

        if not correct_guess:
            self.incorrect_guesses += 1
            if not self.has_incorrect_guesses_remaining():
                return False, f"Sorry, you've run out of guesses. The word was: {self.word}"
        
        if self.is_word_guessed():
            return True, f"Congratulations! You've guessed the word: {self.word}"
        
        return correct_guess, message
