#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 10/15/2020
#Project: Week 5 Programming Assignment


#import necessary modules
import random, sys, csv
from collections import namedtuple, defaultdict, deque


#define main function
def main():

    num_simulations = int(sys.argv[1])
    validate_input(num_simulations)
    results = defaultdict(dict)

    # define main control loop and loop control variable
    j = 13
    while j < 21:
        stand_on_value = j
        stand_on_soft = False
        dkey = "P-H"+str(j)
        results[dkey] = run_simulations(num_simulations, j, stand_on_soft)

        dkey = "P-S" + str(j)
        stand_on_soft = True
        results[dkey] = run_simulations(num_simulations, j, stand_on_soft)

        j += 1

    # create csv file
    header = deque(["D-H" + str(i) for i in range(13, 21)])
    header.appendleft('P-STRATEGY')
    file = 'output.csv'

    with open(file, 'w')as file:
        writer = csv.writer(file)
        writer.writerow(header)
        # unpack nested dictionaries
        for k, v in results.items():
            row = []
            row.append(k)
            row += list(v.values())
            writer.writerow(row)


class Hand:
    """This class represents a blackjack hand"""
    def __init__(self, cards=None):
        self.total = 0
        self.soft_ace_count = 0
        if cards:
            self.cards = cards
            self.total, self.soft_ace_count = self.score()
        else:
            self.cards = []
            self.add_card()

    def __str__(self):
       return f'Hand:cards={self.cards}, total={self.total}, soft_ace_count={self.soft_ace_count}'

    def add_card(self):
        if len(self.cards) < 2:
            self.cards = [random.randint(1, 13) for i in range(2)]
            self.total, self.soft_ace_count = self.score()
        else:
            self.cards.append(random.randint(1, 13))
            self.total, self.soft_ace_count = self.score()

    def is_blackjack(self):
       if self.total == 21:
           return True

    def is_bust(self):
        if self.total > 21:
            return True

    def score(self):

        Score = namedtuple('Score', ['total', 'soft_ace_count'])
        self.cards.sort(reverse=True)
        # init variables to track total score and number of soft aces
        total = 0
        soft_ace_count = 0

        # loop through hand and calculate total score and #soft aces
        for card in self.cards:
            if card in range(2, 11):
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

class Strategy:
    """This class represents the players decision to hit or stand"""

    def __init__(self, stand_on_value, stand_on_soft):
        self.stand_on_value = stand_on_value
        self.stand_on_soft = stand_on_soft

    def __repr__(self):
        return f'Strategy: (stand_on_value={self.stand_on_value}, stand_on_soft={self.stand_on_soft})'

    def __str__(self):
        if self.stand_on_soft == True:
            return "H"+str(self.stand_on_value)
        if self.stand_on_soft == False:
            return "S"+str(self.stand_on_value)

    def stand(self, hand):
        # calculate score
        total = hand.total
        soft_ace_count = hand.soft_ace_count
        """
        If the total is >= to the provided stand_on_value
        proceed return True/False based on hand and dealer strategy.
        """
        if total >= self.stand_on_value and self.stand_on_soft == True:
            return True

        elif total >= self.stand_on_value and self.stand_on_soft == False:
            if soft_ace_count > 0:
                return False

            else:
                return True

        else:
            return False

    def play(self):
        """"Play a hand of blackjack then return the hand"""
        hand = Hand()
        while self.stand(hand) == False:
            hand.add_card()

        return hand

def run_simulations(num_simulations, stand_on_value, stand_on_soft):
    """
    Run the specified number of simulations and record player victories
    for each scenario
    """
    simulation_result = defaultdict(int)
    [simulation_result[i] for i in range(13, 21)]

    #loop through simulations playing specified number of hands for each strategy
    for i in range(num_simulations):

        for i in range(13, 21):
            players_hand = Strategy(stand_on_value, stand_on_soft).play()
            if not players_hand.is_bust():
                dealers_hand = Strategy(i, stand_on_soft).play()
                if not dealers_hand.is_bust():
                    if players_hand.is_blackjack() and not dealers_hand.is_blackjack():

                        simulation_result[i] += 1

                    elif players_hand.total > dealers_hand.total:

                        simulation_result[i] += 1

    for k, v in simulation_result.items():
        simulation_result[k] = round((v/num_simulations)*100, 4)
    return simulation_result



def validate_input(num_simulations):
    if type(num_simulations) is not int:
        raise TypeError("Only integer values are allowed for argument 1.")

if __name__ == "__main__":
    main()
