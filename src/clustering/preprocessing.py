import pandas as pd
import numpy as np
import spacy
import umap.umap_ as umap
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans, HDBSCAN
from sklearn.manifold import TSNE


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


if __name__ == "__main__":
    lyrics_df = load_data()
    lyric_embeddings = make_embeddings(lyrics_df)
    print(lyric_embeddings[0])
    
