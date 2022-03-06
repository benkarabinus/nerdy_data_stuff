"""
Ben Karabinus
University of Denver
COMP 4581, Winter Quarter 2022
Assignemnt 3

"""

from inspect import Traceback
import pandas as pd


def loadInvestments(path):

    realEstate = pd.read_csv(path)
    print(realEstate.head())
    realEstate.drop([0, 0], inplace=True)
    print(realEstate.head())
    realEstate = realEstate[['RegionName', 'Zhvi', '10Year']]
    realEstate.rename(columns={'RegionName': 'InvestmentName',
                               'Zhvi': 'InvestmentCost'}, inplace=True)
    print(realEstate.head())
    realEstate['EstimatedReturnOnInvestment'] = (realEstate['InvestmentCost'] *
                                                 realEstate['10Year'])
    print(realEstate.head())

    realEstateList = realEstate.values.tolist()
    return realEstateList

    #investmentName = realEstate['InvestmentName'].values.tolist()
    #investmentCost = realEstate['InvestmentCost'].values.tolist()
    #estimatedReturn = realEstate['EstimatedReturnOnInvestment'].values.tolist()
    #return investmentName, investmentCost, estimatedReturn


def optomizeinvestments(funds, numProperties, properties):

    # capacity number of columns, numberItems number of rows
    dpTable = [[0 for i in range(funds+1)] for j in range(numProperties+1)]
    traceback = [[0 for i in range(funds+1)] for j in range(numProperties+1)]
    
    #print(dpTable)

    for row in range(0, numProperties+1):
        for column in range(0, funds+1):
            # base case
            if row == 0 or column == 0:
                dpTable[row][column] = 0
                traceback[row][column] = 0
            elif properties[row-1][1] <= column:
                dpTable[row][column] = max(dpTable[row-1][column], dpTable[row-1]
                                         [column-properties[row-1][1]] +
                                         properties[row-1][3])
                traceback[row][column] = properties[row-1]
            else:
                dpTable[row][column] = dpTable[row-1][column]
                traceback[row][column] = traceback[row-1][column]
        print(row)
    maxReturn = dpTable[51][len(dpTable[51])-1]
    return dpTable, traceback, maxReturn


def trace(dpTable, traceback, row, column):

    winners = []

    while dpTable[row][column]:

        if dpTable[row][column] != dpTable[row-1][column]:
            winner = traceback[row][column]
            winners.append(winner)
            row -= 1
            column -= winner[1]
        else:
            winner = traceback[row][column]
            row -= 1

    return winners


def main():

    path = ('/Users/benkarabinus/Documents/Git/nerdy_data_stuff'
            '/DU/COMP4581/Assignment3/State_Zhvi_Summary_AllHomes.csv')
    properties = loadInvestments(path)
    funds = 1000000
    numProperties = len(properties)
    dpTable, traceback, maxReturn = optomizeinvestments(funds, numProperties,
                                                        properties)
    print(maxReturn)
    trace(dpTable, traceback, numProperties, funds)




if __name__ == '__main__':
    main()
