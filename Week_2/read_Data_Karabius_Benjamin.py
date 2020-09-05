#!/usr/bin/env python3
#Ben Karabinus
#Comp 3006
#This program was created to practice using Python 3 csv module for file output
#9/4/2020


'''
Problem Description:

Implement a simple Python program called read_Data.py that utilizes the csv
module to read the attached file Data.csv. The program should read the file
without using DictReader, should ignore the first line, and should output the
contents of the row for which the second column has the maximum value.

'''

#import the csv module
import csv

#main function
def main():

    file = "data.csv"


    c_reader(file)


def c_reader(file):

    with open(file, "r") as file:

        reader = csv.reader(file)

        first = False
        max = 0


        for row in reader:
            if not first:
                first = True
            else:
                for row in reader:
                    if float(row[1]) > max:
                        max = float(row[1])
                        max_row = row
        print(max_row)













if __name__ == "__main__":
    main()
