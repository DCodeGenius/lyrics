from flask import Flask , request
import requests
import json
#from bson.json_util import dumps
from secrets import *
import webbrowser
import base64
from get_url import url_name
from bs4 import BeautifulSoup
import requests
import time
import os.path


app = Flask(__name__)


#step 1 : authorization_code
redirect_url = "http://localhost:5000/api/callback"
scopes = "user-read-currently-playing%20user-read-playback-state"
url = f'https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_url}&' \
      f'scope={scopes}'
authorization_code = 'none'
webbrowser.open(url)

while not os.path.exists("authorization_code.txt"):
    time.sleep(1)
with open("authorization_code.txt", 'r') as f:
    authorization_code = f.read()
os.remove("authorization_code.txt")

# Step 2 - Access tokens
url_token = "https://accounts.spotify.com/api/token"
headers = {}
body = {}

# Encode as Base64
message = f"{client_id}:{client_secret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')

# insert the requested parameters to headers, body
headers['Authorization'] = f"Basic {base64Message}"
body['grant_type'] = "authorization_code"
body['code'] = authorization_code
body['redirect_uri'] = redirect_url

# post request
r = requests.post(url_token, headers=headers, data=body)

# spotify response
token = r.json()['access_token']
expires_in = r.json()['expires_in']
authorization_code = r.json()['refresh_token']


# step 3: access to spotify web api
market_code = 'IL'
url_getCurrentTrack = f'https://api.spotify.com/v1/me/player/currently-playing?market={market_code}'
current_track = requests.get(url_getCurrentTrack, headers={"Authorization": "Bearer " + token})

current_track_json = current_track.json()
item = current_track_json['item']
name_track = item['name']
name_artist = item['artists'][0]['name']

lyrics_url = url_name(name_artist, name_track)
webbrowser.open("http://localhost:5002/api/lyrics")

@app.route("/api/lyrics")
def lyrics():
    html_text = requests.get(lyrics_url)
    html_text = html_text.text
    soup = BeautifulSoup(html_text, 'lxml')
    body_html = soup.find("routable-page")
    lyrics_song = body_html.find("div", class_="lyrics").text
    return lyrics_song


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)






#erors?