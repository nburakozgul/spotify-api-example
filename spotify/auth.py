import requests
import json

from spotify import app

CLIENT_ID = "2a8c1ebe32df454d9edebf3788132b7b";
CLIENT_SECRET = "73e074701aed43f0a3e9e27d3fb5a01d";

TOKEN_URL = "https://accounts.spotify.com/api/token";

def auth():
    data = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'grant_type': 'client_credentials',
    }

    # `auth=(CLIENT_ID, SECRET)` basically wraps an 'Authorization'
    # header with value:
    # b'Basic ' + b64encode((CLIENT_ID + ':' + SECRET).encode())
    res = requests.post(TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), data=data)
    res_data = res.json()

    access_token = res_data.get('access_token')

    return access_token