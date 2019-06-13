from app import app
import constituency
import voter
import result
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')