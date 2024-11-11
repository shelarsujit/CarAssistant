from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  

llm = ChatOpenAI(model="gpt-4")

# Retrieve API keys from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BOOKING_API_KEY = os.getenv("BOOKING_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

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

@tool
def get_location(state: State):
    # Retrieve user’s GPS location
    state['location'] = "Pune, India"
    return state

@tool
def play_song(song_name: str):
    token = get_spotify_access_token()
  
