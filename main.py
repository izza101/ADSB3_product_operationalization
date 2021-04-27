from fastapi import FastAPI
import pandas as pd

app = FastAPI()
df = pd.read_csv("Movie_TMDB_API.csv", index_col = 0)

@app.get("/")
def read_root():
    subject = ["Nama : Izza Aditya Romadhoni", "NPK : 67677"]
    Analysis_link = ["analysis 1 : /MoviesWithHighestRating1", "analysis 2 : /MoviesWithHighestRating2", "analysis 3 : /HighestRatingProfit"]
    return {"user" : subject, "Analysis_link" : Analysis_link}

@app.get("/MoviesWithHighestRating1")
def read_high_rating1():
    df_ = df.loc[df['vote_count'] >= 50].sort_values(by = "vote_average", ascending = False).head(5).reset_index()
    df_ = df_.drop("index",1)
    df_ = df_['title']
    note = "Dengan batas treshold kolom vote_count lebih dari 50, 5 film dengan rating tertinggi adalah seperti terlihat pada data yang ada, data diambil dari TMDB berupa film yang rilis dari tahun 2000 sampai 2020"
    return {"MoviesWithHighestRating with VoteCount > = 50":df_, "note" : note}

@app.get("/MoviesWithHighestRating2")
def read_high_rating2():
    df_2 = df.loc[df['vote_count'] >= 1000].sort_values(by = "vote_average", ascending = False).head(5).reset_index()
    df_2 = df_2.drop("index",1)
    df_2 = df_2['title']
    note2 = "Dengan batas treshold kolom vote_count lebih dari 1000, 5 film dengan rating tertinggi adalah seperti terlihat pada data yang ada, data diambil dari TMDB berupa film yang rilis dari tahun 2000 sampai 2020"
    return {"MoviesWithHighestRating with VoteCount > = 1000":df_2, "note" : note2}

@app.get("/HighestRatingProfit")
def read_hight_profit():
    df['profit']=df['revenue']-df['budget']
    df_1 = df.sort_values(by = 'profit', ascending = False).head(5).reset_index()
    df_1 = df_1.drop("index",1)
    df_1 = df_1['title']
    note3 = "Film dengan profit tertinggi dari tahun 2000 sampai tahun 2020 terlihat pada data yang ada"
    return {"Movies With Highest Profit":df_1, "note" : note3}

