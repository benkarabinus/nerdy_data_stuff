#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 3/5/2020
#Project: Chapter 17 Player Manager
#Purpose: show basic understanding of working with SQL Lite database
#in Python 3

#import necessary modules
import presentation_tier as display

#main function
def main():
    #display title from UI tier
    display.display_title()
    #Display command menu from UI tier
    display.display_command_menu()
    while True:
        #get user command
        command = display.get_command()
        if command == "view":
            #display all players in DB
            display.display_players()
        elif command == "add":
            #add player to DB
            display.add_player()
        elif command == "del":
            # delete player from DB
            display.delete_player()
        elif command == "exit":
            #display goodbye message
            display.display_goodbye()
            break
        else:
            #entry control
            print("Please enter a valid command.")
            continue


#if main module run main function
if __name__ == "__main__":
    main()
