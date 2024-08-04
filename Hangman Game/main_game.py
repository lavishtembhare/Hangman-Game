# main_game.py

import tkinter as tk
from hangman_game import HangmanGame
from database import DatabaseManager

class MainGame:
    def __init__(self):
        self.db_manager = DatabaseManager(
            host="localhost",
            user="root",
            password="",
            database="hangman_game_db"
        )
        self.db_manager.connect()

        self.root = tk.Tk()

        # Ask for player name
        self.player_name = self.get_player_name()

        self.game = HangmanGame(self.root, self.db_manager, self.player_name)

    def get_player_name(self):
        name_window = tk.Toplevel(self.root)
        name_window.title("Enter Player Name")

        tk.Label(name_window, text="Player Name:").pack(pady=10)
        name_entry = tk.Entry(name_window)
        name_entry.pack(pady=10)

        def submit_name():
            player_name = name_entry.get().strip()
            if player_name:
                self.player_name = player_name
                name_window.destroy()

        tk.Button(name_window, text="Submit", command=submit_name).pack(pady=10)
        
        self.root.wait_window(name_window)
        return self.player_name

    def run(self):
        self.root.mainloop()

    def __del__(self):
        self.db_manager.close_connection()
