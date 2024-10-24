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
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Card([dbc.CardHeader("Strength"),dbc.CardBody([html.H4(["18"," / ", "+4"])])]),
                                        dbc.Card([dbc.CardHeader("Dexterity"),dbc.CardBody([html.H4(["18"," / ", "+4"])])]),
                                        dbc.Card([dbc.CardHeader("Constitution"),dbc.CardBody([html.H4(["18"," / ", "+4"])])]),
                                        dbc.Card([dbc.CardHeader("Inteligence"),dbc.CardBody([html.H4(["18"," / ", "+4"])])]),
                                        dbc.Card([dbc.CardHeader("Wisdom"),dbc.CardBody([html.H4(["18"," / ", "+4"])])]),
                                        dbc.Card([dbc.CardHeader("Charisma"),dbc.CardBody([html.H4(["18"," / ", "+4"])])]),
                                    ],
                                    width = 1,
                                ),
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            [
                                                dbc.CardHeader("Saving Throws"),
                                                dbc.CardBody(
                                                    [
                                                        dbc.Row(html.P(["+1"," ","Strength"])),
                                                        dbc.Row(html.P(["+1"," ","Dexterity"])),
                                                        dbc.Row(html.P(["+1"," ","Constitution"])),
                                                        dbc.Row(html.P(["+1"," ","Inteligence"])),
                                                        dbc.Row(html.P(["+1"," ","Wisdom"])),
                                                        dbc.Row(html.P(["+1"," ","Charisma"])),
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
                                                        dbc.Row([html.P("+1"),html.P(" "),html.P("Survival")]),
                                                    ]
                                                )
                                            ]
                                        ),
                                        dbc.Card(
                                            [
                                                dbc.CardHeader(""),
                                                dbc.CardBody(),
                                            ]
                                        ),
                                    ],
                                    width = 2,
                                )
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
