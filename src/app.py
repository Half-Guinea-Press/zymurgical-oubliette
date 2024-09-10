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
                        dbc.Row(
                            [
                                dbc.Col([html.Div(html.Img(src="assets/Valdris%20Fossic%20head.jpg",width="100%")),],width=4),
                                dbc.Col(
                                    [
                                        html.H5("Blood Hunter Lvl 2"),
                                        html.H6(
                                            [
                                                "Dhampyr",
                                                html.Br(),
                                                "Arcane Repo Reaper",
                                                html.Br(),
                                                "Lawfull Neutral",
                                                html.Br(),
                                                "Medium"
                                            ]
                                        ),
                                    ],width=4
                                ),
                            ]
                        ),
                        dbc.Row(html.Br()),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Table(
                                            [
                                                html.Tbody(
                                                    [
                                                        html.Tr(
                                                            [
                                                                html.Td("STR"),
                                                                html.Td("20(+5)"),
                                                            ]
                                                        ),
                                                        html.Tr(
                                                            [
                                                                html.Td("DEX"),
                                                                html.Td("20(+5)"),
                                                            ]
                                                        ),
                                                        html.Tr(
                                                            [
                                                                html.Td("CON"),
                                                                html.Td("20(+5)"),
                                                            ]
                                                        ),
                                                        html.Tr(
                                                            [
                                                                html.Td("INT"),
                                                                html.Td("20(+5)"),
                                                            ]
                                                        ),
                                                        html.Tr(
                                                            [
                                                                html.Td("WIS"),
                                                                html.Td("20(+5)"),
                                                            ]
                                                        ),
                                                        html.Tr(
                                                            [
                                                                html.Td("CHR"),
                                                                html.Td("20(+5)"),
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                            ],bordered=True,striped=True
                                        ),
                                    ],
                                    width=1,
                                ),
                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Table(
                                                    [
                                                        html.Thead(
                                                            html.Tr(
                                                                [
                                                                    html.Th("AC"),
                                                                    html.Th("INIT"),
                                                                    html.Th("SPD"),
                                                                    html.Th("HP"),
                                                                    html.Th("Prof"),
                                                                ]
                                                            )
                                                        ),
                                                        html.Tbody(
                                                            [
                                                                html.Tr(
                                                                    [
                                                                        html.Td("16"),
                                                                        html.Td("+5"),
                                                                        html.Td("30"),
                                                                        html.Td("20"),
                                                                        html.Td("+2"),
                                                                    ]
                                                                ),
                                                            ]
                                                        ),
                                                    ],bordered=True,striped=True
                                                ),
                                            ]
                                        ),
                                        dbc.Row([html.Hr()]),
                                        dbc.Row(
                                            [
                                                dcc.Markdown('''
                                                    **Saving Throws:** list of saves, saves  
                                                    **Skills:** list of saves, saves  
                                                    **Senses:** list of saves, saves  
                                                    **Tools, Instuments, Games:** list of saves, saves  
                                                    **Langauges:** list of saves, saves
                                                '''),
                                            ]
                                        ),
                                        dbc.Row([html.Hr()]),
                                        dbc.Row(
                                            [
                                                dcc.Markdown('''
                                                    **Racial Features:** list of features,features  
                                                    **Class Features:** list of features,features  
                                                    **Background Features:** list of features,features  
                                                    **Other Features:** list of features,features  
                                                '''),
                                            ]
                                        )
                                    ],
                                    width=2,
                                )
                            ]
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Tabs(
                            [
                                dbc.Tab(
                                    [
                                        
                                    ],
                                    label="Character Details",
                                ),
                                dbc.Tab(
                                    dbc.Accordion(
                                        [
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="Cantrips"
                                            ),
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="1st Lvl"
                                            ),
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="2nd Lvl"
                                            ),
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="3rd Lvl"
                                            ),
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="4th Lvl"
                                            ),
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="5th Lvl"
                                            ),
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="6th Lvl"
                                            ),
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="7th Lvl"
                                            ),
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="8th Lvl"
                                            ),
                                            dbc.AccordionItem(
                                                dcc.Markdown('''
                                                    
                                                '''),
                                                title="9th Lvl"
                                            ),
                                        ],
                                    ),
                                    label="Spell Book",
                                ),
                                dbc.Tab(
                                    [
                                        
                                    ],
                                    label="Equipment",
                                ),
                            ]
                        )
                    ]
                )
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
                                html.Br()
                            ],
                        ),
                        dbc.Row(
                            [
                                html.Br(),
                                html.Hr(),
                                html.Br(),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.InputGroup([dbc.InputGroupText("Strength"),dbc.Input(id="Ability Score Strength", type="number", min = 0, max = 20)],className="mb-3"),
                                        dbc.InputGroup([dbc.InputGroupText("Dexterity"),dbc.Input(id="Ability Score Dexterity", type="number", min = 0, max = 20)],className="mb-3"),
                                        dbc.InputGroup([dbc.InputGroupText("Constitution"),dbc.Input(id="Ability Score Constitution", type="number", min = 0, max = 20)],className="mb-3"),
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.InputGroup([dbc.InputGroupText("Intelligence"),dbc.Input(id="Ability Score Intelligence", type="number", min = 0, max = 20)],className="mb-3"),
                                        dbc.InputGroup([dbc.InputGroupText("Wisdom"),dbc.Input(id="Ability Score Wisdom", type="number", min = 0, max = 20)],className="mb-3"),
                                        dbc.InputGroup([dbc.InputGroupText("Charisma"),dbc.Input(id="Ability Score Charisma", type="number", min = 0, max = 20)],className="mb-3"),
                                    ]
                                ),
                            ]
                        )                        
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Accordion(
                            [
                                dbc.AccordionItem(
                                    "This is the content of the first section",
                                    title="Racial Features",
                                ),
                                dbc.AccordionItem(
                                    "This is the content of the second section",
                                    title="Class Features",
                                ),
                                dbc.AccordionItem(
                                    "This is the content of the third section",
                                    title="Background Features",
                                ),
                                dbc.AccordionItem(
                                    "This is the content of the third section",
                                    title="Character Starting Equipment",
                                ),
                            ],
                            always_open=True,
                        ),
                    ]
                ),
                dbc.Col(
                    [
                    ]
                )
            ]
        )
    ],
)

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
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
                    dbc.NavItem(dbc.NavLink("PC", href="/pc", active="exact")),
                    dbc.NavItem(dbc.NavLink("Character Design", href="/character_design", active="exact")),
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
                        
