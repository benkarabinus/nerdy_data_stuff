#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 3/5/2020
#Project: Chapter 17 Player Manager
#Purpose: show basic understanding of working with SQL Lite database
# in Python 3
import db_tier as db
from player import Player

def display_title():
    print("Player Manager")
    print()


def display_command_menu():

    print("Command Menu")
    print("view - View all players")
    print("add - Add a player")
    print("del - Delete a player")
    print("exit Exit Program")
    print()

def get_command():
    command = input("Command: ")
    print()
    return command

def display_players():
   #format player attributes before printing to console
    line_format = "{:15} {:>10} {:>10} {:>10} {:>10}"
    print(line_format.format("Name", "Wins", "Losses", "Ties", "Games"))
    print("-" * 60)
   #get players from DB
    players = db.get_players()
    for player in players:
        print(line_format.format(player.name, player.wins, player.losses, player.ties,
                                 player.games))
    print()

def add_player():

    name = input("Name: ")
    while True:
        try:
            wins = int(input("Wins: "))
            losses = int(input("Losses: "))
            ties = int(input("Ties: "))
            break
        except ValueError:
            print("Please enter a valid integer for wins, ties, losses.")
            continue
    #instantiate new player
    player = Player(name, wins, losses, ties)
    #add player to Db
    db.add_player(player)
    print(name, " was added to the database.")
    print()

def delete_player():
    name = input("Name: ")
    #delete player from DB
    db.delete_player(name)
    print(name, " was deleted from the database.")
    print()

def display_goodbye():
    print("Goodbye!")