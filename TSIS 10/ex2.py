import sqlite3
import os

# Connect to the SQLite database
conn = sqlite3.connect('snake_game.db')
c = conn.cursor()

# Create tables
c.execute('''
    CREATE TABLE IF NOT EXISTS user (
        username TEXT PRIMARY KEY,
        current_level INTEGER
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS user_score (
        username TEXT,
        score INTEGER,
        FOREIGN KEY(username) REFERENCES user(username)
    )
''')

conn.commit()

# Function to start game
def start_game():
    username = input("Enter your username: ")

    # Check if user exists
    c.execute("SELECT * FROM user WHERE username=?", (username,))
    user = c.fetchone()

    if user:
        print(f"Welcome back {username}! Your current level is {user[1]}")
    else:
        print(f"Welcome {username}!")
        c.execute("INSERT INTO user VALUES (?, ?)", (username, 1))
        conn.commit()

    # Start the game here
    # ...

# Function to pause game
def pause_game(username, score):
    print("Game paused.")
    c.execute("INSERT INTO user_score VALUES (?, ?)", (username, score))
    conn.commit()

# Function to resume game
def resume_game(username):
    c.execute("SELECT * FROM user_score WHERE username=?", (username,))
    score = c.fetchone()[1]

    # Resume the game here with the score
    # ...

# Start the game
start_game()
