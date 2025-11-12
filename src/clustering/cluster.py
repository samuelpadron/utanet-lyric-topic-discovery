import umap.umap_ as umap
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans, HDBSCAN
from sklearn.manifold import TSNE


def cluster(embeddings):
    reducer = umap.UMAP(n_neighbors=10, n_components=10, metric='cosine')
    embeddings = reducer.fit_transform(embeddings)
    model = HDBSCAN(min_cluster_size=3, min_samples=2, metric='cosine', cluster_selection_epsilon=0.05)
    labels = model.fit_predict(embeddings)
    return labels


def visualize(embeddings, labels, df):

    umap_vis = umap.UMAP(
    n_neighbors=10,
    n_components=2,
    metric='cosine'
    ) 
    X_vis = umap_vis.fit_transform(embeddings) # convert from 10D -> 2D

    fig = px.scatter(
        x=embeddings[:, 0],
        y=embeddings[:, 1],
        color=labels.astype(str),
        hover_name=df["title"],
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