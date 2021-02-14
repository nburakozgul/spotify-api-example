from flask import Flask
from flask import render_template

from spotify import app
from spotify.file import *
from spotify.auth import *


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/genre/')
@app.route('/genre/<genre>')
def hello(genre=None):
    artist = randomArtistFromGenre(genre)
    return render_template('datatable.html', artist=artist)