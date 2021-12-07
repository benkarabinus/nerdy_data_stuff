#!/usr/bin/env python3
#Name: Ben Karabinus
#Date: 9/1/2020
#Project: Week 1 Programming Assignment
#Purpose: show basic understanding of using python 3 from command line interface

import sys
import statistics as stats


data = []

for line in sys.stdin.readlines():
    line = float(line)
    if line != -9999.0:
        data.append(line)
print("Min:",min(data) , "Max:", max(data) ,"Average:", round(stats.mean(data),4)
 ,"Median:", stats.median(data))
