import hdbscan
import umap.umap_ as umap
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from preprocessing import load_nlp_model
from sklearn.preprocessing import normalize
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score
from sklearn.feature_extraction.text import TfidfVectorizer

def cluster(embeddings):
    X_norm = normalize(embeddings)
    reducer = umap.UMAP(n_neighbors=5, n_components=80, metric='cosine')
    X_reduced = reducer.fit_transform(X_norm)
    model = hdbscan.HDBSCAN(min_cluster_size=6, min_samples=5, metric='euclidean', cluster_selection_epsilon=0.05)
    labels = model.fit_predict(X_reduced)
    probs = model.probabilities_
    return labels, probs, X_reduced

def evaluate_silhouette(X_reduced, labels):
    clustered_indices = (labels != -1)
    X_clustered = X_reduced[clustered_indices]
    labels_clustered = labels[clustered_indices]

    n_clusters = len(np.unique(labels_clustered))
    
    if n_clusters >= 2:
        silhouette_avg = silhouette_score(X_clustered, labels_clustered, metric='euclidean')
        print(f"\n--- Quantitative Evaluation ---")
        print(f"Total Clustered Songs: {len(X_clustered)} / {len(X_reduced)}")
        print(f"Number of Clusters Found (excluding Noise): {n_clusters}")
        print(f"Average Silhouette Score: {silhouette_avg:.4f}")
        print(f"-------------------------------")
        return silhouette_avg
    else:
        print("\n--- Quantitative Evaluation ---")
        print("Cannot calculate Silhouette Score: Fewer than 2 clusters found (excluding noise).")
        print("-------------------------------")
        return None
    

def extract_keywords_tfidf(df, labels, tokenized_lyrics, top_n=5):
    print("\n--- Qualitative Evaluation: TF-IDF Keyword Extraction ---")
    
    tfidf_vectorizer = TfidfVectorizer(
        lowercase=True,
        norm='l2',
        max_features=2000,
        max_df=0.3
    )
    
    tfidf_matrix = tfidf_vectorizer.fit_transform(tokenized_lyrics)
    feature_names = np.array(tfidf_vectorizer.get_feature_names_out())
    
    cluster_themes = {}
    unique_clusters = sorted([c for c in np.unique(labels) if c != -1])

    for cluster_id in unique_clusters:
        cluster_indices = np.where(labels == cluster_id)[0]
        
        cluster_tfidf_sum = np.sum(tfidf_matrix[cluster_indices], axis=0).A1
        
        top_keyword_indices = np.argsort(cluster_tfidf_sum)[::-1][:top_n]
        top_keywords = [str(feature_names[i]) for i in top_keyword_indices]
        
        cluster_themes[cluster_id] = top_keywords
        print(f"Cluster {cluster_id} ({len(cluster_indices)} songs): {', '.join(top_keywords)}")

    print("---------------------------------------------------------------")
    return cluster_themes


def visualize(embeddings, labels, probs, df):

    umap_vis = umap.UMAP(
    n_neighbors=10,
    n_components=2,
    metric='euclidean'
    ) 

    embeddings = umap_vis.fit_transform(embeddings) # convert from 10D -> 2D

    labels_str = np.array(labels, dtype=str)
    labels_str[labels == -1] = "Noise"

    fig = px.scatter(
        x=embeddings[:, 0],
        y=embeddings[:, 1],
        color=labels_str,
        hover_name=df["title"],
        hover_data={
            "artist": df["artist"],
            "membership_prob": np.round(probs, 3),
        },
        title="City Pop Lyrics Clusters (GiNZA Embeddings + HDBSCAN)"
    )
    fig.update_traces(marker=dict(size=6, opacity=0.7))
    fig.update_layout(
        width=900,
        height=700,
        font=dict(family="IPAPGothic"),
        legend_title_text="Cluster"
    )
    fig.write_html("data/processed/interactive_clusters.html")