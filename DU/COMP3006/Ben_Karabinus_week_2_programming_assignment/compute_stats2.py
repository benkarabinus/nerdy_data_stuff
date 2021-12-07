#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 9/9/2020
#Project: Week 2 Programming Assignment
#Purpose: show basic understanding of using python 3 for software testing

#import the necessary modules
import sys, csv
import statistics as stats


#main function
def main():

    #if file_name read from speified file
    if len(sys.argv) > 2:

        #assign command line arguuments column # and file name to respective variables
        col = int(sys.argv[1])
        file_name = sys.argv[2]
        print(compute_stats(read_file(file_name, col)))

    #if not filename read from standard input
    else:
        col = int(sys.argv[1])
        print(compute_stats(read_standard_input(col)))


#function to read specified column from standard input and return a sorted list
def read_standard_input(col):

    reader = csv.reader(sys.stdin, delimiter=' ', skipinitialspace=True)
    data = []
    for row in reader:
        if float(row[col - 1]) != -9999.0:
            data.append(float(row[col -1 ]))
            #sort(ascending) and return data
    data.sort()
    return data


#function to read specified column from specified file and return a sorted list
def read_file(file_name, col):

    with open(file_name, "r") as file:
        #create file reader object and empty list to store data
        reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
        data = []
        #pull data from specified column
        for row in reader:
            if float(row[col - 1]) != -9999.0:
                data.append(float(row[col -1 ]))
    #sort(ascending) and return data
    data.sort()
    return data





#function to return descriptive statistics for specified column
def compute_stats(values):
    #if no data stats == none
    if len(values) == 0:
        o_min = None
        o_max = None
        o_average = None
        o_median = None

    else:
        o_min = min(values)
        o_max = max(values)
        o_average = round(stats.mean(values),4)
        o_median = stats.median(values)

    #return stats as tuple
    return (o_min, o_max, o_average, o_median)






#if main run main
if __name__ == '__main__':
    main()
