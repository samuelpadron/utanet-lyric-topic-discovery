import hdbscan
import umap.umap_ as umap
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import normalize
from sklearn.manifold import TSNE


def cluster(embeddings):
    X_norm = normalize(embeddings)
    reducer = umap.UMAP(n_neighbors=10, n_components=50, metric='cosine')
    X_reduced = reducer.fit_transform(X_norm)
    model = hdbscan.HDBSCAN(min_cluster_size=3, min_samples=2, metric='euclidean', cluster_selection_epsilon=0.05)
    labels = model.fit_predict(X_reduced)
    probs = model.probabilities_
    return labels, probs


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