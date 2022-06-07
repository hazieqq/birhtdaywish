from flask import Flask, render_template
import secrets

app = Flask(__name__)

@app.route('/')
def index():
    #TODO:  check for session log in first
    return render_template('home.html')
        