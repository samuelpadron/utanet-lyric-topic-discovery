import pandas as pd
from bs4 import BeautifulSoup
from scraper.utils import safe_request, save_text
import re

ARTIST_BASE_URL = "https://www.uta-net.com/global/en/artist/ID/?sort=pop-d&filter=all"

def get_artist_df():
    artist_df = pd.read_csv("data/raw/artists.csv")
    artist_df["id"] = artist_df["id"].astype(str)
    artist_ids = list(artist_df["id"])
    return artist_ids

def get_artist_song_ids(artist_ids):
    for artist_id in artist_ids:
        url = f"{ARTIST_BASE_URL.replace('ID', artist_id)}"
        html = safe_request(url)
        
        soup = BeautifulSoup(html, "html.parser")
        song_ids = soup.find_all(href=re.compile(r'\/global\/en\/lyric\/\d*\/'))
        for song_id in song_ids:
            print(song_id.attrs['href'])


if __name__ == "__main__":
    artist_ids = get_artist_df()
    get_artist_song_ids(artist_ids)