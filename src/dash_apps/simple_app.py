# host/dash_apps/simple_app.py
# or
# middleware/dash_apps/simple_app.py

from dash import dcc, html, Dash
from flask import g
def init_app(url_path):

    # If initializing Dash app using Flask app as host
    app = Dash(server=g.cur_app, url_base_pathname=url_path)

    # End if
    
    # If initializing Dash app for middleware
    #app = Dash(requests_pathname_prefix=url_path)

    # End if

    app.layout = html.Div(children=[
        html.A(id="logout-link", children="Main page", href="/"),
        html.H1("Welcome to my Dash App", style={"textAlign": "center"}),
        html.Div(id="dummy"),
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Category 1'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Category 2'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        ),

    ])

    return app.server

