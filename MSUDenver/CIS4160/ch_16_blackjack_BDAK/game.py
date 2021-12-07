#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 3/5/2020
#Project: Chapter 16 Blackjack
#Purpose: show basic understanding of object oriented design and
#the three tier architecture in Python 3

#import necessary modules
import cards

class Game:
    def __init__(self):
        #instanitate player and dealer
        self.__player = Player()
        self.__dealer = Dealer()
        #deal intitial cards
        self.__dealer.hit()
        self.__player.hit()
        self.__player.hit()
    #getter and setter methods for player and dealer
    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player):
        self.__player = player
    @property
    def dealer(self):
        return self.__dealer
    @dealer.setter
    def dealer(self, dealer):
        self.__dealer = dealer

    #dealers move
    def dealer_move(self):
        #dealer hits til hand is greater than 17
        while self.__dealer.add_cards() < 17:
            self.__dealer.hit()
    #player hits
    def player_move(self):
        self.__player.hit()

    #determine the winner of the game
    def determine_winner(self):
        if self.player.add_cards() > 21:
            return "No! You busted. The dealer wins."
        elif self.__dealer.add_cards() > 21:
            return "Yay! The dealer busted. You win!"
        elif abs(self.__player.add_cards() - 21) < \
                abs(self.__dealer.add_cards() - 21):
            return "Yay! You win!"
        elif abs(self.__player.add_cards() - 21) == \
                abs(self.__dealer.add_cards() - 21):
            return "Push! The game is a draw."
        else:
            return " No! Dealer Wins!"


class Player:
    #instantiate player
    def __init__(self):
        self.__hand = hand = []
        self.__sum_cards = 0
        self.__values = []

    def hit(self):
        #get card from card data store
        value, suit = cards.get_card()
        #store the value of the card
        self.__values.append(value)
        card = str(value) + " of " + suit
        #store the text representation of the card
        self.__hand.append(card)

    #print player's hand to the console
    def get_cards(self):
        for card in self.__hand:
            print(card)

    #determine sum of values in the player's hand
    def add_cards(self):
        sum_cards = 0
        for value in self.__values:
            #if face card and not Ace value == 10
            if value not in range(1, 11) and value != "Ace":
                value = 10
            #if Ace initial value is 11
            elif value == "Ace":
                value = 11
            sum_cards += value

            # if bust and ace in hand switch ace value to 1
            if sum_cards > 21:
                sum_cards = 0
                for value in self.__values:
                    if value not in range(1, 11) and value != "Ace":
                        value = 10
                    elif value == "Ace":
                        card = 1
                    elif value not in range(1, 11):
                        value = 10
                    sum_cards += value
        #return hand value
        return sum_cards





class Dealer:
    # instantiate dealer
    def __init__(self):
        self.__hand = []
        self.__sum_cards = 0
        self.__values = []
    #for documentation of this function see player
    def hit(self):
        value, suit = cards.get_card()
        self.__values.append(value)
        card = str(value) + " of " + suit
        self.__hand.append(card)

   #for documentation of this function see player
    def get_cards(self):
        for card in self.__hand:
            print(card)
    #for documentation of this function see player
    def add_cards(self):
        sum_cards = 0
        for value in self.__values:
            if value not in range(1, 11) and value != "Ace":
                value = 10
            elif value == "Ace":
                value = 11
            sum_cards += value
            if sum_cards > 21:
                sum_cards = 0
                for value in self.__values:
                    if value == "Ace":
                        value = 1
                    elif value not in range(1, 11):
                        value = 10
                    sum_cards += value
        return sum_cards
