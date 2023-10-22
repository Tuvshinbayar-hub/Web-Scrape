import os
import requests
import spotipy

from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

URL = 'https://api.spotify.com/v1/search'
scope = "user-library-read, playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()['id']
# sp.user_playlist_create(user=user_id, name='1998-05-07 Top 100 BillBoard', description='Nostalgic songs')
first_album_id = sp.current_user_playlists()['items'][0]['id']
print(first_album_id)


def search_song(song_name: str, year: int):
    result = sp.search(q=f'track:{song_name} year:{year-2}-{year}', type='track')
    if len(result['tracks']['items']) == 0:
        return None
    else:
        return result['tracks']['items'][0]['uri']


def add_track(track_id: str, tracks: list):
    sp.playlist_add_items(playlist_id=track_id, items=tracks)


input_date = input('Which year do you want to travel to? type the data in YYYY-MM-DD format: \n')
year_int = int(input_date.split('-')[0])
url = f'https://www.billboard.com/charts/hot-100/{input_date}/'
response = requests.get(url=url)
contents = response.text

soup = BeautifulSoup(contents, 'lxml')
names_raw = soup.select('.o-chart-results-list__item #title-of-a-story')
names_processed = [name.string.replace('\n\n\t\n\t\n\t\t\n\t\t\t\t\t', '')
                   .replace('\t\t\n\t\n', '') for name in names_raw]

track_list = []
for name in names_processed:
    temp_track = search_song(name, year_int)
    if temp_track is not None:
        track_list.append(temp_track)

sp.playlist_add_items(playlist_id=first_album_id, items=track_list)
