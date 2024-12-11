#host/app.py

from flask import Flask, render_template_string, g
import ssl
import pandas as pd
from dash_apps import simple_app, population
app = Flask(__name__)

with app.app_context():
    # Define Flask context variables to be used in apps. 
    # In this case, we define the dataframe used in the Population app (df)
    # and the Flask instance to be passed to both apps (cur_app)
    g.df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
    )

    g.cur_app = app

    # Add Dash app to Flask context. Specify the app's url path and pass the flask server to your data
    app = simple_app.init_app("/simple_app/")
    app = population.init_app("/population/")

@app.route("/")
def home():
    return render_template_string(f"""
        <h1>Main Flask App</h1>
        <h2>Select your Dash App</h2>
        <ul>
            <li><a href:'/simple_app/'>Simple App</a></li>
            <li><a href:'/population/'>Population</a></li>
        </ul>"""
    )
