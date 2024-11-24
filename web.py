from dotenv import load_dotenv
load_dotenv()
import spotipy
import os
import base64
from requests import post,get
import requests
import json

myAPI = os.getenv("MY_API_KEY")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_song(token, song_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={song_name}&type=track&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    if len(json_result) == 0:
        print("No songs found")
        return None
    return json_result[0]

token = get_token()

import streamlit as st

st.set_page_config(layout="wide")
# streamlit run web.py - how to run streamlit

st.title("AI Music Recommender")

mood = st.text_input("Enter mood: ", value=" ")
evt = st.text_input("Enter event or audience: ", value=" ")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={myAPI}"
headers = {
    'Content-Type': 'application/json'
}
data = {
    'contents': [
        {
            'parts': [
                {'text': f"Without requiring additional information, recommend a {mood} song for {evt}."}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data = json.dumps(data))

responseDict = json.loads(response.text)
st.text(responseDict["candidates"][0]["content"]["parts"][0]["text"])

print(response.text)
print(response.status_code)

result = search_for_song(token, responseDict["candidates"][0]["content"]["parts"][0]["text"])
# track_id = result["id"]
song_preview = result["preview_url"]
st.audio(song_preview, format="audio/mp3")
