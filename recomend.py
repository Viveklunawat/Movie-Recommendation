import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder where recommend.py is
csv_path = os.path.join(BASE_DIR, "movie_recommendor.csv")

recommendation = pd.read_csv(csv_path, index_col=0)

def new_recommendation(text, count):
    reco = recommendation[text]
    recco = list(reco.sort_values(ascending=False).index)
    return recco[1:count+1]

def movie_name():
    return recommendation.index.tolist()
