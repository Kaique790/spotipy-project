from src.connections import get_spotify_client
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sp = get_spotify_client()

def fetchArtist(artist):
    results = sp.search(q=artist, type="artist", limit=1)
        
    if results["artists"]["items"]:
        artist = results["artists"]["items"][0]
        data = {
            "name": artist["name"],
            "id": artist["id"],
            "followers": artist["followers"]["total"],
            "genres": ", ".join(artist["genres"]),
            "popularity": artist["popularity"]
        }
        return data
    
    print("Artista não encontrado")
    return None

def persist_data(data):
    df = pd.DataFrame(data)
    df.to_excel("artists.xlsx")

def get_artists():
    artists = []
    i = 0
    while True:
        i += 1
        print("Digite exit para não selecionar mais artistas")
        artist = input(f"Digite o artista {i}: ")

        if artist == "exit":
            print("saindo")
            break

        searchedArtist = fetchArtist(artist)
        if not searchedArtist:
            print("Artista não encontrado")
            continue

        artists.append(searchedArtist)

    if len(artists) > 0:
        persist_data(artists)
        return artists

def read_artists():
    filepath = os.path.join(BASE_DIR, "artists.xlsx")
    df = pd.read_excel(filepath)
    print(df)

