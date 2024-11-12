from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
import json
import os
from dotenv import load_dotenv
from state import State

load_dotenv()  

llm = ChatOpenAI(model="gpt-4")

# Retrieve API keys from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BOOKING_API_KEY = os.getenv("BOOKING_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8888/callback"

def get_spotify_access_token():
    auth_url = "https://accounts.spotify.com/api/token"
    response = requests.post(
        auth_url,
        {
            "grant_type": "client_credentials",
            "client_id": SPOTIFY_CLIENT_ID,
            "client_secret": SPOTIFY_CLIENT_SECRET,
        }
    )
    return response.json().get("access_token")

latest_location = {"latitude": None, "longitude": None}

@tool
def get_location(state: State, latitude=None, longitude=None):
    global latest_location
    if latitude is not None and longitude is not None:
        # Update the global variable to store the latest location
        latest_location["latitude"] = latitude
        latest_location["longitude"] = longitude
        state['location'] = f"{latitude}, {longitude}"
    elif latest_location["latitude"] is not None and latest_location["longitude"] is not None:
        # If location data was previously saved, use it
        state['location'] = f"{latest_location['latitude']}, {latest_location['longitude']}"
    else:
        state['location'] = "Location not available"
    return state


def get_spotify_access_token():
    auth_url = "https://accounts.spotify.com/api/token"
    response = requests.post(
        auth_url,
        {
            "grant_type": "client_credentials",
            "client_id": SPOTIFY_CLIENT_ID,
            "client_secret": SPOTIFY_CLIENT_SECRET,
        }
    )
    response_data = response.json()
    return response_data.get("access_token")

@tool
def play_song(song_name: str):
    token = get_spotify_access_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Step 1: Search for the song on Spotify
    search_url = f"https://api.spotify.com/v1/search?q={song_name}&type=track&limit=1"
    search_response = requests.get(search_url, headers=headers)
    search_data = search_response.json()

    if not search_data['tracks']['items']:
        return f"Song '{song_name}' not found on Spotify."

    # Get the track ID from search results
    track_id = search_data['tracks']['items'][0]['id']

    # Step 2: Play the song on a connected device
    # (Assumes user has Spotify open on a connected device)
    play_url = f"https://api.spotify.com/v1/me/player/play"
    play_data = {
        "uris": [f"spotify:track:{track_id}"]
    }

    play_response = requests.put(play_url, headers=headers, data=json.dumps(play_data))

    if play_response.status_code == 204:
        # 204 No Content means the request was successful
        track_name = search_data['tracks']['items'][0]['name']
        artist_name = search_data['tracks']['items'][0]['artists'][0]['name']
        return f"Playing '{track_name}' by {artist_name} on Spotify."
    else:
        return "Unable to play the song. Make sure Spotify is open and a device is connected."
  
