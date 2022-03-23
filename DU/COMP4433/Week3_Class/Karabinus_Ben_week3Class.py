import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    diamonds = pd.read_csv('/Users/benkarabinus/Documents/Git/nerdy_data_stuff/DU/COMP4433/diamonds.csv')
    #print(diamonds)
    partOne(diamonds)

def partOne(diamonds):

    fig, ax = plt.subplots(3, 3, figsize=(14, 8))
    ax[0][0].scatter(diamonds['depth'], diamonds['price'])
    ax[0][0].set_title('IDE (User Adoption)')
    #ax[0].set_xlabel('User Adoption')
    #ax[0].set_ylabel('Platform')
    #plt.xticks(range(len(ide)), ide['IDE'], rotation=65)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()