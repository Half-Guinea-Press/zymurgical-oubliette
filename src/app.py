from flask import Flask, render_template_string
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from dash_apps import simple_app, population
import pandas as pd

# Initialize Flask server
flask_app = Flask(__name__)

with flask_app.app_context():
    # Define Flask context variables to be used in apps. 
    # In this case, we define the dataframe used in the Population app (df)
    # and the Flask instance to be passed to both apps (cur_app)
    g.df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
    )

    # Integrate Flask and Dash apps using DispatcherMiddleware
    # The app becomes a Middleware instance, which will default to the 
    # routes in the Flask app if the URL is not found among the mounted
    # Dash apps
    app = DispatcherMiddleware(flask_app, {
        "/simple_app": simple_app.init_app("/simple_app/"),
        "/population": population.init_app("/population/")
    })

@flask_app.route("/")
def home():
    return render_template_string(f"""
        <h1>Main Flask App</h1>
        <h2>Select your Dash App</h2>
        <ul>
            <li><a href:'/simple_app/'>Simple App</a></li>
            <li><a href:'/population/'>Population</a></li>
        </ul>"""
    )
