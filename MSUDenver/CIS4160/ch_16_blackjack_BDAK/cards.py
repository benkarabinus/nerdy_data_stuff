#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 3/5/2020
#Project: Chapter 16 Blackjack
#Purpose: show basic understanding of object oriented design and
#the three tier architecture in Python 3

#import necessary modules
import random
#return cards
def get_card():
    #random selection of value and suit for each card
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    value = random.choice(cards)
    suit = random.choice(suits)
    return value, suit
