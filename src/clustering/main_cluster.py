from preprocessing import load_data, make_embeddings_and_tokens, load_nlp_model
from cluster import *

if __name__ == "__main__":
    lyrics_df = load_data()
    nlp = load_nlp_model()
    lyric_embeddings, lyric_tokens = make_embeddings_and_tokens(lyrics_df, nlp)
    labels, probs, X_reduced = cluster(lyric_embeddings)
    evaluate_silhouette(X_reduced, labels)
    cluster_themes = extract_keywords_tfidf(lyrics_df, labels, lyric_tokens)
    visualize(lyric_embeddings, labels, probs, lyrics_df)