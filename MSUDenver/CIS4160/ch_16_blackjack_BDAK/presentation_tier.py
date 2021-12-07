#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 3/5/2020
#Project: Chapter 16 Blackjack
#Purpose: show basic understanding of object oriented design and
#the three tier architecture in Python 3



def display_title():
    print("Blackjack")
    print()

def play_again():
    choice = input("Pay Again? (y/n): ")
    return choice

def display_goodbye():
    print()
    print("Come back soon!")


def display_dealer_show_card(game):
    print("Dealer's show card!")
    game.dealer.get_cards()
    print()







def player_show_cards(game):
    print("YOUR CARDS")
    game.player.get_cards()
    print()

def display_winner(game):

    print("Dealer's Cards")
    game.dealer.get_cards()
    print()
    print("YOUR POINTS: ", game.player.add_cards())
    print("DEALER'S POINTS: ", game.dealer.add_cards())
    print()
    print(game.determine_winner())
    print()

def player_choice():

    print()
    choice = input("Hit or Stand? (hit/stand): ")
    print()
    return choice
