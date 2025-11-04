import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import os

BASE_URL = "https://www.uta-net.com/global/en/lyric/"
OUTPUT_DIR = "data/raw"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_data(song_id):
    url = f"{BASE_URL}{song_id}/"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")
    lyrics = soup.find("div", {"id": "kashi-area"})
    artist = soup.find("span", {"class": "ms-2 ms-md-3 artist-name text-break d-block"})
    title = soup.find("span", {"class": "ms-2 ms-md-3 text-break d-block"})
    if lyrics and artist and title:
        return f"{title.text},{artist.text},{lyrics.text.strip()}"
    return None

def scrape_songs(song_ids):
    for sid in song_ids:
        lyrics = get_data(sid)
        if lyrics:
            with open(f"{OUTPUT_DIR}/{sid}.txt", "w", encoding="utf-8") as f:
                f.write(lyrics)
            print(f"Saved {sid} lyrics")
        time.sleep(1)

if __name__ == "__main__":
    song_ids = ["52857"]
    scrape_songs(song_ids)