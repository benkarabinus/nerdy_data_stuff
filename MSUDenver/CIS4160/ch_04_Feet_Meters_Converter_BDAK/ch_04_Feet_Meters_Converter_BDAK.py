#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 1/27/2020
#Project: Chapter 4 Exercise Feet Meters Converter
#Purpose: show basic understanding of how to define and use functions and
#modules in Pyhton 3

#import the conversion module
import conversion

#function to display title
def displayTitle():

    print("Feet and Meters Converter")

#function to display menu
def displayMenu():

    print("Conversions Menu:")
    print("a.\tFeet to Meters")
    print("b.\tMeters to Feet")
    
#main function
def main():

    
    displayTitle()

    #loop control variable 
    control = "y"
    
    #main control loop
    while control == "y":

        displayMenu()

       #user chooses feet or meters
        choice = input("Select a Conversion (a/b): ")
        print()

        #boolean statements testing user choice
        if choice.lower() == "a":
             feet = float(input("Enter Feet: "))
             print(conversion.feetToMeters(feet), " meters")
             
        elif choice.lower() == "b":
            meters = float(input("Enter Meters: "))
            print(conversion.metersToFeet(meters), " feet")
            
        print()

        #ask if user would like to perform another conversion and assign
        #input to the loop control variable
        control = input("Would you like to perform another conversion? (y/n): ")
        print()
    print()
    print("Thanks, bye!")


    
#test if this file is being used as the main module
if __name__ == "__main__":
    main()
