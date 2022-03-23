import seaborn as sns
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

toy = sns.load_dataset("mpg")
print(toy.head())

fig = px.area(toy, x='mpg', y='horsepower',
              color='origin', line_group='origin')
fig.show()