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

@app.callback(Output("sidebar-left","is_open"),
    [Input("sidebar-left-toggle","n_clicks")],
    [State("sidebar-left","is_open")],
    )
def toggle_sidebar(n, is_open):
    if n:
        return not is_open
    return is_open
    
@app.callback(Output("sidebar-right","is_open"),
    [Input("sidebar-right-toggle","n_clicks")],
    [State("sidebar-right","is_open")],
    )
def toggle_sidebar2(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output("page-content","children"),
    [Input("url","pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [dbc.Card([html.H1("This is a test to see if I figured it out or if I am just an idiot!"),])]
    elif pathname == "/pc":
        return [pc_page]
    elif pathname == "/character_design":
        return [character_design_page]
    return dbc.Card([
        html.H1("404: Not found"),
        html.Hr(),
        html.P(f"the pathname {pathname} was not recognized ..."),
        ])

pc_page = html.Div(
    [
    dbc.Row(dbc.Col(html.H1("Valrdis Fossic"))),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(html.Img(src="assets/Valdris%20Fossic%20head.jpg")),
                        html.Div("Blood Hunter Lvl 2 (LN)"),
                    ]
                ),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
    ]
)

character_design_page = html.Div(
    [
        dbc.Row(
            dbc.Col((html.H1"Character Builder"),),
        ),
        dbc.Row(
            [
                dbc.InputGroup([dbc.Input(id="characterName",placeholder="Character Name",),],className="mb-3",),
                dbc.InputGroup([dbc.Input(id="playerName",placeholder="Player Name",),],className="mb-3",),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Character Level"),
                        dbc.Input(id="characterLvl",type="number", min=0, max=20, step=1,className="mb-3",),
                    ]
                ),
                dbc.InputGroup(
                    [
                        dbc.DropdownMenu(
                            id="race",
                            label="Character Race",
                            children=[
                                dbc.DropdownMenuItem("Dhampir",id="dhampir"),
                                dbc.DropdownMenuItem("Fettered"id="fettered"),
                                dbc.DropdownMenuItem("Gargoyle"id="gargoyle"),
                                dbc.DropdownMenuItem("Living Vampire"id="livingVampire"),
                            ],
                            className="mb-3",
                        ),
                    ]
                ),
                dbc.InputGroup(
                    [
                        dbc.DropdownMenu(
                            id="startingClass",
                            label="Character Class",
                            children=[
                                dbc.DropdownMenuItem("Artificer"id="artificer"),
                                dbc.DropdownMenuItem("Alchemist"id="alchemist"),
                                dbc.DropdownMenuItem("Bard"id="bard"),
                                dbc.DropdownMenuItem("Blood Hunter"id="bloodHunter"),
                                dbc.DropdownMenuItem("Monk"id="monk"),
                            ],
                            className="mb-3",
                        ),
                    ],
                ),
            ],
        ),
        dbc.Row([]),
    ],
)

main_page = html.Div([
    dbc.Row([    
        dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src="", height="30px")),
                                dbc.Col(dbc.NavbarBrand("The Nocturnal Campaign",className="ms-2")),
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
    ]),    
    dbc.Row([
        dbc.Col([
            dbc.Button("<>",id="sidebar-left-toggle", n_clicks=0, color="primary",className="mb-3"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
                        dbc.NavItem(dbc.NavLink("PC", href="/pc", active="exact")),
                        dbc.NavItem(dbc.NavLink("Character Design", href="/character_design", active="exact")),
                    ],
                    vertical=True,
                    pills=True,
                ),
                id="sidebar-left",
                is_open=True,
                dimension="width",
                ),
            ],
            width=2,
        ),
        dbc.Col(
            html.Div(
                [
                html.Div(id="dd-output-container", style={"paddingTop":"10px"}),
                html.Div(id="page-content",children=[],style={"display":"block"}),
                ]
            ),
            width=7
        ),
        dbc.Col([
            dbc.Button("<>",id="sidebar-right-toggle", n_clicks=0, color="primary",className="mb-3"),
            dbc.Collapse(
                dbc.Card("This is the right card!", body=True),
                id="sidebar-right",
                is_open=True,
                dimension="width",
                ),
            ],
            width=2,
        ),
        ],
        style=
            {
            "paddingTop":"10px"
            }
        ),
    dcc.Location(id="url")])

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
                        
