import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib
from matplotlib import gridspec

"""Remember figure-level and axes-level plots

Top-level fig-level plots accept kind argument and are facetable from the function call

Axes-level plots are easily incorporated into subplotting spaces and take an
optional ax argument to specify the axis they should be written to."""

"""More on Gridspec and customizing figure layouts.

Subplots is probably the most common approach for specifying multiple axes,
but as we've seen there are options that provide greater flexibility.
Gridspec allows us to set the geometry in terms of #rows and #cols."""

# a basic 2x2 subplot space
fig1, axes1 = plt.subplots(2, 2, figsize=(9, 6))

"""The above is more cumbersome to achieve with gridspec,
but notice the flexibility in terms of achieving differential axes sizing.

Note: constrained layout is similar to tight_layout() but needs
to be implemented before axes are added to a figure."""

fig2 = plt.figure(constrained_layout=True)
gs = gridspec.GridSpec(2, 2, figure=fig2)
ax2_1 = fig2.add_subplot(gs[0, 0])
ax2_2 = fig2.add_subplot(gs[0, 1])
ax2_3 = fig2.add_subplot(gs[1, 0])
ax2_4 = fig2.add_subplot(gs[1, 1])

# we can easily achieve something more nuanced
fig3 = plt.figure(constrained_layout=True)
gs = gridspec.GridSpec(3, 3, figure=fig3)
ax3_1 = fig3.add_subplot(gs[0, :])
ax3_2 = fig3.add_subplot(gs[1, :2])
ax3_3 = fig3.add_subplot(gs[1, 2:])
ax3_4 = fig3.add_subplot(gs[2:, :1])
ax3_5 = fig3.add_subplot(gs[2:, 1:])

"""note that .add_gridspec() is a convenience
method to accomplish the above. This can save you an import."""

fig4 = plt.figure(constrained_layout=True)
gs = fig4.add_gridspec(3, 3)
ax4_1 = fig4.add_subplot(gs[0, :])
ax4_1.set_title('gs[0, :]')
ax4_2 = fig4.add_subplot(gs[1, :2])
ax4_2.set_title('gs[1, :2]')
ax4_3 = fig4.add_subplot(gs[1, 2:])
ax4_3.set_title('gs[1, 2:]')
ax4_4 = fig4.add_subplot(gs[2:, :1])
ax4_4.set_title('gs[2:, :1]')
ax4_5 = fig4.add_subplot(gs[2:, 1:])
ax4_5.set_title('gs[2:, 1:]')

"""Now we'll specify some width and height ratios.

We did this in Week5, but we'll go over it in a bit more detail.
First we create a figure."""
fig5 = plt.figure(constrained_layout=True)

"""Note the absolute values don't matter here...

We're only concerned with the ratios.
[2, 3, 1.5] is equiv to [4, 6, 3]"""
widths = [2, 3, 1.5]
heights = [1, 3, 2]

# initializing the gridspec geometry
gs5 = fig5.add_gridspec(nrows=3, ncols=3, width_ratios=widths,
                        height_ratios=heights)

"""We have our gridspec. Now we're just assigning
gridspec components to axes and annotating for clarity."""

for row in range(3):
    for col in range(3):
        ax = fig5.add_subplot(gs5[row, col])
        label = 'Width: {}\nHeight: {}'.format(widths[col], heights[row])
        ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')

"""Now we use the gridspec_kw parameter with subplots.

Note, we're passing the width and height params (as a dict) to gridspec_kw
as part of our call to subplots() instead of passing them to
add_gridspec() or gridspec.GridSpec()"""

widths = [2, 3, 1.5]
heights = [1, 3, 2]

gs_kw = dict(width_ratios=widths, height_ratios=heights)

fig, axes = plt.subplots(ncols=3, nrows=3, constrained_layout=True,
                         gridspec_kw=gs_kw)

"""Since we're passing gridspec params through subplots
we already have our axes specified, so we'll iterate a bit differently than above."""

for r, row in enumerate(axes):
    for c, ax in enumerate(row):
        label = 'Width: {}\nHeight: {}'.format(widths[c], heights[r])
        ax.annotate(label, (0.1, 0.5), xycoords='axes fraction', va='center')

"""Seaborn styles"""

# just a simple plot.  Notice I'm truncating the bin range to avoid the outliers
diamonds = sns.load_dataset('diamonds')

fig, ax = plt.subplots(figsize=(9, 6))
sns.histplot(diamonds['carat'], ax=ax, binrange=(0, 3), color='black')

# switches to sns defaults
sns.set_theme()

fig, ax = plt.subplots(figsize=(9, 6))
sns.histplot(diamonds['carat'], ax=ax, binrange=(0, 3), color='black')

# Restores all RC params to original settings
sns.reset_orig()

"""Seaborn categorizes matplotlib parameters into two separate groups:

1. The first group sets aesthetic style of plots.
    -Styles here are controlled by the functions axes_style() and set_style()

2. The second group scales elements of plots so they can be utilized in different contexts.
    -Scaling is accomplished using plotting_context() and set_context()

The first of each set of pairs returns a dict of parameters.
The second sets the matplotlib defaults."""

# Aesthetic Functions

# see the current parameter values
sns.axes_style()

# There are five preset seaborn themes
themes = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
for i in themes:
    sns.set_style(i)
    fig, ax = plt.subplots(figsize=(9, 6), num=i)
    sns.histplot(diamonds['carat'], ax=ax, binrange=(0, 3))

# we can also use set_style() to tune the parameters specifically
sns.reset_orig()

sns.axes_style()

sns.set_style({'axes.facecolor': '#cae0e0',
               'axes.spines.left': False,
               'grid.linestyle': ':',
               'axes.grid': True,
               'font.family': 'serif'})

sns.axes_style()

fig, ax = plt.subplots(figsize=(9, 6), num=i)
sns.histplot(diamonds['carat'], ax=ax, binrange=(0, 3))

# sns.reset_orig()

# Scaling Functions

sns.plotting_context()

sns.set_context({'font.size': 14.0,
                 'grid.linewidth': 1.2})

fig, ax = plt.subplots(figsize=(9, 6), num=i)
sns.histplot(diamonds['carat'], ax=ax, binrange=(0, 3))

matplotlib.rc_file_defaults()

""" Matplotlib style sheets

Matplotlib also has a number of great style sheets that can 
tune your rc_params (runtime configuration prameters)"""

# to see the available style sheets
plt.style.available

"""Note, plt.style.use() will also allow you to invoke a style,
but it will apply it to your entire session."""

with plt.style.context('fivethirtyeight'):
    fig, ax = plt.subplots(figsize=(9, 6), num=i)
    sns.histplot(diamonds['carat'], ax=ax, binrange=(0, 3))

with plt.style.context('bmh'):
    fig, ax = plt.subplots(figsize=(9, 6), num=i)
    sns.histplot(diamonds['carat'], ax=ax, binrange=(0, 3))

with plt.style.context('ggplot'):
    fig, ax = plt.subplots(figsize=(9, 6), num=i)
    sns.histplot(diamonds['carat'], ax=ax, binrange=(0, 3))

with plt.style.context('dark_background'):
    fig, ax = plt.subplots(figsize=(9, 6), num=i)
    sns.histplot(diamonds['carat'], ax=ax, binrange=(0, 3))