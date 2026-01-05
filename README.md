# utanet-lyric-topic-discovery

## Project Structure

```
project-root/
│
├── src/
│   └── scraper/
|       └── main_scraper.py		# Entrypoint script for scraping
|       └── scrape_artists.py	# Scrape song ids from artists
|       └── scrape_lyrics.py	# Get lyrics and create dataset
|       └── utils.py			# Utilities for file handling
│   └── clustering/
|       └── main_cluster.py     # Entrypoint script for clustering
|       └── cluster.py			# Clustering with HDBSCAN and UMAP
|       └── preprocessing.py	# Tokenizer and embeddings
├── src/
│   └── raw/
|       └── artists.csv			# CSV file with artists and utanet ID
|       └── utanet.csv			# CSV file with song lyrics
│   └── processed/              # Directory for HTML cluster visualization
├── requirements.txt
├── Dockerfile
└── README.md
```

## Running

1. Build the Docker container or start up a new virtual environment and install `requirements.txt` through `pip install -r requirements.txt`

2. Run `main_cluster.py` to get clustering results. The visualization page can be seen under` data/processed/interactive_cluster.html`. 
3. If you want to add more artists or change the number of songs scraped per artist, you can look at `src/scraper/scrape_artists.py` or run `main_scraper.py` to generate a new dataset in `utanet.csv`.

