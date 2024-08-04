# database.py

import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    """Handles database operations for storing player records."""

    def __init__(self, host, user, password, database):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "hangman_game_db"
        self.connection = None

    def connect(self):
        """Connects to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            self.connection = None

    def close_connection(self):
        """Closes the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")

    def add_player(self, player_name):
        """Adds a new player to the database."""
        if self.connection is None:
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM player_records WHERE player_name = %s", (player_name,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute("INSERT INTO player_records (player_name, wins, losses) VALUES (%s, %s, %s)",
                               (player_name, 0, 0))
                self.connection.commit()
        except Error as e:
            print(f"Error adding player to database: {e}")
        finally:
            cursor.close()

    def update_record(self, player_name, win):
        """Updates the player's record with a win or loss."""
        if self.connection is None:
            return

        cursor = self.connection.cursor()
        try:
            if win:
                cursor.execute("UPDATE player_records SET wins = wins + 1 WHERE player_name = %s", (player_name,))
            else:
                cursor.execute("UPDATE player_records SET losses = losses + 1 WHERE player_name = %s", (player_name,))
            self.connection.commit()
        except Error as e:
            print(f"Error updating player record in database: {e}")
        finally:
            cursor.close()

    def get_player_record(self, player_name):
        """Retrieves the player's win/loss record."""
        if self.connection is None:
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT wins, losses FROM player_records WHERE player_name = %s", (player_name,))
            record = cursor.fetchone()
            return record
        except Error as e:
            print(f"Error retrieving player record from database: {e}")
            return None
        finally:
            cursor.close()
