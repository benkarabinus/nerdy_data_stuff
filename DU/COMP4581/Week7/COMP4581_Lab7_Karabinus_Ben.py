"""
Ben Karabinus
University of Denver
COMP 4581, Winter Quarter 2022
Lab 7
"""

from time import time


# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    else: # The recursive case
        minCoins = float("inf")
        for currentCoin in coins: # Check all coins
        # If we can give change
            if (amount - currentCoin) >= 0:
                # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
            # Keep the best
                minCoins = min(minCoins, currentMin)
    return minCoins


# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    # Create the initial tables
    minCoins = [None for i in range(amount+1)]
    makeChange = [None for i in range(amount+1)]
    change = []
    # Fill in the base case(s)
    minCoins[0] = 0
    makeChange[0] = 0
    # Fill in the rest of the table
    for tableIndex in range(1, amount+1):
        #print(minCoins)
        result = tableIndex
        makeChange[tableIndex] = 1
        for i in range(len(coins)):
            if coins[i] <= tableIndex:
                #remainder = (tableIndex-coins[i])
                currentResult = 1 + minCoins[tableIndex-coins[i]]
                if currentResult < result:
                    result = currentResult
                    makeChange[tableIndex] = coins[i]
        minCoins[tableIndex] = result

    # Perform the traceback to print result
    while amount != 0:
        change.append(makeChange[amount])
        amount -= makeChange[amount]

    return minCoins[-1], change


def main():

    C = [1, 5, 10, 12, 25] # coin denominations (must include a penny)
    A = int(input('Enter desired amount of change: '))
    assert A >= 0

    print("DAC:")
    t1 = time()
    numCoins = DACcoins(C, A)
    t2 = time()
    print("optimal:", numCoins, " in time: ", round((t2-t1)*1000, 1), "ms")
    print()

    print("DP:")
    t1 = time()
    numCoins, change = DPcoins(C, A)
    t2 = time()
    [print(coin) for coin in change]
    print("optimal:", numCoins, " in time: ", round((t2-t1)*1000, 1), "ms")


if __name__ == '__main__':
    main()
