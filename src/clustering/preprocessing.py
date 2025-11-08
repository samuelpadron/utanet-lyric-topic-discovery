import pandas as pd
import spacy
from sklearn.preprocessing import normalize

def load_data():
    df = pd.read_csv("data/raw/utanet.csv", sep=";")

    return df 

def make_embeddings(df, model_name="ja_ginza"):
    nlp = spacy.load(model_name)

    lyric_vectors = []
    for text in df["lyrics"]:
        doc = nlp(text)
        lyric_vectors.append(doc.vector)

    print(lyric_vectors[0].shape)


if __name__ == "__main__":
    lyrics_df = load_data()
    make_embeddings(lyrics_df)
