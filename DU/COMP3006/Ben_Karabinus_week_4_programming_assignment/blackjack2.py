#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 10/9/2020
#Project: Week 4 Programming Assignment


#import necessary modules
import random, sys, csv
from collections import namedtuple, defaultdict, deque





#define main function
def main():

    num_simulations = int(sys.argv[1])

    validate_input(num_simulations)

    results = defaultdict(dict)

    # define main control loop and loop control variable
    j =13

    while j < 21:

        stand_on_value = j
        stand_on_soft = True
        dkey = "S"+str(j)
        results[dkey] = run_simulations(num_simulations, j, stand_on_soft)

        dkey = "H" + str(j)
        stand_on_soft = False
        results[dkey] = run_simulations(num_simulations, j, stand_on_soft)

        j +=1

    #create csv file
    header = deque([i for i in range(13, 22)])
    header.appendleft('STRATEGY')
    header.append('BUST')
    file ='output.csv'

    with open(file, 'w')as file:
        writer = csv.writer(file)
        writer.writerow(header)

        #unpack nested dictionaries
        for k, v in results.items():
            row = []
            row.append(k)
            row += list(v.values())
            writer.writerow(row)


def run_simulations(num_simulations, stand_on_value, stand_on_soft):

    simulation_result = defaultdict(int)

    #loop through simulations playing specified number of hands for each strategy
    for k in range(13, 23):
        simulation_result[k] = 0

    for i in range(num_simulations+1):

        result = play_hand(stand_on_value, stand_on_soft)

        if result in simulation_result.keys():

            simulation_result[result] += 1

    for key in simulation_result.keys():

        simulation_result[key] = round((simulation_result[key]/num_simulations) * 100, 4)

    return simulation_result



def play_hand(stand_on_value, stand_on_soft):

    #init hand (2 cards)
    cards = [get_card() for i in range(2)]

    #hit or stand
    Stand = stand(stand_on_value, stand_on_soft, cards)


    #cretate loop control structure, run until stand == True
    while Stand.stand == False:

        #if stand is false append new card to hand
        cards.append(get_card())
        Stand = stand(stand_on_value, stand_on_soft, cards)

    if Stand.total > 21:
        return 22

    else:
        return Stand.total

"""
Define function to get cards.
Values (1) == Ace. Aces are wild add 1 or 11 to score as game necessitates
Values (2-10) == face value (e.g. 2 == 2)
Values (11-13) == Jack, Queen and  King and add 10 to the players score.
"""

def get_card():

    return random.randint(1, 13)



def score(cards):

    Score = namedtuple('Score', ['total', 'soft_ace_count'])

    cards.sort(reverse=True)

    #init variables to track total score and number of soft aces
    total = 0
    soft_ace_count = 0

    #loop through hand and calculate total score and #soft aces
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

    return Score(total, soft_ace_count)

#function to determine hit or stand (loop control variable)
def stand(stand_on_value, stand_on_soft, cards):

    Stand = namedtuple('Stand', ['stand', 'total'])

    #calculate score
    total, soft_ace_count = score(cards)



    """
    If the total is >= to the provided stand_on_value
    proceed return True/False based on hand and dealer strategy.
    """
    if total >= stand_on_value and stand_on_soft == True:

        return Stand(True, total)

    elif total >= stand_on_value and stand_on_soft == False:

        if soft_ace_count > 0:

            return Stand(False, total)

        else:

            return Stand(True, total)

    else:

        return Stand(False, total)


def validate_input(num_simulations):

    if type(num_simulations) is not int:
        raise TypeError("Only integer values are allowed for argument 1.")

if __name__ == "__main__":
    main()
