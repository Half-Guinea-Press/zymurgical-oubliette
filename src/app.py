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

## SubContent Pages

characterSheet = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("Player Name"),
                        html.Br()
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.H3("Class/Level")),
                                dbc.Col(html.H3("Player Name"))
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(html.H3("Species")),
                                dbc.Col(html.H3("Background")),
                                dbc.Col(html.H3("Experience")),
                            ]
                        )
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Col(
                            [
                                dbc.Card([dbc.CardHeader("Strength"),dbc.CardBody([html.H5("18")]),dbc.CardFooter([html.P("+4")]),]),
                                dbc.Card([dbc.CardHeader("Dexterity"),dbc.CardBody([html.H5("18")]),dbc.CardFooter([html.P("+4")]),]),
                                dbc.Card([dbc.CardHeader("Constitution"),dbc.CardBody([html.H5("18")]),dbc.CardFooter([html.P("+4")]),]),
                                dbc.Card([dbc.CardHeader("Inteligence"),dbc.CardBody([html.H5("18")]),dbc.CardFooter([html.P("+4")]),]),
                                dbc.Card([dbc.CardHeader("Wisdom"),dbc.CardBody([html.H5("18")]),dbc.CardFooter([html.P("+4")]),]),
                                dbc.Card([dbc.CardHeader("Charisma"),dbc.CardBody([html.H5("18")]),dbc.CardFooter([html.P("+4")]),]),
                            ]
                        ),
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardHeader("Saving Throws"),
                                        dbc.CardBody(
                                            [
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Strength")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Dexterity")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Constitution")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Inteligence")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Wisdom")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Charisma")]),
                                            ]
                                        )
                                    ]
                                ),
                                dbc.Card(
                                    [
                                        dbc.CardHeader("Skill Proficiencies"),
                                        dbc.CardBody(
                                            [
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Acrobatics")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Animal Handling")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Arcana")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Athletics")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Deception")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("History")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Insight")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Investigation")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Medicine")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Nature")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Perception")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Performance")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Religion")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Sleight of Hand")]),
                                                dbc.Row([html.P("+1"),html.P(" "),html.P("Stealth")]),
                                                bc.Row([html.P("+1"),html.P(" "),html.P("Survival")]),
                                            ]
                                        )
                                    ]
                                ),
                                
                            ]
                        )
                    ]
                ),
                dbc.Col(
                    [
                        
                    ]
                ),
                dbc.Col(
                    [
                        
                    ]
                ),
            ]
        )
    ]
)

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
                dbc.Tabs(
                    [
                        dbc.Tab(
                            children = [],
                            label = "Player Characters",
                            id = "pcTab"
                        ),
                        dbc.Tab(
                            children = [],
                            label = "",
                            id = "Tab"
                        ),
                    ]
                )
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
        groupH,
        groupN
    ]
)

if __name__=="__main__":
    app.run_server
    
url = f"https://zymurgical-oubliette.onrender.com/"
                        
