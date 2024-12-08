# hangman_game.py

import tkinter as tk
from tkinter import messagebox
from hangman import Hangman
from database import DatabaseManager

class HangmanGame:
    
    def __init__(self, root, db_manager, player_name):
        self.root = root
        self.root.title("Hangman Game")

        self.hangman = Hangman()
        self.db_manager = db_manager
        self.player_name = player_name

        self.create_widgets()
        self.update_display()

        # Add player to database
        self.db_manager.add_player(self.player_name)
        self.update_player_record_label()

    def create_widgets(self):
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 20))
        self.word_label.pack(pady=20)

        self.guess_label = tk.Label(self.root, text="Enter a letter:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.incorrect_label = tk.Label(
            self.root, text=f"Incorrect guesses left: {self.hangman.max_incorrect_guesses}"
        )
        self.incorrect_label.pack()

        self.player_record_label = tk.Label(self.root, text="")
        self.player_record_label.pack(pady=10)

        self.new_game_button = tk.Button(self.root, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=20)

    def update_display(self):
        display_word = self.hangman.get_display_word()
        self.word_label.config(text=display_word)
        incorrect_left = self.hangman.max_incorrect_guesses - self.hangman.incorrect_guesses
        self.incorrect_label.config(text=f"Incorrect guesses left: {incorrect_left}")

    def update_player_record_label(self):
        record = self.db_manager.get_player_record(self.player_name)
        if record:
            wins, losses = record
            self.player_record_label.config(text=f"Player {self.player_name} - Wins: {wins}, Losses: {losses}")

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid input", "Please enter a single alphabetical character.")
            return

        success, message = self.hangman.guess_letter(guess)
        self.update_display()

        if success and self.hangman.is_word_guessed():
            messagebox.showinfo("Hangman", message)
            self.db_manager.update_record(self.player_name, win=True)
            self.update_player_record_label()
            self.new_game()
        elif not success and not self.hangman.has_incorrect_guesses_remaining():
            messagebox.showinfo("Hangman", message)
            self.db_manager.update_record(self.player_name, win=False)
            self.update_player_record_label()
            self.new_game()
        else:
            if success:
                messagebox.showinfo("Hangman", message)
            else:
                messagebox.showwarning("Hangman", message)

        self.guess_entry.delete(0, tk.END)

    def new_game(self):
        self.hangman.new_game()
        self.update_display()
