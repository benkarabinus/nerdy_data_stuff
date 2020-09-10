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

    #assign command line arguuments column # and file name to respective variables
    col = int(sys.argv[1])
    file_name = sys.argv[2]

    #call to functions containing program logic
    print(compute_stats(read_file(file_name, col)))


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
