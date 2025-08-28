import pandas as pd
from src.connections import get_spotify_client

artistas_df = pd.read_excel('artistas.xlsx')
artistas = artistas_df['artistas']

for artista in artistas:
    sp = get_spotify_client()
    res = sp.search(q=str(artista), type='artist', limit=1)
    if res['artists']['items']: 
        artista_id = res['artists']['items'][0]['id']
        artista_name = res['artists']['items'][0]['name']
        artista_track = sp.artist_top_tracks(artista_id, country='BR')
        print(f'Id: {artista_id} Nome: {artista_name}')
        for track in artista_track['tracks']:
            print(track['name'])