import streamlit as st
import pandas as pd
from recommender import recommend
import pickle

movies = pd.read_csv('movies.csv')

st.title("🎬 Netflix-style Movie Recommender")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie to get recommendations", movie_list)

if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
