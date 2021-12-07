#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 3/10/2020
#Project: Chapter 18 Exercise Preferences
#Purpose: show basic understanding of how to create GUI
#in Python 3

#import csv module
import csv

#create variable for the filename
FILENAME = "preferences.csv"

#get user  preferences
def read_to_list():
    #initialize preferences list
    preferences = []
    #open file
    try:
        with open(FILENAME, newline="") as file:
            #create reader object
            reader = csv.reader(file)
            #write contents to list by row
            for row in reader:
                preferences.append(row)
            return tuple(preferences[0])
    #catch FileNotFoundError and set default values
    except FileNotFoundError:
        row =[]
        row.append("")
        row.append("English")
        row.append(10)
        preferences.append(row)
        return tuple(preferences[0])


#write list contents to csv file (this function is reuseable)
def preference_writer(preferences):
    #open file
    with open(FILENAME, "w", newline="") as file:
        #write contents to file by row
        writer = csv.writer(file)
        writer.writerows(preferences)

#this function is reuseable but is not needed for this program
#def add_preferences(person):
    #create new preferences list for person instance
    #preferences = []
    #preferences.append(person.name)
    #preferences.append(person.language)
    #preferences.append(person.save_time)
    #return preferences
