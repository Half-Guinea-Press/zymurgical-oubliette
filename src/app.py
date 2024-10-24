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

app = Dash(external_stylesheets=[dbc.themes.SANDSTONE])
server = app.server

# Get Data

# Content Renderer

@app.callback(Output("page-content","children"),
    [Input("url","pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [dbc.Card([html.H1("Welcome to the Zymurgical Oubliette. Please forgive the dust as we are under construction..."),])]
    elif pathname == "/group_h":
        return [groupH]
    elif pathname == "/group_n":
        return [groupN]
    return dbc.Card([
        html.H1("404: Not found"),
        html.Hr(),
        html.P(f"the pathname {pathname} was not recognized ..."),
        ])

# Content Pages

## Group H

groupH = html.Div(
    [
        dbc.Row(
            [
                dbc.NavbarSimple(
                    children = [],
                    brand = "Group H",
                    color = "primary",
                    dark = "true"
                )
            ]
        ),
        dbc.Row(
            [
                
            ]
        )
    ]
)

## Group N

groupN = html.Div(
    [
        dbc.Row(
            [
                dbc.NavbarSimple(
                    children = [],
                    brand = "Group N",
                    color = "primary",
                    dark = "true"
                )
            ]
        ),
        dbc.Row(
            [
                
            ]
        )
    ]
)

# Main Pages

main_page = html.Div([
    dbc.Row(
        [    
            dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src="", height="30px")),
                                    dbc.Col(dbc.NavbarBrand("Zymurgical Oubliette",className="ms-2")),
                                ],
                                align="center",
                                className="g-0"
                            ),
                            href="/",
                            style={"textDecoration":"none"},
                        ),
                    ]
                ),
                color="dark",
                dark=True,
            ),
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
                    dbc.NavItem(dbc.NavLink("Group H", href="/group_h", active="exact")),
                    dbc.NavItem(dbc.NavLink("Group N", href="/group_n", active="exact")),
                ],
                pills=True,
                fill=True
            )
        ]
    ),    
    dbc.Row([
        dbc.Col(
            html.Div(
                [
                html.Div(id="page-content",children=[],style={"display":"block"}),
                ]
            ),
        ),
        ],
        style=
            {
            "padding":"20px"
            }
        ),
    dcc.Location(id="url")])

# app validation and runner

app.layout = main_page

app.validation_layout = html.Div(
    [
        main_page,
        pc_page,
        character_design_page
    ]
)

if __name__=="__main__":
    app.run_server
    
url = f"https://zymurgical-oubliette.onrender.com/"
                        
