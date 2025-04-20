# games.py
import random

# Stores active games {user_id: secret_number}
active_games = {}

def start_new_game(user_id):
    secret_number = random.randint(1, 100)
    active_games[user_id] = secret_number
    print(f"The number guessing game starts (answer {secret_number} for {user_id})")
    return secret_number

def check_guess(user_id, guess):
    if user_id not in active_games:
        return "no_game"

    print(f"user {user_id} guessed {guess}")
    target = active_games[user_id]
    if guess < target:
        return "low"
    elif guess > target:
        return "high"
    else:
        del active_games[user_id]
        return "correct"
