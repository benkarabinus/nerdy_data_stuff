#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 3/5/2020
#Project: Chapter 16 Blackjack
#Purpose: show basic understanding of object oriented design and
#the three tier architecture in Python 3

#import necessary modules
from game import Game
import presentation_tier as display

#main function
def main():

    #display title from UI tier
    display.display_title()
    #set main loop control variable
    control = "y"
    #main control loop
    while control.lower() == "y":
        #instantiate a new game
        game = Game()
        #dealer shows first card
        display.display_dealer_show_card(game)
        #player views their cards
        display.player_show_cards(game)
        #dealer hits until hand is 17 or greater
        game.dealer_move()
        #input validation control
        while True:
            #display player choice from UI tier
            choice = display.player_choice().lower()
            #input validation
            if choice.lower() == "hit" or choice.lower() == "stand":
                break
            else:
                print("Please enter (hit/stand)")
        #player hits
        while choice == "hit":
            game.player_move()
            display.player_show_cards(game)
            #input validation control
            while True:
                choice = display.player_choice().lower()
                if choice.lower() == "hit" or choice.lower() == "stand":
                    break
                else:
                    print("Please enter (hit/stand)")
        #if stand display winner
        display.display_winner(game)
        #ask the user if they'd like to play again
        control = display.play_again()
    #display goodbye  message
    display.display_goodbye()

#if main module run main function
if __name__ == "__main__":
    main()