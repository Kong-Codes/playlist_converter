import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
user_id1 = "31pzol73ivznps56jgpx54g2g4ce"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username=user_id1,
    )
)

# user_id = sp.current_user()["id"]
# print(user_id)


def spotify_search(name, desc, song_name: list):
    user_id = sp.current_user()["id"]
    song_uris = []
    for song in song_name:
        result = sp.search(q=f"{song}")
        # print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    playlist = sp.user_playlist_create(user=user_id, name=f"{name}", public=False, description=f"{desc}")

    playlist_id = playlist["id"]

    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
    return playlist_id


def spotify_get(playlist_id):
    songs = sp.playlist(playlist_id)
    music = []
    for num in range(len(songs['tracks']['items'])):
        music.append(songs['tracks']['items'][num]['track']['name'] + ' ' + songs['tracks']['items'][num]['track']['album']['artists'][0]['name'])
    return music
