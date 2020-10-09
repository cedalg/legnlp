import nltk
from nltk.corpus import stopwords
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import TfidfVectorizer,TfidfTransformer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def traitement(df, keywords):
    nltk.download('stopwords')
    df['décision tokénizé'] = df['décision'].apply(word_tokenize)
    stop = stopwords.words('french')
    df['décision stopwordé'] = df['décision'].apply(lambda x: ' '.join([item for item in x if item not in stop]))
    df["décision stopwordé tokénizé"] = df['décision'].apply(word_tokenize)
    df["décision stopwordé tokénizé"] = df["décision stopwordé tokénizé"].apply(lambda x: ' '.join([item for item in x if item not in stop]))
    return df

def cosine_sim(df, cas_personnel):
    count_vectorizer = CountVectorizer(stop_words='french')
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(df["décision"])
    sparse_matrix.todense()
    X = count_vectorizer.transform(df['décision'])
    com = f'{cas_personnel}'
    com_vectorizé = count_vectorizer.transform(np.array([com]))
    ligne = np.argmax(cosine_similarity(com_vectorizé,X))
    score = cosine_similarity(com_vectorizé,X).max()
    return df, ligne, score

def resultat(df, ligne, score):
    result = df['décision'].iloc[ligne]
    jp_proche = df.iloc[ligne]
    return result, jp_proche, score


















