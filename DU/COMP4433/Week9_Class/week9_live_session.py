import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

"""This week we'll focus on plotly.

We'll focus on building base charts with express and
becoming comfortable with the dictionary representation of these objects
so that we can modify them.

For week 10 we'll do a deeper dive into Dash"""

"""Both express and graph_objects allow you to build
plotly.graph_objects.Figure objects.  Express offers functions 
to build fully populated Figure objects easily.
Figures build with express still use plotly.graph_objects.Figure instances
under the hood, so it's recommended to start with express and modify from
there."""

"""Plotly charts are represented as JSON objects, which is essential in
allowing them to be accessed by different programming languages."""

"""graph_objects is the low-level interface to figures, traces and layout."""

"""The subplots (make_subplots) module contains helper functions for layouts
of multi-plot figures"""

"""Figure factory (plotly.figure_factory) module offers special figures that
are difficult to achieve otherwise."""

# printing a figure will show the underlying data structure of
# a plotly.graph_objects.Figure object.
fig = px.line(x=['a', 'b', 'c'], y=[1, 3, 2],
              title='sample figure',
              height=525)
fig.show()

# note that layout.template is often omitted.
print(fig)
print(type(fig))
fig_dict = fig.to_dict()
print(fig_dict)
fig_json = fig.to_json()
print(fig_json)
print(type(fig_json))

# Manipulating figure attributes
# using object attributes or update methods
fig.layout.title = 'Example Figure'
fig.update_layout(title='Example Sample')
fig.show()

# note: unspecified figure attributes will be set by default

"""Figures are represented as trees with named nodes called attributes.
A figure has three top-level attributes.  Data and Layout
are always part of a Figure.  Frames is dependant on chart type.

1. Data
2. Layout
3. Frames
"""

"""1. Data: Value must be a list of dicts which are called traces.
Traces consist of a collection of data and a type.

Each trace has one of 40+ types (e.g., scatter, bar, histogram, etc.)
The type of a trace determines its allowable attributes.
"""
print(fig)

"""2. Layout: Value must be a dict. Contains attributes that control positioning 
and configuration of non-data related figure components.  
Layout options are applied to the figure as a whole. For example, 
margins, subplots, title, legend shapes, images, sliders, dropdowns, annotations, etc."""

""""3. Frames: Value must be a list of dicts that define sequential frames
in an animated plot. Each frame contains its own data attribute as well as other parameters.
Animations are controlled/triggered by controls defined in layout.sliders and/or
layout.updatemenus"""

gpm = px.data.gapminder()
fig2 = px.choropleth(gpm, locations='iso_alpha', color='lifeExp',
                    hover_name='country', animation_frame='year',
                    range_color=[20, 80])
fig2 = px.choropleth(gpm, locations='iso_alpha', color='lifeExp',
                    hover_name='country', animation_frame='year')

print(fig2)
fig2.show()

# choropleth with JSON
import json
from urllib.request import urlopen

# Let's load to geojson files and examine the differences
with urlopen('https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json') as resp:
    states = json.load(resp)

with urlopen('https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json') as resp:
    states2 = json.load(resp)

"""Choropleths in express

geometry information for px.choropleth can be supplied from geojson 
where each feature has either an id field or some identifying value in properties OR
you can use a built-in plotly geometry like US states or world countries.
You also need a list of values indexed by feature identifier.  
If you're geojson data doesn't have an appropriate id field and you want
to use a property then you'll need to specify the featureidkey argument.
"""

for i in states['features']:
    print(i['id'])
for i in states2['features']:
    print(i['id'])

df = pd.read_csv('https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/US_Unemployment_Oct2012.csv')

fig3 = px.choropleth(df, geojson=states2, locations='State',
                    color='Unemployment', color_continuous_scale='Viridis',
                    scope='usa',
                    labels={'Unemployment': 'Unemployment Rate'})
fig3.show()

"""If you're geojson data doesn't have an appropriate id field and you want
to use a property then you'll need to specify the featureidkey argument.

Let's use the original State geojson file with no meaningful ID.
We'll access the key (state name) which is the name property of the geojson"""

fig3b = px.choropleth(df, geojson=states, locations='State',
                     featureidkey='properties.name',
                    color='Unemployment', color_continuous_scale='Viridis',
                    scope='usa',
                    labels={'Unemployment': 'Unemployment Rate'})
fig3b.show()

# We need the keys to match.
st_codes = pd.read_csv('https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv')
df = df.merge(st_codes, how='left', left_on='State', right_on='Abbreviation')
df.drop(columns=['State_x', 'Abbreviation'], inplace=True)
df.rename(columns={'State_y': 'State'}, inplace=True)

# This should get us there.
fig3c = px.choropleth(df, geojson=states, locations='State',
                     featureidkey='properties.name',
                    color='Unemployment', color_continuous_scale='Viridis',
                    scope='usa',
                    labels={'Unemployment': 'Unemployment Rate'})
fig3c.show()

