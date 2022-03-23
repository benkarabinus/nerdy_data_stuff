"""Week 5 Live Session
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""figure-level vs axes-level functions

It's useful to review the documentation on this concept.
This will help you fully incorporate seaborn plotting
with matplotlib object-oriented approaches.
"""

diamonds = sns.load_dataset('diamonds')

# histplot() is axes-level
sns.histplot(data=diamonds, x='price', hue='cut', multiple='stack')

# displot() is fig-level
sns.displot(data=diamonds, x='price', hue='cut', multiple='stack', kind='hist')

# Below we use the figure-level method and facet the plots by cut
sns.displot(data=diamonds, x='price', hue='cut', kind='hist', col='cut')

"""Axes-level plots can be used to build complex matplotlib plots
using an object-oriented approach.
Figure-level plotting functions can't be used to draw on subplot axes."""

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
sns.histplot(data=diamonds, x='price', hue='cut', multiple='stack', ax=axes[0])
sns.kdeplot(data=diamonds, x='price', hue='cut', multiple='stack', ax=axes[1])
plt.tight_layout()

"""More on integrating fig, ax object-oriented pyplot approach with sns.
Specify ax argument in call to axes-level sns plotting functions.

Don't forget about the shape of the ndarray axes objects.
"""
mpg = sns.load_dataset('mpg')

sns.set()
sns.set_style('darkgrid')

fig = plt.figure(figsize=(12, 9))

gs = fig.add_gridspec(3, 4)
ax0 = plt.subplot(gs[:2, :2])
ax1 = plt.subplot(gs[2:, :2])
ax2 = plt.subplot(gs[:4, 2:])

sns.scatterplot(data=mpg, x='acceleration',
                y='mpg', hue='cylinders',
                ax=ax0)

sns.histplot(data=mpg, x='mpg', bins=20,
             ax=ax1)

sns.boxplot(data=mpg, x='model_year', y='mpg',
            ax=ax2)
ax2.set_xlabel('model year')

fig.suptitle('Automobile Data (1970-1982)', fontsize=18)
plt.tight_layout()

"""Multi-Classifier Consensus Density Plot

I made this name up, but the plot itself is occasionally useful.
Especially if you're trying to assess differential classification,
identify hard-to-classify cases or determine voting in an ensemble model.

A similar technique is employed in the week 6 asynch for missingness."""

# some random data meant to simulate the application of some different classifiers
np.random.seed(57)
pid = np.linspace(8000, 9001, 1000).astype(str)
outcome = np.random.randint(0, 2, 1000)
classifier_1 = np.round((outcome + 0.5) * np.random.rand(1000)).astype(int)
classifier_2 = np.round((outcome + 0.4) * np.random.rand(1000)).astype(int)
classifier_3 = np.round((outcome + 0.3) * np.random.rand(1000)).astype(int)

# building a dataframe
df = pd.DataFrame(list(zip(pid, outcome, classifier_1, classifier_2, classifier_3)),
                  columns=['id', 'outcome', 'c_1', 'c_2', 'c_3'])

# we could use a boolean mask here, but I'm creating new columns to assess classifications
for i, j in zip(['c_1', 'c_2', 'c_3'], ['c_1_bool', 'c_2_bool', 'c_3_bool']):
    df[j] = np.vectorize(lambda x, y: True if x == y else False)(df[i], df['outcome'])

# Bool value heatmap...classification results unsorted.
sns.heatmap(df[['c_1_bool', 'c_2_bool', 'c_3_bool']], cbar=True, cmap='vlag')
plt.tight_layout()
plt.show()

# the above plot is hard to make sense of. Let's assess which classifier is most accurate.
df[['c_1_bool', 'c_2_bool', 'c_3_bool']].describe()

# Sorted by best performing classifier
df.sort_values(by=['c_1_bool'], ascending=False, inplace=True)

sns.heatmap(df[['c_1_bool', 'c_2_bool', 'c_3_bool']], cbar=True,
            cmap=sns.diverging_palette(185, 45, as_cmap=True))
plt.tight_layout()
plt.show()

# Hierarchically sorted
df.sort_values(by=['c_1_bool', 'c_2_bool', 'c_3_bool'],
               ascending=[False, False, False],
               inplace=True)

sns.heatmap(df[['c_1_bool', 'c_2_bool', 'c_3_bool']], cbar=True,
            cmap=sns.diverging_palette(185, 45, as_cmap=True))
plt.tight_layout()
plt.show()

""" Facet Grids

Note that we can facet figure-level plots by specifying column and row args.
Also note that we can essentially replicate any axes-level plot from the figure-level
method by specifying the kind argument."""

# basic figure-level relational plot
sns.relplot(data=mpg, x='mpg', y='horsepower', col='origin')
# specifying kind for relplot()
sns.relplot(data=mpg, x='mpg', y='horsepower', col='origin', kind='line')

sns.catplot(data=mpg, x='model_year', y='mpg', col='origin')
sns.catplot(data=mpg, x='model_year', y='mpg', row='origin', kind='violin')

# Specifying a FacetGrid
sns.set_style('whitegrid')

# note the availability of the methods FacetGrid.map()
# and FacetGrid.map_dataframe() for applying plotting functions.

g = sns.FacetGrid(diamonds, col='cut', row='color')
# mapping an axes-level plotting method
g.map(sns.histplot, 'price')
sns.despine(left=True, bottom=True)

g2 = sns.FacetGrid(mpg, col='origin')
g2.map_dataframe(sns.scatterplot, x='mpg', y='acceleration', hue='model_year')

g3 = sns.FacetGrid(mpg, col='origin')
g3.map_dataframe(sns.regplot, 'mpg', 'acceleration')

# note that lmplot is figure-level while regplot is axes-level
# lmplot combines facetgrids with elements of regplot()
g4 = sns.lmplot(data=mpg, x='mpg', y='acceleration', col='origin', hue='origin')

g5 = sns.lmplot(data=mpg, x='mpg', y='acceleration', hue='origin')

g6 = sns.lmplot(data=mpg, x='mpg', y='weight', hue='origin')

"""pairplots

These were tricky for us to achieve in matplotlib but easy with seaborn.
These will detect and operate only on numeric columns.
"""

sns.pairplot(mpg)

# gridspec_kw...a subplots() parameter.
widths = [2, 3, 1.5]
heights = [1, 3, 2]

gs_kw = dict(width_ratios=widths, height_ratios=heights)
fig, axes = plt.subplots(ncols=3, nrows=3, constrained_layout=True,
                         gridspec_kw=gs_kw)
for r, row in enumerate(axes):
    for c, ax in enumerate(row):
        label = 'Width: {}\nHeight: {}'.format(widths[c], heights[r])
        ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')
