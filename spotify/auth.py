import requests
import json

from spotify import app

CLIENT_ID = "";
CLIENT_SECRET = ""; #do not share your client_secret again 

TOKEN_URL = "https://accounts.spotify.com/api/token";
SEARCH_URL = "https://api.spotify.com/v1/search";
ARTIST_URL = "https://api.spotify.com/v1/artists/{}/top-tracks";

#basic auth that returns access token
def auth():
    data = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'grant_type': 'client_credentials',
    }

    res = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), data=data)
    res_data = res.json()

    access_token = res_data.get('access_token')
    return access_token

#returns artist search result as json
def getArtist(artist,access_token):
    hearders = headers = {
        "Authorization": "Bearer " + access_token
    }
    params = { 'q': artist, 'type': 'artist' }

    artist_info = requests.get(SEARCH_URL,headers=hearders,params=params)
    if not artist_info:
        access_token = auth()
        artist_info = requests.get(SEARCH_URL,headers=hearders,params=params)

    return artist_info.json()

#top tracks of artist
def getTopTracksOfArtist(artist_id,access_token):
    
    hearders = headers = {
        "Authorization": "Bearer " + access_token
    }

    params = { 'market': 'TR' }

    top_tracks = requests.get(ARTIST_URL.format(artist_id),headers=hearders,params=params)
    if not top_tracks:
        access_token = auth()
        top_tracks = requests.get(SEARCH_URL,headers=hearders,params=params)

    return top_tracks.json()