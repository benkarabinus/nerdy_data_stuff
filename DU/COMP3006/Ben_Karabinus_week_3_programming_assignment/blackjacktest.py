#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 9/26/2020
#Project: Week 3 Programming Assignment
#Purpose: show basic understanding of using python 3 for software testing

import random,sys


def main():


    #set input variables == to system arguments
    num_simulations = 100
    stand_on_value = 17
    stand_on_soft = "hard"

    #call function to validate input
    validate_input(num_simulations,stand_on_value,stand_on_soft)

    #init bust counter
    bust_count = 0

    #create loop control structure, run specified number of simulations
    for i in range(num_simulations+1):

        #init hand (2 cards)
        cards = [get_card() for i in range(2)]


        #cretate loop control structure, run until stand == True
        while stand(stand_on_value, stand_on_soft, cards) == False:

            #if stand is false append new card to hand
            cards.append(get_card())

            #test for bust
            if (score(cards)[0]) > 21:

                bust_count += 1


    #print bust percentage to the console
    print(f"The percentage of simulations for which the hand was bust was {bust_count/num_simulations :.2%}.")









"""
Define function to get cards.
Values (1) == Ace. Aces are wild add 1 or 11 to score as game necessitates
Values (2-10) == face value (e.g. 2 == 2)
Values (11-13) == Jack, Queen and  King and add 10 to the players score.

"""

def get_card():

    return random.randint(1, 13)


def score(cards):

    cards.sort(reverse=True)



    #init variables to track total score and number of soft aces
    total = 0
    soft_ace_count = 0

    #loop through hand and calculate total score and # soft aces
    for card in cards:

        if card in range(2,11):
            total += card

        elif card == 1:
            if (total + 11) <= 21:
                card = 11
                total += card
                soft_ace_count += 1

            else:
                card = 1
                total += card


        else:
            total += 10

    return (total, soft_ace_count)

#function to determine hit or stand (loop control variable)
def stand(stand_on_value, stand_on_soft, cards):


    #calculate score
    total, soft_ace_count = score(cards)

    """
    Determine dealer strategy.
    If "soft" the game is S17 dealer stands on all 17's.
    If "hard" the game is H17 dealer hits on soft 17's.
    """
    if stand_on_soft.lower() == "soft":
        soft = True
    if stand_on_soft.lower() == "hard":
        soft = False

    """
    If the total is >= to the provided stand_on_value
    proceed return True/False based on hand and dealer strategy.
    """
    if total >= stand_on_value and soft == True:

        return True

    elif total >= stand_on_value and soft == False:

        if soft_ace_count > 0:

            return False

        else:
            return True

    else:
        return False


#function to validate user input
def validate_input(num_simulations, stand_on_value, stand_on_soft):

    valid_strategy = False

    if type(num_simulations) is not int or type(stand_on_value) is not int:

        raise TypeError("Only integer values are allowed for agruements 1 and 2.")

    if stand_on_value < 1 or stand_on_value > 20:
        raise ValueError("You must enter a stand-on-value between (1-20).")

    if type(stand_on_soft) is not str:
        raise TypeError("Only string values are allowed for argument 3.")

    if stand_on_soft.lower() == "hard" or stand_on_soft.lower() == "soft":

        valid_strategy = True

    elif valid_strategy == False:

        raise ValueError("You must enter 'soft' or 'hard' for argument 3.")






if __name__ == "__main__":
    main()
