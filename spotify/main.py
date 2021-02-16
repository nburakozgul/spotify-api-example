from flask import Flask
from flask import render_template

from spotify import app
from spotify.file import *
from spotify.auth import *

ACCESS_TOKEN = "";
N = 5 #number of the top songs

@app.route('/') #open datatable with only search bar ?
def hello_world():
    return 'Hello, World!'

@app.route('/genre/')
@app.route('/genre/<genre>')
def genre(genre=None):
    global ACCESS_TOKEN
    artist = randomArtistFromGenre(genre)
    
    if not ACCESS_TOKEN: #need refresh token
        ACCESS_TOKEN = auth()

    artist_info = getArtist(artist,ACCESS_TOKEN)

    #if there is no artist? need to handle
    if artist_info['artists']['total'] != 0:
        artist_id = artist_info['artists']['items'][0]['id'] #id of the first artist from the search
        artist_name = artist_info['artists']['items'][0]['name']

        top_tracks = getTopTracksOfArtist(artist_id,ACCESS_TOKEN)['tracks'][:N] #top N songs of given artist

        data = {"artist_name":artist_name, "songs":[]} #simple json object created for table
        for track in top_tracks:
            track_name = track['name']
            album_name = track['album']['name']
            release_date = track['album']['release_date']
            album_cover =  track['album']['images'][len(track['album']['images'])-1]
            item = {"track_name":track_name,"album_name":album_name,"release_date":release_date,"album_cover":album_cover}
            data['songs'].append(item)
        
    return render_template('datatable.html', data=data)