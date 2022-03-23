import numpy as np
import pandas as pd
import geopandas as gpd
import json
from matplotlib import pyplot as plt
import geoplot as gplt

"""First...geojson
1. A geometric object (with additional properties) is a Feature.
2. Sets of geometric objects are contained within a FeatureCollection.

geojson format of a Feature is below.

{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}

"""

"""We'll work with several types of geometric objects.

Point: 
The 'coordinates' member is a single position: 
[125.6, 10.1]

LineString: 
The 'coordinates' member is an array of two or more positions:
[[102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]]

Polygon: 
The polygon is defined by the concept of the linear ring, 
which is a closed line string with four or more positions.
The first and last positions must be identical.  Linear rings are used to 
represent surface boundary areas or surface holes. 
[[[16.979667,48.123497], [point, point], [point, point], [16.979667,48.123497]]]

# MultiPolygon: 
The 'coordinates' member is an array of Polygon coordinate arrays.
In other words, a list of Polygons.
[
[[[45.001987,39.740004], [point, point], [point, point],[45.001987,39.740004]]],
[[[47.373315,41.219732], [point, point], [point, point],[47.373315,41.219732]]]
]
"""

"""geopandas represents data using a GeoDataFrame, 
which is just a pandas DataFrame with a special geometry column 
containing a geometric object describing the physical nature of the record in question: 
a POINT in space, a POLYGON, etc."""

"""opening a json file with country-level data
note when reading this to a dict we only have two keys: type and features"""

with open('countries.geo.json') as json_data:
    d1 = json.load(json_data)
    print(d1['type'])
    print(d1['features'][0]['properties']['name'])
    print(d1['features'][0]['geometry']['coordinates'][0])

"""opening a geojson version of the same file...They're identical...
except for the file extension.
geojson is also a file extension but has more to do with the formatting conventions."""

with open('countries.geojson') as json_data:
    d2 = json.load(json_data)
    print(d2['type'])
    print(d2['features'][0]['properties']['name'])
    print(d2['features'][0]['geometry']['coordinates'][0])

"""Let's convert this to a DataFrame and export it to a csv and examine it.
The structure is alright, but not optimal.
"""
countries = pd.DataFrame(d2)
countries.to_csv('countries.csv', index=False)

"""Now we'll read in the same file with geopandas instead of json.load().

This will put our data into a DataFrame-like object instead of a dict,
giving us a better datastructure to work with.
Let's examine the structure.

Note: we can read in either version of this file.
The important part is that they both adhere to geojson formatting."""

countries = gpd.read_file('countries.geojson')
print(countries.columns)
countries.to_csv('countries_gpd.csv', index=False)

# And we'll plot the GeoDataFrame with geopandas
ax = countries.plot(figsize=(15, 9), alpha=0.5, edgecolor='k')
plt.tight_layout()
plt.show()

"""We can use our fig, ax approach as well.
Here I'm going to add an arbitrary column.  This will produce a choropleth."""
np.random.seed(51)
countries['random_measure'] = np.random.rand(len(countries))

fig, ax = plt.subplots(figsize=(15, 9), alpha=0.5, edgecolor='k')
countries.plot(column='random_measure',
               cmap='Greens',
               linewidth=1,
               legend=True,
               ax=ax)
plt.show()

"""Now plotting with geoplot"""

gplt.polyplot(countries, figsize=(15, 8))
plt.tight_layout()
plt.show()

"""Choropleths in geoplot"""


gplt.choropleth(countries,
                   hue=countries['random_measure'],
                   cmap='plasma',
                   figsize=(15, 8))

plt.tight_layout()
plt.show()


"""Keyword arguments that are not part of the geoplot API 
are passed to the underlying matplotlib.patches.Polygon objects; 
this can be used to control plot aesthetics. 
To pass keyword argument to the legend, use the legend_kwargs argument.

Also note that we can layer plots easily in geoplot.
Also note that working with projections in geoplot can be tricky.
"""
# read in states json data...I won't post this json file.
states = gpd.read_file('us-states.json')
states['Some_Feature'] = np.random.rand(len(states))

ax = gplt.polyplot(states,
                   figsize=(15, 9),
                   #projection=gcrs.AlbersEqualArea(),
                   edgecolor='white',
                   facecolor='black',
                   hatch='o')
gplt.choropleth(states,
                hue=states['Some_Feature'],
                cmap='YlOrRd',
                legend=True,
                ax=ax)
