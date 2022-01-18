"""
Ben Karabinus
COMP 4433 Winter Quarter 2022
Assignmnt 1
"""


# import needed modules
import numpy as np
import pandas as pd
import random


def main():

    partOne()
    #partTwo()
    #partThree()
    #partFour()


def partOne():

    # read in the elements csv file
    elements = pd.read_csv('elements.csv')
    nineTen = [{'name': 'Fluorine', 'symbol': 'F', 'atomicNumber': 9},
               {'name': 'Neon', 'symbol': 'Ne', 'atomicNumber': 10}]
    print(elements)
    elements = elements.append(nineTen, ignore_index=True)
    print(elements)
    # add atomic weights rounded to the nearest integer
    elements['atomicWeights'] = [1.08, 4.003, 6.940, 9.012, 10.810, 12.001,
                                 14.007, 15.999, 18.998, 20.180]
    elements = elements.round({"atomicWeights": 0})
    print(elements)


# part 2
def partTwo():
    # greek alphabet list
    letters = ['alpha', 'beta', 'gamma', 'delta', 'epsilon',
               'zeta', 'eta', 'theta', 'iota']
    random.shuffle(letters)

    # random np.arrays
    mu = 10
    sigma = 1.5
    arr1 = sigma * np.random.randn(9) + mu
    arr2 = sigma * np.random.randn(9) + mu

    # nine element array ranging from 0 to 2*pi
    angle = np.random.uniform(0, 2*np.pi, 9)
    cosine = np.cos(angle)
    mixedDict = {'letters': letters, 'arr1': arr1, 'arr2': arr2,
                 'angle': angle, 'cosine': cosine}
    mixedDataframe = pd.DataFrame(mixedDict)
    print(mixedDataframe)
    mixedDataframe.sort_values(by='letters', ascending=True, inplace=True)
    mixedDataframe.drop(['arr2', 'cosine'], axis=1, inplace=True)
    mixedDataframe = mixedDataframe[mixedDataframe.letters != 'zeta']
    print(mixedDataframe)


# part 3
def partThree():

    # function to print fibonacci numbers
    def fibonacci(n):
        fibArray = []
        for i in range(n+1):
            if i == 0:
                fibArray.append(i)
            elif i == 1 or i == 2:
                fibArray.append(1)
            else:
                fibArray.append(fibArray[i-1]+fibArray[i-2])
        fibRatio = []
        for i in range(len(fibArray)-4, len(fibArray)):
            fibRatio.append(fibArray[i]/fibArray[i-1])
        return fibArray, fibRatio
    fibArray, fibRatio = fibonacci(12)
    print(fibArray)
    print(fibRatio)
    print("The ratio of any two successive Fibonacci numbers "
          "is very close to the Goden Ratio. A number naturally occuring"
          " in nature.")


# part 4
def partFour():

    def kelvinToRankine(*args):
        for arg in args:
            print(arg * (9/5))
    kelvinToRankine(1000, 2000, 3000, 4000, 5000)
    kelvins = [1000, 2000, 3000, 4000, 5000]
    convert = lambda temp: temp*(9/5)
    kelvins = [convert(temp) for temp in kelvins]
    [print(temp) for temp in kelvins]


if __name__ == '__main__':
    main()