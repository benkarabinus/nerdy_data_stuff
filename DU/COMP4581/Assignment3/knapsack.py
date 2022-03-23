"""
Ben Karabinus
0/1 knapsack example
3/5/2022

"""


def knapsackDP(capacity, numberItems, values):

    # capacity number of columns, numberItems number of rows
    table = [[None for i in range(capacity+1)] for j in range(numberItems+1)]
    traceback = [[None for i in range(capacity+1)] for j in range(numberItems+1)]

    for row in range(0, numberItems+1):
        for column in range(0, capacity+1):
            # base case
            if row == 0:
                table[row][column] = 0
                traceback[row][column] = 0
            # else if item weight <= current allowed weight (the column)
            # then select max(previousknpsack or currentKnapsack)
            elif values[row-1][1] <= column:
                table[row][column] = max(table[row-1][column], table[row-1]
                                         [column-values[row-1][1]] +
                                         values[row-1][2])
                traceback[row][column] = values[row-1]
            # else item is too heavy keep previous knapsack
            else:
                table[row][column] = table[row-1][column]
                traceback[row][column] = traceback[row-1][column]

    return table, traceback


def trace(table, traceback, row, column):

    # create list to hold the winners
    winners = []

    # do while table[row][colum] not equal to zero
    while table[row][column]:
        # if item is not from previous row then winner
        if table[row][column] != table[row-1][column]:
            winner = traceback[row][column]
            winners.append(winner)
            row -= 1
        # subtract the weight of the winner to decrement appropriate num columns
            column -= winner[1]
        else:
            winner = traceback[row][column]
            row -= 1

    return winners




def main():

    # the capacity of my knapsack
    capacity = 7
    # number items is 4
    numberItems = 4
    # there are values and weights for each item
    items = ['A', 'B', 'C', 'D']
    values = [['A', 1, 1], ['B', 3, 4], ['C', 4, 5], ['D', 5, 7]]
    table, traceback = knapsackDP(capacity, numberItems, values)
    winners = trace(table, traceback, numberItems, capacity)
    [print(winner) for winner in winners]


if __name__ == '__main__':
    main()
