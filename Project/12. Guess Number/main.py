# from replit import clear
from art import logo
import random

print(logo)
# Number Guessing Game Objectives:

# Include an ASCII art logo.

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 1
if difficulty == "easy":
    # print("You have 10 attempts remaining to guess the number.")
    attempts = 10
elif difficulty == "hard":
    # print("You have 5 attempts remainging to guess the number.")
    attempts = 5
else:
    print("You Type Wrong difficulty. Type 'easy' or 'hard': ")
# Allow the player to submit a guess for a number between 1 and 100.
random_guess = random.randint(1, 100)

print(random_guess)
# print(player_guess)
# print(attempts)

while attempts:
    print(f"You have {attempts} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    if player_guess == random_guess:
        print(f"You got it! The answer was {random_guess}.")
        break
    elif player_guess > random_guess:
        print("Too high.")
        print("Guess again")
    elif player_guess < random_guess:
        print("Too low.")
        print("Guess again!")
    attempts -= 1

if attempts == 0:
    print(f"You've run out of guesses.You lose.")

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
