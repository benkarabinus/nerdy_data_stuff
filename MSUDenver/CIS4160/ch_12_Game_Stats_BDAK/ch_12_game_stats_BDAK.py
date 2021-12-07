#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 2/18/2020
#Project: Chapter 12 Exercise Game Stats
#Purpose: show basic understanding of how to use dictionaries
#in Python 3

#function to display title
def display_title():
    print("Game Stats Program")
    print()

#function to display players list
def display_players(players):
    #create a list of players
    players = list(players.keys())
    #sort list in alphabetical order
    players.sort()
    #print list to console
    print("ALL PLAYERS")
    for name in players:
        print(name)
    print()

#function to select a player
def select_player(players,player):
    #search dictionary for selected player
    if player in players:
        player = players[player]
        #print player stats to console
        print("Wins: ", player["Wins"])
        print("Losses: ", player["Losses"])
        print("Ties: ", player["Ties"])
        print()
     #inform user their entry was not found
    else:
        print("There is no player named " + player +".")
        print()


#main function
def main():
    #initialize dictionary players
    players = {
        "Ben":
            {"Wins": 0, "Losses": 60, "Ties": 0},
        "Elizabeth":
            {"Wins": 41, "Losses": 3, "Ties": 22 },
        "Joel":
            {"Wins": 32, "Losses": 14, "Ties": 17},
        "Mike":
            {"Wins": 8, "Losses": 19, "Ties": 11}
        }

    display_title()
    display_players(players)

    choice = "y"
    while choice.lower() != "n":
        #set player == user input
        player = input("Enter a player name: ")
        select_player(players, player)
        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")

#if main module run main function
if __name__ == "__main__":
    main()