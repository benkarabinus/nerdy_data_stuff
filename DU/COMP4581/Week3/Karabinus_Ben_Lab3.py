"""
Ben Karabinus
University of Denver
COMP 4581 Winter Quarter 2022
Lab 3
"""

import random
from time import time
from csv import writer

"""
Assignment Comments

The encryption cracking function "def factor(pq)" was run on my personal laptop.
Bit lengths ranging from 15 to 30 were used for each run. Bit lenghts of above 30
took around 5 minutes to run. Fiting an exponential curve to the data using
Excel produced the following results:

Equation for exponential fit: y = 7E-06e^0.7413x

Approximate time 1024 bits (milliseconds): 3E+300

Approximate time 1024 bits (years): 9.506426E+289

"""


def main():

    n = int(input("Please enter a positive integer value gretater than or "
            "equal to 15 for the number of bits: "))
    # with open("RSACracking.csv", 'w') as file:
        # csv_writer = writer(file)
    print("{}\t {}\t".format('Bits', 'Time (milliseconds)'))
    for n in range(15, n+1):
        pq = nBitPrime(n)*nBitPrime(n)
        # print(pq)
        t1 = time()
        p, q, = factor(pq)
        t2 = time()
        mtime = (t2-t1)*1000
        # print(p,q)
        # print(mtime)
        print("{}\t {}\t".format(n, mtime))
        # csv_writer.writerow([n, mtime])


def isPrime(p):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


def nBitPrime(n):

    randNum = random.random()
    p = int(2**n * randNum)
    while p < 2 or not isPrime(p):
        randNum = random.random()
        p = int(2**n * randNum)
    return p


def factor(pq):
    for i in range(2, pq+1):
        if pq % i == 0:
            p = i
            q = pq/p
            return p, q


if __name__ == '__main__':
    main()
