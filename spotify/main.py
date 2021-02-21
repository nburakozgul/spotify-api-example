from flask import Flask
from flask import render_template,url_for,redirect

from spotify import app
from spotify.file import *
from spotify.auth import *
from spotify.static.contants import *

ACCESS_TOKEN = "";
N = 5 #number of the top songs

@app.route('/') #open datatable with only search bar ?
def root():
    global ACCESS_TOKEN
    
    if not ACCESS_TOKEN: 
        ACCESS_TOKEN = auth()
    return redirect(url_for('genre',genre='rock'))

@app.route('/genre/')
@app.route('/genre/<genre>')
def genre(genre=None):
    global ACCESS_TOKEN
    artist = randomArtistFromGenre(genre)

    if not artist:
        return render_template('datatable.html', data={"error_message": GENRE_NOT_FOUND})
    
    if not ACCESS_TOKEN: 
        ACCESS_TOKEN = auth()
        if not ACCESS_TOKEN: 
            return render_template('datatable.html', data={"error_message":AUTH_ERROR_MESSAGE})

    artist_info = getArtist(artist,ACCESS_TOKEN)
    if not artist_info:
        return render_template('datatable.html', data={"error_message":AUTH_ERROR_MESSAGE})
        
    if artist_info['artists']['total'] != 0:
        artist_id = artist_info['artists']['items'][0]['id'] #id of the first artist from the search
        artist_name = artist_info['artists']['items'][0]['name']

        top_tracks = getTopTracksOfArtist(artist_id,ACCESS_TOKEN) #top N songs of given artist
        if not top_tracks:
            return render_template('datatable.html', data={"error_message":AUTH_ERROR_MESSAGE})
        else:
            top_tracks = top_tracks['tracks'][:N]

        data = {"artist_name":artist_name,"genre":genre, "songs":[]} #simple json object created for table
        for track in top_tracks:
            track_name = track['name']
            album_name = track['album']['name']
            release_date = track['album']['release_date']
            album_cover =  track['album']['images'][len(track['album']['images'])-1]
            item = {"track_name":track_name,"album_name":album_name,"release_date":release_date,"album_cover":album_cover}
            data['songs'].append(item)
    else:
        return render_template('datatable.html', data={"error_message":ARTIST_NOT_FOUND})
        
    return render_template('datatable.html', data=data)