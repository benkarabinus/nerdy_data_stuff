#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 1/27/2020
#Project: Chapter 4 Exercise Feet Meters Converter
#Purpose: show basic understanding of how to define and use functions and
#and modules in Pyhton 3

#function converting feet to meters
def feetToMeters(feet):

    meters = feet * .3048
    return round(meters,2)


#function converting meters to feet
def metersToFeet(meters):

    feet = meters/.3048
    return round(feet,2)


#test if this file is being used as the main module
if __name__ == "__main__":
    main()
