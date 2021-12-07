#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 2/18/2020
#Project: Chapter 17 Player Manager
#Purpose: show basic understanding of working with SQL Lite database
# in Python 3

#import necessary modules
import sqlite3
from contextlib import closing
from player import Player
#set DB connection (local file)
conn = sqlite3.connect("player_db.sqlite")



#get players from DB
def get_players():
    query = '''SELECT name, wins, losses, ties, (wins + losses + ties) as games
               FROM Player
               ORDER BY wins DESC'''
    #catch DB exception
    try:
        with closing(conn.cursor()) as c:
            c.execute(query)
            results = c.fetchall()
    except sqlite3.OperationalError as e:
        message = "Error reading database -", e
        results = None

    if results != None:
        #convert results to list of player instances
        players = []
        for row in results:
            player = Player(row[0], row[1], row[2], row[3], row[4])
            players.append(player)
        return players
    else:
        return message

#add player to DB
def add_player(player):

    sql = '''INSERT INTO Player (name, wins, losses, ties) 
             VALUES (?, ?, ?, ?)'''
    #catch DB exception
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (player.name, player.wins, player.losses,
                            player.ties))
        #commit changes to DB
        conn.commit()
    except sqlite3.OperationalError as e:
        message = ("Error reading database -", e)
        results = None
        return message

#delete player
def delete_player(name):
    sql = '''DELETE FROM Player WHERE name = ?'''
    #catch DB exception
    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (name,))
        #commit changes to DB
        conn.commit()
    except sqlite3.OperationalError as e:
        message = ("Error reading database -", e)
        results = None
        return message


