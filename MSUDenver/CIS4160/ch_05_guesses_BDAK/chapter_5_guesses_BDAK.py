#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 2/5/2020
#Project: Chapter 5 Exercise Guesses
#Purpose: show basic understanding of how to debug programs in Python 3

import random

def display_title():
    print("Guess the number!")
    print()

def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    #you must initialize the variable count prior to playing the game
    #count must be initialized to 1 not 0 
    count = 1
    print("I'm thinking of a number from 1 to " + str(limit) + "\n")
    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        # the boolean operator For the elif below must be ">" not ">="    
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            print("You guessed it in " + str(count) + " tries.\n")
            return

def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        limit = get_limit()
        #the function play play_game() must be passed the variable limit
        play_game(limit)
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

