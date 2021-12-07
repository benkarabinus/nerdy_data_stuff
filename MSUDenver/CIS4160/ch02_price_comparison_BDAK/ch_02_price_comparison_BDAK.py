#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 1/21/2020
#Project: chapter 2 exercise price comparison
#Purpose: writing your first simple program in Python 3

#the function price_per_unit calculates the price per unit for a given detergent
#rounding to two decimal places
def price_per_unit(units, price):

    price_per_unit = round(price/units, 2)
    
    #if price per unit is greater than or equal to one dollar then print result in dollars 
    if price_per_unit >= 1:

        return "$" +str(price_per_unit)
    
    #if price per unit is less than one dollar print result in cents  
    else:
        return str((price_per_unit * 100)) + " cents"
        
    




#main function of the program
def main():

    print("Price Comparison")
    print()
    print()
    units_1 = float(input("Please enter the size of the first laundry detergent (e.g. if 10oz enter 10): "))
    price_1 = float(input("Please enter the price of the first laundry detergent (e.g. 5.99): "))
    print()
    print()
    units_2 = float(input("Please enter the size of the second laundry detergent (e.g. if 10oz enter 10): "))
    price_2 = float(input("Please enter the price of the second laundry detergent (e.g. 5.99): "))
    print()
    print()
    print("The price per unit of the first detergent is " +price_per_unit(units_1, price_1)+" per unit" )
    print("The price per unit of the second detergent is " + price_per_unit(units_2, price_2)+ " per unit")
    print()
    print("Bye")
    
    
    
    

    


if __name__ == "__main__":
    main()
