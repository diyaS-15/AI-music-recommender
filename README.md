# AI-music-recommender

This AI music recommendation webapp takes in user input for the mood and the event/audience and uses Gemini model to return a song recommendation.
- Utilized Gemini API to run the model and generate a song
- Utilized Spotify Web API to get tracks and integrate song preview function
- Used Python's Streamlit library to launch webapp to host the information

The project can be run locally using streamlit run web.py


## Files:
- web.py: main file that has gemini api call, spotify api call, and streamlit code
- .env: environment file that holds my gemini api key, client-id, and client-secret 
- config.toml: added background color.

### Important Notes:
- .env file is not in the repository as it holds sensitive information, like personal api keys.
- the config.toml file has to be inside a .streamlit folder to correctly work
