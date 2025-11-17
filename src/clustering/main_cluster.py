from preprocessing import load_data, make_embeddings
from cluster import cluster, visualize

if __name__ == "__main__":
    lyrics_df = load_data()
    lyric_embeddings = make_embeddings(lyrics_df)
    labels, probs = cluster(lyric_embeddings)
    visualize(lyric_embeddings, labels, probs, lyrics_df)