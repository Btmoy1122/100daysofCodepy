import art
import random
print(art.logo)
print("Welcome to Number Guessing Game!")
num = random.randint(1,101)
print("I'm thinking of a number between 1 and 100")
difficulty =  input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    guess = int(input("Guess a number: "))
    if guess == num:
        print(f"You got it! The answer was {num}")
        break
    elif guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")
    attempts -=1
    print(f"You have {attempts} attempts remaining.")
