"""
Ben Karabinus
COMP 4581 Lab 2
University of Denver, RSECS, Winter Quarter 2022
"""

# import needed modules
from time import time
import random
import copy



def main():

    # print table using str.format
    print("{}\t {}\t {}\t {}\t".format('N', 'Merge', 'Insert', 'Bubble'))

    # perform each type of sort on random integer list of length "i"
    for i in range(100, 5001, 100):
        A = [i for i in range(1, i+1)]
        random.shuffle(A)
        Merge = timeSort(copy.copy(A), mergeSort)
        Insert = timeSort(copy.copy(A), insertionSort)
        Bubble = timeSort(copy.copy(A), bubbleSort)
        print("{}\t {}\t {}\t {}\t".format(i, Merge, Insert, Bubble))


# function to merge lists
def merge(A, B):
    out = []
    i, j = 0,0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    while i < len(A):
        out.append(A[i])
        i += 1
    while j < len(B):
        out.append(B[j])
        j += 1
    return out

# function for merge sort
def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left, Right)

# function for insertion sort
def insertionSort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i-1
        while j >= 0 and L[j] > key:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key
    return L

# function for bubble sort
def bubbleSort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L


# function to time each sort
def timeSort(A, sortFunction):
    
    t1 = time()
    B = sortFunction(A)
    t2 = time()
    mtime = round((t2-t1)*1000,1)
    return mtime

if __name__ == '__main__':
    main()