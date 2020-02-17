from flask import render_template
from app import app
from . import main


@main.route('/')
def home():
     return render_template('home.html')