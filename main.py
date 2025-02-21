import random
# from art import logo

"""Create a deal card function.Returns a random card from the deck"""
def deal_card():
    #the cards list will be contained inside of this function
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # we want to randomly pick a card out of this list
    card = random.choice(cards)
    return card

"""Create a deal card function. It will take a list of cards as an input
and return the score"""
def calculate_score(cards):
    # checking for black jack
    # logic: a hand with only 2 cards , an ace(11&10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # if the user score goes over 21 want to change the ace from 11 to 1
    if 11 in cards and sum(cards) > 21:
        # use the append and remove functions
        cards.remove(11)
        cards.append(1)
    # using the sum function we calculate the score of the cards
    return sum(cards)

"""Create a function to compare the user score and the computer score"""
def compare(u_score, c_score):
    if u_score == c_score:
        return "A draw 🤨"
    elif c_score == 0:
        return "You lose , the computer has black jack 😖"
    elif u_score == 0:
        return "You win!!!!!"
    elif u_score > 21:
        return "You went over. You lose ☹️"
    elif c_score > 21:
        return "You win !!! Computer went over."
    elif u_score > c_score:
        return "You win !!!"
    else:
        return "You lose"

def play_game():
    # print(logo)
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    """Deal the user and computer 2 cards each"""
    # we can use an underscore because we do not need this variable
    # when this loop runs we will get a new card by calling deal_card
    for _ in range(2):
        # using append to add a single item to a list
        user_card.append(deal_card())
        computer_card.append(deal_card())

    """Create a while loop that will be active until the game is over"""
    while not is_game_over:

        """we call the calculate score function"""
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"your cards:{user_card}, current score:{user_score}")
        # picking out the computers first card
        print(f"computers first card {computer_card[0]}")

        """make sure if the computer and the user has a blackjack
        or if the user score is over 21. We have to end the game"""
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

        """Create a while loop to check on computer score"""
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand :{user_card}, Your final score: {user_score}")
    print(f"Computer score:{computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    print("\n"*100)
    play_game()