# Of course a more direct route is as follows. No need for geojson parameter.
# but locationmode needs to be set.
fig3d = px.choropleth(df, locations='State', locationmode='USA-states',
                    color='Unemployment', color_continuous_scale='Viridis',
                    scope='usa',
                    labels={'Unemployment': 'Unemployment Rate'},
                    title='US Unemployment Rates')
fig3d.show()

# basic express plots: https://plotly.com/python/basic-charts/
# scatter with express

fig4 = px.scatter(x=gpm['lifeExp'], y=gpm['pop'])
fig4.show()

"""setting size for bubble charts...all parameters are added to tooltip.
additional attributes can be added with hover_data argument.
passing a dict to hover_data will allow you to exclude tooltip features.
using discrete color"""

fig5 = px.scatter(gpm, x='lifeExp', y='pop', color='continent',
                  size='gdpPercap', hover_data=['country'])
fig5.show()

# setting size and continuous color with symbol specified
fig5 = px.scatter(gpm, x='lifeExp', y='pop', color='lifeExp',
                  size='gdpPercap', symbol='continent', hover_data=['country'])
fig5.show()

# faceting
fig6 = px.scatter(gpm, x='lifeExp', y='gdpPercap', color='lifeExp',
                  size='pop', facet_row='continent')

# let's assess the figure tree
print(fig6)

fig6.show()

# now we'll truncate the range of the y axis by setting it explicitly
# also ordering categories of facet dimension
fig6b = px.scatter(gpm, x='lifeExp', y='gdpPercap', color='lifeExp',
                   size='pop', facet_row='year',
                   category_orders={'year': [2007, 2002, 1997, 1992, 1987, 1982, 1977, 1972, 1967, 1962, 1957, 1952]},
                   range_y=[-1000, 40000],
                   title='Life Expectancy x PerCap GDP')
fig6b.show()
# assess figure tree again
print(fig6b)

# 3D Scatter
fig7 = px.scatter_3d(gpm, x='lifeExp', y='pop', z='gdpPercap',
                     color='continent')
fig7.show()

# line
fig8 = px.line(gpm, x='year', y='lifeExp',
              color='continent', hover_name='country',
              line_shape='spline', render_mode='svg')
fig8.show()

fig8b = px.line(gpm, x='year', y='lifeExp',
              color='continent', hover_name='country',
              line_group='country',
              line_shape='spline', render_mode='svg')
fig8b.show()

# area

fig9 = px.area(gpm, x='year', y='pop',
              color='continent', line_group='country')
fig9.show()

# styling figures.  express figures can be styled using
# precisely the same appraoches as for graph_objects.

""" Style achieved in four ways:
1. Built in express styling args (set in px plotting function call)
-title
-width and height (figure dimensions)
-template
-labels (default uses dataframe col or label name (x, y, color)
(labels takes a dict..keys are labels to rename and values are desired labels)
(these appear in axis labels, legend and color bar titles and hover labels)
-category_orders (default is order of appearance)
(accepts dict. keys are column name and values are a list of values in desired order)
-hover_data (which attributes appear)
-hover_name (how they are formatted)
"""

fig_bar = px.bar(gpm, x='year', y='pop', color='continent')
fig_bar.show()

fig_bar2 = px.bar(gpm, x='year', y='pop', color='continent',
                  title='Global Population: 1952-2007',
                  width=1200, height=900,
                  labels={'pop': 'Population', 'year': 'Year', 'continent': 'Continent'},
                  category_orders={'year': [2007, 2002, 1997, 1992, 1987, 1982, 1977, 1972, 1967, 1962, 1957, 1952]},
                  color_discrete_map={'Europe': '#55e07d'},
                  template='plotly_dark')
fig_bar2.show()

"""updating or modifying figures made with express.

Some features can't be controlled with px plotting function parameters.
update and add methods on the plotly.graph_objects.Figure object.

Below we're also demonstrating a styling approach which is specifying the template
in the px function call.
"""

fig_bar3 = px.bar(gpm, x='year', y='pop', color='continent',
                  title='Global Population: 1952-2007',
                  width=1200, height=900,
                  labels={'pop': 'Population', 'year': 'Year', 'continent': 'Continent'},
                  category_orders={'year': [2007, 2002, 1997, 1992, 1987, 1982, 1977, 1972, 1967, 1962, 1957, 1952]},
                  color_discrete_map={'Europe': '#55e07d'},
                  template='plotly_dark')
fig_bar3.update_layout(font_family='Old Standard TT"')
fig_bar3.show()


"""Setting express styling defaults."""
pio.templates.default = "simple_white"

px.defaults.template = "ggplot2"
px.defaults.color_continuous_scale = px.colors.sequential.Blackbody
px.defaults.width = 600
px.defaults.height = 400


""" animation """
fig = px.bar(gpm, x='continent', y='pop', color='continent',
             animation_frame='year')
fig.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='Crimson', size=14))
fig.show()

# controlling y-axis range
fig = px.bar(gpm, x='continent', y='pop', color='continent',
             animation_frame='year')
fig.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='Crimson', size=14))
fig.update_yaxes(range=[0, 4000000000])
fig.show()


