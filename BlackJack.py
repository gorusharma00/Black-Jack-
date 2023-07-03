import random
import os
from logo import logo

def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "It's a draw 🙂😑"
    elif computer_score == 0:
        return "You loose 😖"
    elif user_score == 0:
        return "You win 😍😎"
    elif user_score > 21:
        return "You get over 21,You loose😖"
    elif computer_score > 21:
        return "You win 😍😎"
    elif user_score > computer_score:
        return "You win 😍😎"
    else:
        return "You loose😖"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards} and your score: {user_score}")
        print(f"computer's First card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"computer final hand: {computer_cards}, computer final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play Black Jack Game? Type 'y' for yes and 'n' for no: ") == "y":
    os.system('cls')
    play_game()
    




