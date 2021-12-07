#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 2/18/2020
#Project: Chapter 17 Player Manager
#Purpose: show basic understanding of working with SQL Lite database
# in Python 3

class Player:
    #instantiate player
    def __init__(self, name=None, wins=0, losses=0, ties=0, games=0):
        self.__name = name
        self.__wins = wins
        self.__losses = losses
        self.__ties = ties
        self.__games = games

    #getter and setter functions for player object
    @property
    def name(self):
        return self.__name

    @name.setter
    def height(self, name):
        self.__name = name

    @property
    def wins(self):
        return self.__wins
    @wins.setter
    def wins(self,wins):
        self.__wins = wins
    @property
    def losses(self):
        return self.__losses
    @losses.setter
    def losses(self, losses):
        self.losses = losses
    @property
    def ties(self):
        return self.__ties
    @ties.setter
    def ties(self, ties):
        self.__ties = ties
    @property
    def games(self):
        return self.__games
