#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 2/18/2020
#Project: Chapter 15 Rectangle Square Calculator
#Purpose: show basic understanding of object oriented design and
#inheritance in Python 3

#import the necessary classes
from shapes import Rectangle, Square

#function to display the title
def display_title():
    print("Rectangle Calculator")
    print()

#function to get the shapes dimensions snd validate input
def get_dimensions(shape):

    #control loop for handling exceptions
    while True:
        #accept user input based upon shape
        if shape.lower() == "r":
            try:
                height = int(input("Height: "))
                width = int(input("Width: "))
            except ValueError:
                print("Please enter a valid integer for height and width.")
                continue
            return height, width
        elif shape.lower() == "s":
            try:
                length = int(input("length: "))
            except ValueError:
                print("Please enter a valid integer for length: ")
                continue
            return length

#main function
def main():

    display_title()
    #declare loop control variable
    choice = "y"

    #main control loop
    while choice.lower() == "y":
        #prompt user to select shape
        shape = input("Rectangle or Square (r/s): ")
        #rectangle
        if shape == "r":
            height, width = get_dimensions(shape)
            #create Rectagle object
            rectangle = Rectangle(height,width)
            #print perimeter to console
            print("Perimeter: ", rectangle.get_perimeter())
            #print area to console
            print("Area: ", rectangle.get_area())
            #print string representation to console
            print(rectangle)

        #square
        elif shape.lower() == "s":
            length = get_dimensions(shape)
            #create square object
            square = Square(length)
            #print perimeter to console
            print("Perimeter: ", square.get_perimeter())
            #print area to console
            print("Area: ", square.get_area())
            #print string representation to console
            print(square)

        #enforce "r" or "s"
        else:
            print("That is not a valid shape!")
        print()
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")



#if main module run main function
if __name__ == "__main__":
    main()