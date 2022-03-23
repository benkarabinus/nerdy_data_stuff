"""
Ben Karabinus
University of Denver
COMP 4581, Winter Quarter 2022
Assignemnt 3

"""

import pandas as pd


def loadInvestments(path):

    realEstate = pd.read_csv(path)
    realEstate.drop([0, 0], inplace=True)
    realEstate = realEstate[['RegionName', 'Zhvi', '10Year']]
    realEstate.rename(columns={'RegionName': 'InvestmentName',
                               'Zhvi': 'InvestmentCost'}, inplace=True)
    realEstate['EstimatedReturnOnInvestment'] = (realEstate['InvestmentCost'] *
                                                 realEstate['10Year'])
    realEstateList = realEstate.values.tolist()

    return realEstateList


def optomizeinvestments(funds, numProperties, properties):

    # capacity number of columns, numberItems number of rows
    dpTable = [[None for i in range(funds+1)] for j in range(numProperties+1)]
    traceback = [[None for i in range(funds+1)] for j in range(numProperties+1)]

    for row in range(0, numProperties+1):
        for column in range(0, funds+1):
            # base case
            if row == 0:
                dpTable[row][column] = 0
                traceback[row][column] = 0
            # else if item weight <= current allowed weight (the column)
            # then select max(previousknpsack or currentKnapsack)
            elif properties[row-1][1] <= column:
                dpTable[row][column] = max(dpTable[row-1][column], dpTable[row-1]
                                           [column-properties[row-1][1]] +
                                           properties[row-1][3])
                traceback[row][column] = properties[row-1]
            # else item is too heavy keep previous knapsack
            else:
                dpTable[row][column] = dpTable[row-1][column]
                traceback[row][column] = traceback[row-1][column]
        # print row for sanity check
        print(row)
    maxReturn = dpTable[51][len(dpTable[51])-1]

    return dpTable, traceback, maxReturn


def trace(dpTable, traceback, row, column):

    # create list to hold the winners
    winners = []
    # do while table[row][colum] not equal to zero
    while dpTable[row][column]:
        # if item is not from previous row then winner
        if dpTable[row][column] != dpTable[row-1][column]:
            winner = traceback[row][column]
            winners.append(winner)
            row -= 1
        # subtract weight of the winner to decrement appropriate num columns
            column -= winner[1]
        else:
            winner = traceback[row][column]
            row -= 1

    return winners


def main():

    path = ('/Users/benkarabinus/Documents/Git/nerdy_data_stuff'
            '/DU/COMP4581/Assignment3/State_Zhvi_Summary_AllHomes.csv')
    properties = loadInvestments(path)
    # the capacity of the knapsack (columns)
    funds = 1000000
    # the number of items (rows)
    numProperties = len(properties)
    dpTable, traceback, maxReturn = optomizeinvestments(funds, numProperties,
                                                        properties)
    winners = trace(dpTable, traceback, numProperties, funds)
    print("The optimal states in which to invest the alloted one million dollars "
          "are as follows:")
    print()
    for winner in winners:
        print("{}, Purchase Price: ${:,.2f}, 10-Year Return: {:.2%}, "
        "Estimeated Return: ${:,.2f}".format(winner[0], winner[1], winner[2],
                                             winner[3]))
        print()
    print("The total return on investment is ${:,.2f}".format(maxReturn))


if __name__ == '__main__':
    main()
