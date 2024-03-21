import pprint
from ytmusicapi import YTMusic
ytmusic = YTMusic("oauth.json")

pp = pprint.PrettyPrinter(width=41, compact=True)
# pp.pprint(search_results)


def get_playlist(playlist_id):
    playlist = ytmusic.get_playlist(playlist_id)
    music = []
    for num in range(len(playlist['tracks'])):
        music.append(playlist['tracks'][num]['title'] + ' ' + playlist['tracks'][num]['artists'][0]['name'])
    return music


def create_playlist(name, description):
    new_playlist = ytmusic.create_playlist(name, description)
    return new_playlist


def add_playlist_item(playlist_id, titles):
    items = ytmusic.add_playlist_items(playlist_id, titles)
    return items


def youtube_playlist(name, description, mus : list):
    ided = create_playlist(name, description)
    songs = []
    for music in mus:
        song = search_id(music)
        songs.append(song)
    add_playlist_item(ided, songs)
    return ided


def search_id(musics):
    sang = ytmusic.search(query=musics)
    # pp.pprint(sang[0])
    if sang[0]['videoId'] is not None:
        return sang[0]['videoId']
    elif sang[0]['videoId'] is None:
        return sang[1]['videoId']
