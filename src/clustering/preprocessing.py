import pandas as pd
import numpy as np
import spacy
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE


RANDOM_STATE = 42

def load_data():
    df = pd.read_csv("data/raw/utanet.csv", sep=";")

    return df 

def make_embeddings(df, model_name="ja_ginza"):
    nlp = spacy.load(model_name)

    lyric_embeddings = []

    for text in df["lyrics"]:
        doc = nlp(text)
        lyric_embeddings.append(doc.vector)

    return np.array(lyric_embeddings)

def cluster(embeddings):
    model = KMeans(n_clusters=5, random_state=RANDOM_STATE)
    labels = model.fit_predict(embeddings)
    return labels


def visualize(embeddings, labels, df):
    reducer = TSNE(n_components=2, random_state=RANDOM_STATE, perplexity=10)
    embeddings_2d = reducer.fit_transform(embeddings)

    plt.figure(figsize=(8,6))
    scatter = plt.scatter(embeddings_2d[:,0], embeddings_2d[:,1], c=labels, cmap="tab10")
    plt.title("City Pop Lyrics Clusters (GiNZA Embeddings)")
    plt.xlabel("t-SNE 1")
    plt.ylabel("t-SNE 2")

    legend = plt.legend(*scatter.legend_elements(), title="Cluster")
    plt.gca().add_artist(legend)

    plt.rcParams['font.family'] = 'IPAPGothic' # Allow for japanese text
    plt.rcParams['axes.unicode_minus'] = False
    for i, title in enumerate(df["title"]):
        plt.text(embeddings_2d[i, 0], embeddings_2d[i, 1], title, fontsize=8, alpha=0.7)

    plt.savefig("data/processed/cluster_plot.png", dpi=300, bbox_inches="tight")
    print("Saved figure to data/processed")

if __name__ == "__main__":
    lyrics_df = load_data()
    lyric_embeddings = make_embeddings(lyrics_df)
    labels = cluster(lyric_embeddings)
    visualize(lyric_embeddings, labels, lyrics_df)
    
