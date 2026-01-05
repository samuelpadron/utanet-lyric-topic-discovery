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
|       └── main_cluster.py      # Entrypoint script for clustering
|       └── cluster.py			 # Clustering with HDBSCAN and UMAP
|       └── preprocessing.py	 # Tokenizer and embeddings
├── src/
│   └── raw/
|       └── artists.csv			 # CSV file with artists and utanet ID
|       └── utanet.py			 # CSV file with song lyrics
├── requirements.txt
├── Dockerfile
└── README.md
```



