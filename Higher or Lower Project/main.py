import art
from game_data import data
import random


def format(choice):
    name = choice['name']
    role = choice['description']
    country = choice['country']
    return f"{name}, {role}, {country}"

def check_answer(choice1, choice2, ans):
    correct_answer = ""
    if int(choice1['follower_count'])>int(choice2['follower_count']):
        correct_answer = "A"
    else:
        correct_answer = "B"
    if ans == correct_answer:
        return True
    return False

choice_B = random.choice(data)
cont = True
score = 0
print(art.logo)
while cont:
    choice_A = choice_B
    choice_B = random.choice(data)
    if choice_A == choice_B:
        choice_B = random.choice(data)
    print(f"Compare A: {format(choice_A)}")
    print(art.vs)
    print(f"Against B: {format(choice_B)}")
    answer = input("Who has more followers. Type 'A' or 'B': ")
    correct = check_answer(choice_A, choice_B, answer)
    if not correct:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        cont = False
    else:
        score += 1
        print(art.logo)
        print(f"You're right! Your score is {score}")
