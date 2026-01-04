import pandas as pd
from bs4 import BeautifulSoup
from utils import safe_request, save_text
import re

ARTIST_BASE_URL = "https://www.uta-net.com/global/en/artist/ID/?sort=pop-d&filter=all"

def get_artist_ids():
    artist_df = pd.read_csv("data/raw/artists.csv")
    artist_df["id"] = artist_df["id"].astype(str)
    artist_ids = list(artist_df["id"])
    return artist_ids

def get_artist_song_ids(artist_ids):
    song_ids = []
    for artist_id in artist_ids:
        url = f"{ARTIST_BASE_URL.replace('ID', artist_id)}"
        html = safe_request(url)
        
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all(href=re.compile(r'\/global\/en\/lyric\/\d*\/'), limit=20)
        for a in links:
            href = a.attrs['href']
            song_id = re.sub(r'/global\/en\/lyric\/', '', href)[:-1] # Grab only the id from the href and skip the last '/'
            song_ids.append(song_id)

    return song_ids


if __name__ == "__main__":
    artist_ids = get_artist_ids()
    song_ids = get_artist_song_ids(artist_ids)
    print(song_ids)
