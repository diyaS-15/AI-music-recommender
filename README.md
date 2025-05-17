# AI-music-recommender
Live Demo: https://ai-song-recommender.streamlit.app/ 

## Description
Welcome! This is music recommendation webapp where the user can input their current mood, intended event or audience and recieve a recommended song with a playable preview. This was done using Gemini Developer API, Spotify Web API, and Streamlit in Python.

- Gemini Developer API allowed for easy intelligent song recommendation using the Gemini model
- Spotify Web API was used to integrate song preview functionality to play recommended track 
- Streamlit for convient frontend to display and deploy webapp

The project can be run locally using streamlit run web.py

## Files:
- web.py: main file that has gemini api call, spotify api call, and streamlit code
- .env: environment file that holds my gemini api key, client-id, and client-secret
- config.toml: added background color.

### Important Notes:
- .env file is not in the repository as it holds sensitive information, like personal api keys.
