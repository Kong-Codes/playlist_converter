# playlist_converter

## Overview
This project revolves entirely around converting music playlists from Youtube to Spotify seamlessly.

The provided script in `app.py` is the flask server used to run the process live on the web.
The provided script in the `youtube.py` is used to extract and compile a playlist within Youtube music.

The `youtube.py` contains the following methods:

- `get_playlist`: This function extracts all the songs in a youtube music playlist and returns a list.
- `create_playlist`: This function creates a youtube music playlist.
- `add_playlist_item`: This function adds songs to the created playlist.
- `youtube_playlist`: This function returns the link to the playlist.
- `search_id`: This function extracts the song search id.

The provided script in the `spotify.py` is used to extract and compile a playlist within spotify.


The `spotify.py` contains the following methods:

- `spotify_get`: This function extracts all the songs in a spotify music playlist and returns a list.
- `spotify_search`: This function returns the link to the playlist.

## Technologies used
- HTML
- CSS
- Python  <br>
  *Dependencies used:*
  - flask: `^3.0.2`
  - spotipy: `^2.23.0`
  - ytmusicapi: `^1.6.0`
  - python-dotenv: `^1.0.1`


## Prerequisites
- Spotify account
- Youtube account
- Python3.9+ Intepreter
