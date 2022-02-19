"""
Ben Karabinus
University of Denver
COMP 4581, Winter quarter 2022
Assignment 1
"""

import pandas as pd
import numpy as np


def getData():

    prices = pd.read_csv('/Users/benkarabinus/Documents/Git/nerdy_data_stuff/'
                         'DU/COMP4581/Assignment2/prices-split-adjusted.csv')
    # prices = prices[prices['symbol'] == 'AAPL'] # filter to AAPL for testing
    securities = pd.read_csv('/Users/benkarabinus/Documents/Git/nerdy_data_stuff'
                             '/DU/COMP4581/Assignment2/securities.csv')
    # securities = securities[securities['Ticker symbol'] == 'AAPL'] # filter to AAPL for testing
    combined = pd.merge(securities[['Ticker symbol', 'Security']], prices,
                        left_on='Ticker symbol', right_on='symbol')
    tickers = combined['Ticker symbol'].unique().tolist()
    securities = combined['Security'].unique().tolist()
    companies = [tickers, securities]

    return combined, companies


def getTickers(securities):

    profits = {}
    for i in range(len(securities[0])):
        profits[securities[0][i]] = [securities[1][i]]
    return profits


def getProfits(combined, profits):

    maxProfit = (0, 0, 0)
    for ticker in profits.keys():
        company = combined[combined['Ticker symbol'] == ticker][['Ticker symbol',
                                                                'date',  'close']]
        company['change'] = company.close.diff()
        company.fillna(value=0, inplace=True)
        profits[ticker].append(company['change'].to_list())
        profits[ticker].append(company['date'].tolist())
        currentProfit = maxStockDAC(profits[ticker][1])
        if currentProfit[0] > maxProfit[0]:
            maxProfit = currentProfit
            maxTicker = ticker
    company = profits[maxTicker][0]
    buyDate = profits[maxTicker][2][maxProfit[1]-1]
    sellDate = profits[maxTicker][2][maxProfit[2]-1]
    profit = round(maxProfit[0], 2)

    return company, buyDate, sellDate, profit


def maxStockDAC(A, low=0, high=None, rightidx=0, leftidx=0):

    
    if high == None:
        high = len(A)-1
    # Base Case
    if low == high:
        if A[low] >0:
            return A[low], rightidx, leftidx # create a tuple to track date idx
        else:
            return 0, rightidx, leftidx # create a tuple to track date idx
    # Divide
    mid = (low+high) //2
    #conquer
    maxLeft = maxStockDAC(A, low, mid)
    maxRight = maxStockDAC(A, mid+1, high)

    # combine
    maxLeft2Center = left2Center = 0
    for i in range(mid, low-1, -1):
        left2Center += A[i]
        maxLeft2Center = max(left2Center, maxLeft2Center)
        if maxLeft2Center == left2Center:
            leftidx=i # starting date index
    maxRight2Center = right2Center = 0
    for i in range(mid+1, high+1):
        right2Center += A[i]
        maxRight2Center = max(right2Center, maxRight2Center)
        if maxRight2Center == right2Center:
            rightidx=i # ending date index
    # return
    if max(maxLeft[0], maxRight[0], maxLeft2Center+maxRight2Center) == maxLeft[0]:
        return maxLeft
    elif max(maxLeft[0], maxRight[0], maxLeft2Center+maxRight2Center) == maxRight[0]:
        return maxRight
    else:
        return maxLeft2Center + maxRight2Center, leftidx, rightidx


def main():

    combined, companies = getData()
    profits = getTickers(companies)
    profit = getProfits(combined, profits)
    print("Best stock to buy: \"{}\" on {} and sell on {} with a profit of ${:.2f}".format(profit[0], 
          profit[1], profit[2], profit[3]))


if __name__ == '__main__':
    main()
