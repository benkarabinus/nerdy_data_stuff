#!/usr/bin/env python3
#Ben Karabinus
#Comp 3006
#This program was created to practice using Python 3 csv module for file output
#9/3/2020

#import the csv module
import csv

#main function
def main():

    #call to function c_writer
    c_writer()


def c_writer():

    with open("output.csv", "w") as file:

        fieldnames = ("x","f(x)=x**2+10x+10")

        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()


        x = -20

        while x < 21:
            fx = x**2+10*x+10
            writer.writerow({'x':x, "f(x)=x**2+10x+10": fx})
            x += 0.1






if __name__ == "__main__":
    main()
