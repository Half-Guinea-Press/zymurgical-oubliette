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
            dbc.Col(html.H1("Character Builder"),),
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupText("Character Name"),
                                        dbc.Input(id="characterName")                                        
                                    ],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupText("Player Name"),
                                        dbc.Input(id="playerName"),
                                    ],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [
                                        dbc.InputGroupText("Character Level"),
                                        dbc.Input(id="characterLvl",type="number", min=0, max=20, step=1),
                                    ],
                                    className="mb-3",
                                ),
                            ]
                        ),
                        dbc.Row(html.Hr()),
                        dbc.Row(
                            [
                                html.Div(
                                    dcc.Dropdown(
                                        [
                                            "Aarakocra",
                                            "Aasimar (Fallen)",
                                            "Aasimar (Protector)",
                                            "Aasimar (Scourge)",
                                            "Aasimar",
                                            "Autognome",
                                            "Bugbear",
                                            "Bullywug",
                                            "Centaur",
                                            "Deep Gnome",
                                            "Dhampir",
                                            "Dhampir",
                                            "Dragonborn (Base)",
                                            "Dragonborn (Chromatic)",
                                            "Dragonborn (Gem)",
                                            "Dragonborn (Metallic)",
                                            "Dragonborn",
                                            "Duergar",
                                            "Dwarf (Duergar)",
                                            "Dwarf (Hill)",
                                            "Dwarf",
                                            "Eladrin",
                                            "Elf (Drow)",
                                            "Elf (Eladrin)",
                                            "Elf (High)",
                                            "Elf (Sea)",
                                            "Elf (Wood)",
                                            "Elf",
                                            "Fettered",
                                            "Firbolg",
                                            "Gargoyle",
                                            "Genasi (Earth)",
                                            "Genasi (Fire)",
                                            "Genasi (Water)",
                                            "Genasi",
                                            "Giff",
                                            "Gith (Githyanki)",
                                            "Gith",
                                            "Githyanki",
                                            "Gnoll",
                                            "Gnome (Deep)",
                                            "Gnome (Deep/Svirfneblin)",
                                            "Gnome (Forest)",
                                            "Gnome (Rock)",
                                            "Gnome",
                                            "Goblin",
                                            "Goliath",
                                            "Grimlock",
                                            "Hadozee",
                                            "Half-Elf (Base)",
                                            "Half-Elf (Variant; Aquatic Elf Descent)",
                                            "Half-Elf (Variant; Drow Descent)",
                                            "Half-Elf (Variant; Moon Elf or Sun Elf Descent)",
                                            "Half-Elf (Variant; Wood Elf Descent)",
                                            "Half-Elf",
                                            "Half-Orc (Base)",
                                            "Half-Orc",
                                            "Halfling (Lightfoot)",
                                            "Halfling (Stout)",
                                            "Halfling",
                                            "Harengon",
                                            "Hexblood",
                                            "Hobgoblin",
                                            "Human (Base)",
                                            "Human (Variant)",
                                            "Human",
                                            "Kalashtar",
                                            "Kender",
                                            "Kenku",
                                            "Kobold",
                                            "Kuo-Toa",
                                            "Leonin",
                                            "Living Vampire",
                                            "Lizardfolk",
                                            "Loxodon",
                                            "MTF",
                                            "Merfolk",
                                            "Minotaur",
                                            "Orc",
                                            "Owlin",
                                            "Plasmoid",
                                            "Reborn",
                                            "Satyr",
                                            "Sea Elf",
                                            "Shifter (Beasthide)",
                                            "Shifter (Longtooth)",
                                            "Shifter (Wildhunt)",
                                            "Shifter",
                                            "Simic Hybrid",
                                            "Skeleton",
                                            "Tabaxi",
                                            "Thri-kreen",
                                            "Tiefling (Asmodeus)",
                                            "Tiefling (Baalzebul)",
                                            "Tiefling (Base)",
                                            "Tiefling (Dispater)",
                                            "Tiefling (Fierna)",
                                            "Tiefling (Glasya)",
                                            "Tiefling (Levistus)",
                                            "Tiefling (Mammon)",
                                            "Tiefling (Mephistopheles)",
                                            "Tiefling (Variant; Devil's Tongue)",
                                            "Tiefling (Variant; Hellfire)",
                                            "Tiefling (Variant; Infernal Legacy)",
                                            "Tiefling (Variant; Winged)",
                                            "Tiefling (Zariel)",
                                            "Tiefling",
                                            "Tortle",
                                            "Triton",
                                            "Troglodyte",
                                            "Varies",
                                            "Vedalken",
                                            "Verdan",
                                            "Warforged",
                                            "Yuan-Ti",
                                            "Yuan-ti Pureblood",
                                            "Zombie",
                                        ],
                                        id="race",
                                        placeholder="Character Race",
                                    ),
                                ),
                                html.Div(
                                    dcc.Dropdown(
                                        [
                                            "Alchemist",
                                            "Artificer",
                                            "Barbarian",
                                            "Bard",
                                            "Blood Hunter",
                                            "Cleric",
                                            "Druid",
                                            "Fighter",
                                            "Monk",
                                            "Paladin",
                                            "Ranger",
                                            "Rogue",
                                            "Sorcerer",
                                            "Warlock",
                                            "Wizard"
                                        ],
                                        id="class",
                                        placeholder="Character Class",
                                    ),
                                ),
                                html.Div(
                                    dcc.Dropdown(
                                        [
                                            "Arcane Repo Reaper",
                                            "Acolyte",
                                            "Anthropologist",
                                            "Archaeologist",
                                            "Astral Drifter",
                                            "Athlete",
                                            "Azorius Functionary",
                                            "Baldur's Gate Acolyte",
                                            "Baldur's Gate Charlatan",
                                            "Baldur's Gate Criminal",
                                            "Baldur's Gate Entertainer",
                                            "Baldur's Gate Folk Hero",
                                            "Baldur's Gate Guild Artisan",
                                            "Baldur's Gate Hermit",
                                            "Baldur's Gate Noble",
                                            "Baldur's Gate Outlander",
                                            "Baldur's Gate Sage",
                                            "Baldur's Gate Sailor",
                                            "Baldur's Gate Soldier",
                                            "Baldur's Gate Urchin",
                                            "Boros Legionnaire",
                                            "Celebrity Adventurer's Scion",
                                            "Charlatan",
                                            "City Watch",
                                            "City Watch (Investigator)",
                                            "Clan Crafter",
                                            "Cloistered Scholar",
                                            "Courtier",
                                            "Criminal",
                                            "Criminal (Spy)",
                                            "Custom Background",
                                            "Dimir Operative",
                                            "Entertainer",
                                            "Entertainer (Gladiator)",
                                            "Faceless",
                                            "Faction Agent",
                                            "Failed Merchant",
                                            "Far Traveler",
                                            "Feylost",
                                            "Fisher",
                                            "Folk Hero",
                                            "Gambler",
                                            "Gate Warden",
                                            "Giant Foundling",
                                            "Golgari Agent",
                                            "Gruul Anarch",
                                            "Guild Artisan",
                                            "Guild Artisan (Guild Merchant)",
                                            "Haunted One",
                                            "Hermit",
                                            "House Agent",
                                            "Inheritor",
                                            "Investigator",
                                            "Izzet Engineer",
                                            "Knight of Solamnia",
                                            "Knight of the Order",
                                            "Lorehold Student",
                                            "Mage of High Sorcery",
                                            "Marine",
                                            "Mercenary Veteran",
                                            "Noble",
                                            "Noble (Knight)",
                                            "Noble (Retainers)",
                                            "Orzhov Representative",
                                            "Outlander",
                                            "Plaintiff",
                                            "Planar Philosopher",
                                            "Prismari Student",
                                            "Quandrix Student",
                                            "Rakdos Cultist",
                                            "Rewarded",
                                            "Rival Intern",
                                            "Ruined",
                                            "Rune Carver",
                                            "Sage",
                                            "Sailor",
                                            "Sailor (Pirate)",
                                            "Selesnya Initiate",
                                            "Shipwright",
                                            "Silverquill Student",
                                            "Simic Scientist",
                                            "Smuggler",
                                            "Soldier",
                                            "Urban Bounty Hunter",
                                            "Urchin",
                                            "Uthgardt Tribe Member",
                                            "Waterdhavian Noble",
                                            "Wildspacer",
                                            "Witchlight Hand",
                                            "Witherbloom Student",                                        
                                        ],
                                        id="background",
                                        placeholder="Character Background",
                                    ),
                                ),
                            ],
                        ),
                        dbc.Row(html.Hr()),
                        dbc.Row([]),
                    ]
                ),
                dbc.Col(
                    [
                    ]
                ),
            ]
        )
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
                        
