import sys
import os
from urllib.parse import urlparse
from flask import Flask, render_template, request
from youtube import get_playlist, create_playlist, add_playlist_item, youtube_playlist, search_id
from spotify import spotify_get, spotify_search

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def conversion():
    return render_template('convert.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/congratulations', methods=['POST'])
def final_page():
    if request.method == 'POST':
        name = request.form['playlist_name']
        link = request.form['playlist_link']
        desc = request.form['description']
        conversion_type = request.form['conversion']
        parsed_url = urlparse(link)
        path = parsed_url.path
        query = parsed_url.query
        youtube_link = None  # Define the variable outside the if statement
        spotify_link = None
        error = None
        if conversion_type == 'Spotify-Youtube':
            ll = path.split('/')
            if len(ll) >= 2:  # Ensure we have at least 2 parts after splitting
                music = spotify_get(ll[2])
                youtube_link = youtube_playlist(name, desc, music)
            else:
                error = "Invalid path format for Spotify-Youtube conversion"
        elif conversion_type == 'Youtube-Spotify':
            lam = query.split('=')
            if len(lam) >= 1:  # Ensure we have at least 1 parts after splitting
                music = get_playlist(lam[1].split('&'))
                spotify_link = spotify_search(name, desc, music)
            else:
                error = "Invalid query format for Youtube-Spotify conversion"
        return render_template('congratulations.html', spotify_link=spotify_link,
                               youtube_link=youtube_link, error=error)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
