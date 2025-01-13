   # black jack game
import random

def deal_card():
    #returns card from deck (a random one)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
comp_cards = []

# to fill the lists created above
for _ in range(2):
    new_card = deal_card() # or user_card.append(deal_card())
    comp_cards.append(deal_card()) # or comp = deal_card()

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    return sum(cards)