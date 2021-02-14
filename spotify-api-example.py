from flask import Flask
from flask import render_template
from file import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/genre/')
@app.route('/genre/<genre>')
def hello(genre=None):
    artist = randomArtistFromGenre(genre)
    return render_template('datatable.html', artist=artist)