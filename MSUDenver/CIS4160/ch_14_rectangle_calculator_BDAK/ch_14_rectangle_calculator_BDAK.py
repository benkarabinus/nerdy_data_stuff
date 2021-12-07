#!/usr/bin/env python3
# Name: Ben Karabinus
# Date: 2/23/2020
# Project: Chapter 14 Rectangle Calculator
# Purpose: show basic understanding of defining and using
# classes in Python 3

#import the necessary classes
from shapes import Rectangle

#function to display the title
def display_title():
    print("Rectangle Calculator")
    print()

# function to get the shapes dimensions snd validate input
def get_dimensions():
    # control loop for handling exceptions
    while True:
            try:
                # get user input
                height = int(input("Height: "))
                width = int(input("Width: "))
            # catch exceptions
            except ValueError:
                print("Please enter a valid integer for height and width.")
                continue
            return height, width

#main function
def main():

    display_title()
    #declare loop control variable
    choice = "y"

    #main control loop
    while choice.lower() == "y":
        # create Rectangle
        height, width = get_dimensions()
        # create Rectagle object
        rectangle = Rectangle(height,width)
        # print perimeter to console
        print("Perimeter: ", rectangle.get_perimeter())
        # print area to console
        print("Area: ", rectangle.get_area())
        # print string representation to console
        print(rectangle)
        print()
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")



#if main module run main function
if __name__ == "__main__":
    main()