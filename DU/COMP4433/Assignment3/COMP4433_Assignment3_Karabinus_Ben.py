"""
Ben Karabinus
University of Denver
COMP 4433, Winter Quarter 2022
Assignment 3
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

mpg = sns.load_dataset('mpg')
diamonds = sns.load_dataset('diamonds')
car_crashes = sns.load_dataset('car_crashes')
iris = sns.load_dataset('iris')


def partOne():

    # Part 1 - Correlation Heatmap
    sns.set_style('darkgrid')
    sns.heatmap(mpg.corr(), cmap='coolwarm')
    plt.title("Correlation Heatmap MPG")
    plt.tight_layout()
    plt.show()
    # Part 1 - Simple Pairplot
    g0 = sns.pairplot(mpg, height=1.5, aspect=1)
    g0.fig.suptitle("Pairplot MPG",)
    plt.tight_layout()
    plt.show()


def partTwo():

    print(diamonds.head())
    print(diamonds.color.unique())
    print(diamonds.cut.unique())
    diamondsFiltered = diamonds[(diamonds.color != 'E') &
                                (diamonds.color != 'D') &
                                (diamonds.cut != 'Fair')]
    print(diamondsFiltered.color.unique())
    print(diamondsFiltered.cut.unique())
    g0 = sns.FacetGrid(diamonds, col='cut', row='color', height=1.5, aspect=1.5)
    g0.fig.suptitle("Scatterplot Diamonds")
    g0.map(sns.scatterplot, 'price', 'carat', )
    g0.tight_layout()
    plt.show()


# Part 3
def partThree():

    fig, ax = plt.subplots(1, 2, figsize=(14, 10))
    ax[0].set_title("Total as a Function of Speeding")
    ax[1].set_title("Total as a Function of Alcohol Consumption")
    sns.regplot(data=car_crashes, x='speeding', y='total', ax=ax[0])
    sns.regplot(data=car_crashes, x='alcohol', y='total', ax=ax[1])
    plt.show()


def partFour():

    fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True)
    sns.boxplot(data=iris, x='species', y='sepal_length', ax=axes[0, 0])
    sns.boxplot(data=iris, x='species', y='sepal_width', ax=axes[0, 1])
    sns.boxplot(data=iris, x='species', y='petal_length', ax=axes[1, 0])
    sns.boxplot(data=iris, x='species', y='petal_width', ax=axes[1, 1])
    fig.suptitle("Iris: Distribution of Measurements by Species")
    plt.tight_layout()
    plt.show()


def main():

    partOne()
    #partTwo()
    #partThree()
    #partFour()


if __name__ == '__main__':
    main()
