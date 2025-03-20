import streamlit as st
import pandas as pd
import pickle

# Load precomputed cosine similarity matrix
with open("cosine_sim.pkl", "rb") as f:
    cosine_sim = pickle.load(f)

# Load the movies dataset
movies = pd.read_csv("movies.csv")

# Create an index mapping movie titles to indices
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Function to get movie recommendations
def recommend_movies(title, cosine_sim=cosine_sim):
    title = title.strip().lower()
    idx = indices.get(title)

    if idx is None:
        return ["Movie not found! Try a different title."]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]

    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

# Streamlit App UI
st.title("🎬 Movie Recommendation System")
st.write("Enter a movie name, and we'll suggest 5 similar movies!")

# User input
movie_name = st.text_input("Enter movie title:", "")

if st.button("Get Recommendations"):
    if movie_name:
        recommendations = recommend_movies(movie_name)
        st.subheader("Top 5 Recommended Movies:")
        for i, rec_movie in enumerate(recommendations):
            st.write(f"{i+1}. {rec_movie}")
    else:
        st.warning("Please enter a movie title.")
