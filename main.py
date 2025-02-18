from art import pic
import random
# print(pic)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play the jame of Black Jack? Type: 'y' or 'n ").lower()

"""Function to draw a card"""
def draw_cards():
    return random.sample(cards, 2)

"""Function to calculate the sum of the cards"""
def calculation(hand):
    score = sum(hand)

    # Check if the hand contains an Ace and the score is over 21
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

"""Function to see the users hand"""
def user_cards ():
    hand = draw_cards()
    score = calculation(hand)
    print(f"Your cards: {hand}, current score: {score}")


if play == "y":
    user_hand, user_score = user_cards()
    print(f"Your cards: {user_hand}, current score: {user_score}")
    


    
    


