import pandas as pd
import numpy as np
import spacy
import umap.umap_ as umap
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans, HDBSCAN
from sklearn.manifold import TSNE


POS_TO_INCLUDE = ["NOUN", "ADJ", "VERB"]
GENERAL_WORDS = {
    # Functional / Auxiliaries (Japanese)
    "ない", "いい", "いる", "する", "なる", "ある", "こと", "もの", "時", 
    "の", "どう", "そう", "これ", "それ", "ここ", "そこ", "どこ", "だめ", 
    "けど", "ため", "思う", "ゆく", "生きる", "生まれる", "好き", "違う",
    "知る", "愛する", "くれる",
    # Pronouns/Placeholders (Japanese)
    "私", "僕", "君", "貴方", "あなた", 
    # Functional / Auxiliaries / Exclamations (English)
    "the", "a", "an", "is", "are", "be", "was", "were", "and", "or", 
    "to", "in", "say", "can", "can't" "if", "with", "it", "it's", "me", "you", "your", 
    "my", "i", "baby", "come", "oh", "ah", "don", "break", "out", "of",
    "for", "do", "gonna", "but", "loveland", "they", "don't", "she",
    # Generic Theme Words (English and Japanese)
    "love", "pain", "dreamin", "girl", "boy", "today", "tomorrow", 
    "言葉", "愛", "いつも", "まま", "holy", "know", "wow", "believe", "catch",
    "we're", "get", "got", "la", "si", "yea", "see", "ever", "rain", "rainy", "ve", "how",
    "二人", "ふたり", "ドーナツ", "ピーチパイ", "そば", "どんな", "dancing", "neat"
}

def load_data():
    df = pd.read_csv("data/raw/utanet.csv", sep=";")

    return df 


def load_nlp_model(model_name="ja_ginza"):
    try:
        nlp = spacy.load(model_name)
        return nlp
    except OSError:
        print(OSError)
        return None


def make_embeddings_and_tokens(df, nlp):
    lyric_embeddings = []
    tokenized_lyrics = []
    
    for text in df["lyrics"]:
        doc = nlp(text)

        lyric_embeddings.append(doc.vector)

        tokens = []
        for sent in doc.sents:
            for token in sent:
                 if (token.pos_ in POS_TO_INCLUDE and 
                    not token.is_punct and 
                    not token.is_space and 
                    len(token.text) > 1):
                    lemma = token.lemma_.lower().strip()

                    if lemma not in GENERAL_WORDS:
                        if lemma == "love":
                            continue

                        tokens.append(lemma)
        
        tokenized_lyrics.append(" ".join(tokens)) 

    return np.array(lyric_embeddings), pd.Series(tokenized_lyrics)


if __name__ == "__main__":
    lyrics_df = load_data()
    nlp = load_nlp_model()
    lyric_embeddings,_ = make_embeddings_and_tokens(lyrics_df, nlp)
    print(lyric_embeddings[0])
    
