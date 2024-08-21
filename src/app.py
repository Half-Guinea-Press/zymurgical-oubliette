import dash
import dash_auth
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, State
from dash_bootstrap_components._components.Container import Container
import plotly.graph_objects as go
import plotly.express as px
import json

app = Dash(__name__)
server = app.server

# Get Data

@app.callback(Output("sidebars","is_open"),
    [Input("sidebar-toggle","n_clicks")],
    [State("sidebars","is_open")],
    )
def toggle_sidebar(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output('page-content','children'),
    [Input('url','pathname')])
def render_page_content(pathname):
    if pathname == '/':
        return [dbc.Card([html.H1("This is a test to see if I figured it out or if I am just an idiot!"),])]
    elif pathname == '/pc':
        return [pc_page]
    elif pathname == '/character_design':
        return [character_design_page]
    return dbc.Card([
        html.H1('404: Not found'),
        html.Hr(),
        html.P(f'the pathname {pathname} was not recognized ...'),
        ])

pc_page = html.Div([])

character_design_page = html.Div([])

main_page = html.Div([
    dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="", height="30px")),
                            dbc.Col(dbc.NavbarBrand("Brand Text")),
                        ],
                        align="center",
                    ),
                    href="/",
                    style={"textDecoration":"none"},
                ),
            ]
        ),
        color="dark",
        dark=True,
    ),
    dbc.Row([
        dbc.Col([
            dbc.Button("<>",id="sidebar-toggle", n_clicks=0, color="primary",className="mb-3"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavLink("Home", href="/", active="exact"),
                        dbc.NavLink("PC", href="/pc", active="exact"),
                        dbc.NavLink("Character Design", href="/character_design", active="exact")
                    ],
                    vertical=True,
                    pills=True,
                ),
                id="sidebars",
                is_open=True,
                dimension="width",
                style={
                    "position":"fixed",
                    "top":100,
                    "left":0,
                    "bottom":0,
                    "width":"inherit",
                    "padding":"1rem 1rem",
                    "backgroundColor": "#f8f9fa",
                    },
                ),
            ],
            width=2,
        ),
        dbc.Col(
            html.Div([
                html.Div(id="dd-output-container", style={'paddingTop':'10px'}),
                html.Div(id='page-content',children=[],style={'display':'block'}),
            ]),width=9),
        ],style={'paddingTop':'10px'}),
    dcc.Location(id='url')])

app.layout = main_page

app.validation_layout = html.Div(
    [
        main_page,
        pc_page,
        character_design_page
    ]
)

if __name__=='__main__':
    app.run_server
    
url = f'https://zymurgical-oubliette.onrender.com/'
                        
