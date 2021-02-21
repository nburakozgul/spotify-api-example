# spotify-api-example
Spotify API Client Credentials Example

## How to run

On project folder run this comment to create a venv folder:

### `python3 -m venv venv`

On Windows :

### `py -3 -m venv venv`

---------------------------------------------------------------------------------------------
Before you work on your project, activate the corresponding environment:

### ` . venv/bin/activate`

On Windows :

### `venv\Scripts\activate`

---------------------------------------------------------------------------------------------

Within the activated environment, use the following command to install required packages:

### `pip install -r .\requirements.txt`

---------------------------------------------------------------------------------------------

Tell your terminal the application to work with by exporting the FLASK_APP environment variable:

### `export FLASK_APP=spotify`

On windows

### `set FLASK_APP=spotify`

On PowerShell

### `$env:FLASK_APP = "spotify"`

---------------------------------------------------------------------------------------------

Before run the application set cliend_id and client_secret

You can from edit auth.py also you can set into spotify_credentials.txt (first line client_id, second line client_secret)

---------------------------------------------------------------------------------------------
Run Flask

### `flask run`

Running on http://127.0.0.1:5000/ 
