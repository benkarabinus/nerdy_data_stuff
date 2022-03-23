from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.io as pio

import pandas as pd
import numpy as np

measures = {
'frl':	['Fan relations', "Courtesy by players, coaches and front offices toward fans, and how well a team uses technology to reach them"],
'own':	['Ownership', "Honesty; loyalty to core players and the community"],
'pla':	['Players', "Effort on the field, likability off it"],
'fut':	['Future wins', "Projected wins over next 5 seasons"],
'bwg':	['Bandwagon Factor', "Are the team's next 5 years likely to be better than their previous 5?"],
'trd':	['Tradition', "Championships/division titles/wins in team's entire history"],
'bng':	['Bang for the buck', "Wins per fan dollars spent"],
'beh':	['Behavior', "Suspensions by players on team since 2007, with extra weight to transgressions vs. women"],
'nyp':	['Proximity to NYC', "Proximity to New York City"],
'slp':	['Proximity to St. Louis', "Proximity to St. Louis"],
'aff':	['Affordability', "Price of tickets, parking and concessions"],
'smk':	['Small Market', "Size of market in terms of population, where smaller is better"],
'stx':	['Stadium experience', "Quality of venue; fan-friendliness of environment; frequency of game-day promotions"],
'cch':	['Coaching', "Strength of on-field leadership"],
'uni':	['Uniform', "Stylishness of uniform design, according to Uni Watch's Paul Lukas"],
'bmk':	['Big Market', "Size of market in terms of population, where bigger is better"]
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server # allow heroku to recognize server

df = pd.read_csv('data.csv')

md_text = """
# NFL Team Attributes:
## Choose X, Y and sizing variables to update the chart.
"""

app.layout = html.Div([
    html.Div([
        dcc.Markdown(children=md_text, style={'font': '15px Arial, sans-serif', 'color': 'white', 'font-weight': '500'}),

        html.Div([
            html.Label('X-Axis Measure', style={'font': '15px Arial, sans-serif', 'color': 'white', 'font-weight': 'bold'}),
            dcc.Dropdown(options=[dict(label=j[0],value=i) for i,j in measures.items()],
                         value='frl',
                         id='x-selection'
            )
        ], style={'width': '28%', 'padding': '15px', 'display': 'inline-block', 'backgroundColor': 'black'}),

        html.Div([
            html.Label('Y-Axis Measure',
                       style={'font': '15px Arial, sans-serif', 'color': 'white', 'font-weight': 'bold'}),
            dcc.Dropdown(options=[dict(label=j[0], value=i) for i, j in measures.items()],
                         value='own',
                         id='y-selection'
                         )
        ], style={'width': '28%', 'padding': '15px', 'display': 'inline-block', 'backgroundColor': 'black'}),

        html.Div([
            html.Label('Size Factor', style={'font': '15px Arial, sans-serif', 'color': 'white', 'font-weight': 'bold'}),
            dcc.Dropdown(options=[dict(label=j[0], value=i) for i,j in measures.items()],
                         value='pla',
                         id='size-selection'
            )
        ], style={'width': '28%', 'padding': '15px', 'display': 'inline-block', 'backgroundColor': 'black'}),

    ], style={'backgroundColor': 'black'}),

    html.Div([
        html.Div([
            dcc.Graph(id='measure-scatter'),
            ], style={'width': '48%', 'display': 'inline-block', 'backgroundColor': 'black'}),
        html.Div([
            dcc.Graph(id='team-map'),
            ], style={'width': '48%','float': 'right', 'display': 'inline-block', 'backgroundColor': 'black'})
    ])
], style={'backgroundColor': 'black'})

@app.callback(
    Output('measure-scatter', 'figure'),
    Output('team-map', 'figure'),
    Input('x-selection', 'value'),
    Input('y-selection', 'value'),
    Input('size-selection', 'value'))
def update_plots(x_col, y_col, s_col):
    pio.templates.default = "plotly_dark"

    fig = px.scatter(df, x=x_col, y=y_col,
                     size=s_col,
                     color='conference',
                     hover_name='team')
    fig.update_xaxes(title=measures[x_col][1])
    fig.update_yaxes(title=measures[y_col][1])

    fig2 = px.scatter_geo(df, lat='lat', lon='long',
                         color='conference',
                         size=s_col,
                         hover_name='team',
                         scope='usa')

    return fig, fig2

if __name__ == '__main__':
    app.run_server(debug=True)
