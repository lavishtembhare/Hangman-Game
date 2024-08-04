# Hangman Game

This is a simple Hangman game implemented using Python and Tkinter with a MySQL backend to store player records (wins and losses). The game provides a graphical user interface (GUI) for players to guess letters and uncover a random word.

Features

- Graphical User Interface: A simple and intuitive interface built with Tkinter.
- Player Records: Stores each player's wins and losses in a MySQL database.
- Random Word Selection: Randomly selects a word from a predefined list for each game.
- Multiple Attempts: Allows players a limited number of incorrect guesses.

Prerequisites

Before running the game, ensure you have the following software installed:

- Python: Version 3.x
- MySQL: A running MySQL server and the `mysql-connector-python` library.

Setup

1. Clone the Repository

Clone the repository to your local machine:
git clone <repository_url>
cd hangman_game


Install Dependencies
Install the required Python libraries using pip:
pip install mysql-connector-python

Configure MySQL
Create a Database and Table

Open your MySQL client (e.g., MySQL Workbench or command line) and create a new database and table:
CREATE DATABASE hangman_game_db;

USE hangman_game_db;

CREATE TABLE player_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100),
    wins INT DEFAULT 0,
    losses INT DEFAULT 0
);
Update Database Credentials

Open main_game.py and update the DatabaseManager initialization with your MySQL credentials:
self.db_manager = DatabaseManager(
    host="localhost",
    user="your_username",
    password="your_password",
    database="hangman_game_db"
)
4. Run the Game
Run the game by executing the following command in the terminal from the hangman_game directory:
python main.py


Game Instructions
Enter Player Name: When prompted, enter your player name. This name will be used to track your record.

Guess the Word: Enter one letter at a time in the provided input field to guess the hidden word.

View Results: The game will display your wins and losses at the end of each round. Start a new game by clicking the "New Game" button.

Game Over: If you run out of guesses, the game ends and updates your record as a loss.

Code Structure
The code is organized into the following files:

bash
hangman_game/
    ├── database.py        # Database management code
    ├── game.py            # Core game logic (Hangman class)
    ├── hangman.py         # Hangman word handling
    ├── hangman_game.py    # GUI implementation
    ├── main_game.py       # Main game loop and initialization
    └── main.py            # Entry point of the application
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.


Summary

This `README.md` provides a comprehensive guide to setting up, running, and understanding the Hangman game project. It covers installation, configuration, and usage instructions to help users easily get started with the game. If you have specific details about the repository URL or additional instructions, feel free to update the placeholder sections accordingly.
