#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 1/21/2020
#Project: Chapter 3 Exercise Change Calculator
#Purpose: show basic understanding of boolean operators and control statements

def main():

    #loop control variable
    choice = "y"
    
    #Main control loop
    while choice.lower() == "y":

        print("Change Calculator")
        print()
        change = int(input("Enter number of cents (0-99): "))
        print()

        #calculate change forcing rounding
        quarters = (change//25)
        change = change - (quarters * 25)
        dimes = (change//10)
        change = change - (dimes * 10)
        nickles = (change//5)
        change = change - (nickles * 5)
        pennies = change
        
        #print change to console
        print("Quarters: ",quarters)
        print("Dimes:    " ,dimes)
        print("Nickles:  " ,nickles)
        print("Pennies:  " ,pennies)
        print()

        choice = input("Continue? (y/n): ")
       
        print()
        
    print("Bye!")

    
        
        
    


if __name__ == "__main__":
    main()
