# host/dash_apps/population.py
# or
# middleware/dash_apps/population.py

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import ssl
from flask import g

ssl._create_default_https_context = ssl._create_unverified_context

def init_app(url_path, server=None):
    global df

    # If initializing Dash app using Flask app as host
    app = Dash(server=g.cur_app, url_base_pathname=url_path)

    # End if
    
    # If initializing Dash app for middleware
    #app = Dash(requests_pathname_prefix=url_path)

    # End if

    # Access the variables defined in the main Flask instance using g object.
    df = g.df

    app.title = "Population by country - Ploomber Cloud Dash Application"

    app.layout = html.Div(
        [
            html.A(id="logout-link", children="Main page", href="/"),
            html.H1(children="Population by country", style={"textAlign": "center"}),
            dcc.Dropdown(df.country.unique(), "Canada", id="dropdown-selection"),
            dcc.Graph(id="graph-content"),
        ]
    )

    init_callbacks(app)
    return app.server


def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x="year", y="pop")

def init_callbacks(app):
    app.callback(
        Output("graph-content", "figure"), 
        Input("dropdown-selection", "value")
    )(update_graph)

