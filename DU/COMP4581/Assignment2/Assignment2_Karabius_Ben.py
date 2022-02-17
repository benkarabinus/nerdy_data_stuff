"""
Ben Karabinus
University of Denver
COMP 4581, Winter quarter 2022
Assignment 1
"""

import pandas as pd
import numpy as np
from collections import OrderedDict


def readStocks(ticker):

    prices = pd.read_csv('/Users/benkarabinus/Documents/Git/nerdy_data_stuff/'
                         'DU/COMP4581/Assignment2/prices-split-adjusted.csv')
    
    prices = prices[prices['symbol'] == ticker]
    prices['change'] = prices.close.diff()
    prices.fillna(value=0, inplace=True)
    date = prices['date'].values.tolist()
    changes = prices['change'].values.tolist()

    change = {'AAPL': [date, changes]}
    
    return prices, change

def getData():

    prices = pd.read_csv('/Users/benkarabinus/Documents/Git/nerdy_data_stuff/'
                         'DU/COMP4581/Assignment2/prices-split-adjusted.csv')
    prices = prices[prices['symbol'] == 'AAPL']
    print(prices.head())
    securities = pd.read_csv('/Users/benkarabinus/Documents/Git/nerdy_data_stuff'
                             '/DU/COMP4581/Assignment2/securities.csv')
    securities = securities[securities['Ticker symbol'] == 'AAPL']
    print(securities.head())
    combined = pd.merge(securities[['Ticker symbol', 'Security']], prices, left_on='Ticker symbol', right_on='symbol' )
    print(combined)
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
        company = combined[combined['Ticker symbol'] == ticker][['Ticker symbol','date',  'close']]
        company['change'] = company.close.diff()
        company.fillna(value=0, inplace=True)
        print(company.head())
        profits[ticker].append(company['change'].to_list())
        profits[ticker].append(company['date'].tolist())
        currentProfit = MSSDAC(profits[ticker][1])
        if currentProfit[0] > maxProfit[0]:
            maxProfit = currentProfit
            maxTicker = ticker
    company = profits[maxTicker][0]
    buyDate = profits[maxTicker][2][maxProfit[1]-1]
    sellDate = profits[maxTicker][2][maxProfit[2]-1]
    profit = round(maxProfit[0], 2)
    return company, buyDate, sellDate, profit







def MSSDAC(A, low=0, high=None, rightidx=0, leftidx=0):

    
    if high == None:
        high = len(A)-1
        
    # Base Case
    if low == high:
        if A[low] >0:
            return A[low], rightidx, leftidx
        else:
            return 0, rightidx, leftidx
    # Divide
    mid = (low+high) //2
    #conquer
    maxLeft = MSSDAC(A, low, mid)
    #print(maxLeft)
    maxRight = MSSDAC(A, mid+1, high)
    #print(maxRight)
    # combine
    maxLeft2Center = left2Center = 0
    
    for i in range(mid, low-1, -1):
        left2Center += A[i]
        maxLeft2Center = max(left2Center, maxLeft2Center)
        if maxLeft2Center == left2Center:
            leftidx=i
        
    #print(maxLeft2Center)
    maxRight2Center = right2Center = 0
    for i in range(mid+1, high+1):
        right2Center += A[i]
        maxRight2Center = max(right2Center, maxRight2Center)
        if maxRight2Center == right2Center:
            rightidx=i

        
    #print(maxRight2Center)
    #return max(maxLeft, maxRight, maxLeft2Center+maxRight2Center)
    if max(maxLeft[0], maxRight[0], maxLeft2Center+maxRight2Center) == maxLeft[0]:
        return maxLeft
    elif max(maxLeft[0], maxRight[0], maxLeft2Center+maxRight2Center) == maxRight[0]:
        return maxRight
    else:
        return maxLeft2Center + maxRight2Center, leftidx, rightidx





def main():

    combined, companies = getData()
    profits = getTickers(companies)
    getProfits(combined, profits)
    #prices, change = readStocks('AAPL')
    #print(prices)
    #val = MSSDAC(change['AAPL'][1])
    #print(val)
    start = change['AAPL'][0][val[1]]
    print(start)
    

if __name__ == '__main__':
    main()
