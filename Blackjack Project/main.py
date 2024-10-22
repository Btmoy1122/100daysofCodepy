import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def print_hand(user_cards, computer_cards,score,comp_score):
    print(f"Your final hand: {user_cards}, final score is {score}")
    print(f"Computer's final hand: {computer_cards}, final score is {comp_score}")


def main():
    print(art.logo)
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]
    score = user_cards[0]+user_cards[1]
    print(f"You cards: {user_cards}, current score is {score}")
    print(f"Computer's first card: {computer_cards}")
    cont = True
    over = False

    while cont:
        another = input(print("Type 'y' to get another card, type 'n' to pass: "))
        if another == "n":
            cont = False
            break
        else:
            user_cards.append(random.choice(cards))
            score = sum(user_cards)
            print(f"Your cards: {user_cards}, current score is {score}")
            print(f"Computer's first card: {computer_cards}")
            if score >21:
                over = True
                break
    score = sum(user_cards)
    comp_score = sum(computer_cards)
    if not over:
        comp_over = False
        while comp_score<17:
            computer_cards.append(random.choice(cards))
            comp_score = sum(computer_cards)
            if comp_score >21:
                comp_over = True
        if comp_over:
            print_hand(user_cards, computer_cards, score, comp_score)
            print("Opponent went over. You win")
        else:
            print_hand(user_cards, computer_cards, score, comp_score)
            if comp_score%21<score%21:
                print("You lose")
            elif score%21<comp_score%21:
                print("You win")

    else:
        print_hand(user_cards, computer_cards, score, comp_score)
        print("You went over. You lose")
    play_again= input(print("Would you like to play again? (y/n)"))
    if play_again=="y":
        main()

main()