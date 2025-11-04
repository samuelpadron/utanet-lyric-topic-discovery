from scraper.scrape_lyrics import SongScraper
from scraper.scrape_artists import get_artist_ids, get_artist_song_ids

if __name__ == "__main__":
    artist_ids = get_artist_ids()
    song_ids = get_artist_song_ids(artist_ids)
    scraper = SongScraper()
    scraper.scrape_songs(song_ids)
