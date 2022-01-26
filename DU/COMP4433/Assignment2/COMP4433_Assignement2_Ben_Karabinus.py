"""
Ben Karabinus
University of Denver
COMP 4433, Winter Quarter 2022
Assignmnt 2
"""
from shutil import which
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


def main():

    partOne()
    #partTwo()
    #partThree()
    #partFour()


def partOne():
    weights = np.rint(np.array([1.08, 4.003, 6.940, 9.012, 10.810, 12.001]))
    weights = weights.astype(int)
    title = "Atomic Weights"
    title2 = "Atomic Weights (Pct of Whole)"
    labels = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
    explodeOne = (0, 0, 0, 0, 0, 0.1)
    explodeTwo = (0, 0.1, 0, 0, 0, 0)
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    ax[0].set_title(title)
    ax[0].pie(weights, labels=labels, explode=explodeOne,
              autopct=lambda p: '{:.0f}'.format(p*sum(weights)/100))
    ax[0].axis('equal')  # no ovular pie charts
    ax[1].set_title(title2)
    ax[1].pie(weights, labels=labels, explode=explodeTwo,
              autopct='%1.1f%%')
    ax[1].axis('equal')  # no ovular pie charts
    plt.show()


def partTwo():

    ide = pd.read_csv('/Users/benkarabinus/Documents/Git/nerdy_data_stuff/DU/'
                      'COMP4433/Assignment2/py_ide2.csv')
    fig, ax = plt.subplots(1, 2, figsize=(14, 8))
    ax[0].barh(ide['IDE'], ide['Adoption'])
    ax[0].set_title('IDE (User Adoption)')
    ax[0].set_xlabel('User Adoption')
    ax[0].set_ylabel('Platform')
    plt.xticks(range(len(ide)), ide['IDE'], rotation=65)
    ax[1].bar(range(len(ide)), ide['Adoption'])
    ax[1].set_title('IDE (User Adoption)')
    ax[1].set_ylabel('User Adoption')
    ax[1].set_xlabel('Platform')
    plt.tight_layout()
    plt.show()


def partThree():

    dates = ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
             '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08']
    nums = np.random.uniform(100, 201, 8)
    df = pd.DataFrame({'date': dates, 'nums': nums})
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    fig = plt.figure(figsize=(16, 8))
    ax0 = fig.add_axes([0.15, 0.25, 0.3, 0.4])
    ax0.plot(df['nums'])
    ax0.grid(which='major', alpha=0.25)
    plt.xticks(rotation=65)
    ax1 = fig.add_axes([0.525, 0.25, 0.3, 0.4])
    ax1.bar(df.index, df['nums'])
    plt.xticks(rotation=65)
    ax0.set_title("Dates vs Numbers (Line)")
    ax1.set_title("Dates vs Numbers (Bar)")
    plt.tight_layout()
    plt.show()


def partFour():

    googleJan21 = yf.download('GOOGL', '2021-01-01', '2021-01-31')
    fig = plt.figure(figsize=(16, 8))
    fig.align_xlabels()
    ax0 = fig.add_axes([0.1, 0.55, 0.8, 0.3])
    ax0.plot(googleJan21['High'], 'g', label='High')
    ax0.plot(googleJan21['Low'], 'r', label='Low')
    ax0.plot(googleJan21['Open'], 'b', label='Open')
    ax0.set_title("Google Stock Prices January 2021 (USD)")
    plt.legend()
    ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.3])
    ax1.plot(googleJan21.index, googleJan21['Volume'])
    ax1.set_title("Google Stock Volume January 2021 (millions of shares)")
    plt.show()


if __name__ == '__main__':
    main()
