# TUTTI I SETUP CHE NOI VOGLIAMO CONFIGURARE

import os
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder="static")

# Use bootstrap with the app
Bootstrap(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = "chiavesegreta"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "db.sqllite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

