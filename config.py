from dotenv import load_dotenv
import os, base64, requests, json, random

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_token():
    auth_string = f'{CLIENT_ID}:{CLIENT_SECRET}'
    auth_bytes = auth_string.encode('utf-8')
    auth_b64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token

def get_popular():
    songs = []

    token = get_token()

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    url = 'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF/tracks' # spotify top 50
    result = requests.get(url, headers=headers)
    result_json = json.loads(result.content)

    for song in result_json["items"]:
        songs.append(
            [song["track"]["name"], song["track"]["artists"][0]["name"]]
        )

    return random.choice(songs)