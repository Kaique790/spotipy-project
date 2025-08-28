from src.connections import get_spotify_client

def main():
    sp = get_spotify_client()
    results = sp.search(q="Coldplay", type="artist", limit=1)
    artist = results["artists"]["items"][0]
    print("Artista encontrado:", artist["name"])

if __name__ == "__main__":
    main()
