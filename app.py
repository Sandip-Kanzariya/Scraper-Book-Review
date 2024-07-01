from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from api.views import book_blueprint
import os
from extensions import db, migrate

app = Flask(__name__)

@app.route('/')
def index(): 
    return "Hello "

app.config.from_object("config") # Load configurations from config.py file
db.init_app(app) 
migrate.init_app(app, db)

# Additional code to create database tables
with app.app_context():
    db.create_all()


# For Endpoints
app.register_blueprint(blueprint=book_blueprint)


if __name__ == '__main__':
    app.run(
        host=app.config.get("FLASK_RUN_HOST"),
        port=app.config.get("FLASK_RUN_PORT"),
        debug=app.config.get("FLASK_DEBUG"),
    )