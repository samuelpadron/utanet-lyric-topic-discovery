import pandas as pd
from bs4 import BeautifulSoup
from scraper.utils import safe_request, save_text

BASE_URL = "https://www.uta-net.com/global/en/lyric/"
OUTPUT_DIR = "data/raw"


class SongScraper:
    def __init__(self, output_dir=OUTPUT_DIR):
        self.output_dir = output_dir

    def get_song_data(self, song_id):
        html = safe_request(f"{BASE_URL}{song_id}/")
        if not html:
            return None

        soup = BeautifulSoup(html, "html.parser")
        lyrics = soup.find("div", {"id": "kashi-area"})
        lyrics = lyrics.text.replace('\n','').replace('\u3000','')
        artist = soup.find("span", {"class": "ms-2 ms-md-3 artist-name text-break d-block"})
        title = soup.find("span", {"class": "ms-2 ms-md-3 text-break d-block"})

        if lyrics and artist and title:
            return f"{title.text};{artist.text};{lyrics.strip()}"
        return None

    def scrape_songs(self, song_ids):
        for sid in song_ids:
            lyrics = self.get_song_data(sid)
            if lyrics:
                save_text(f"{self.output_dir}/utanet.csv", lyrics)
                print(f"Saved {sid}")