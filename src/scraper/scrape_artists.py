import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import os

ARTIST_BASE_URL = "https://www.uta-net.com/global/en/artist/ID/?sort=pop-d&filter=all"

artist_df = pd.read_csv("data/raw/artists.csv")
artist_df["id"] = artist_df["id"].astype(str)
artist_ids = list(artist_df["id"])