{
 "cells": [
  {
   "cell_type": "code",
   
   "id": "c227de6e-9539-4909-a37b-1908c31b0e9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import pickle\n",
    "\n",
    "# Load precomputed cosine similarity matrix\n",
    "with open(\"cosine_sim.pkl\", \"rb\") as f:\n",
    "    cosine_sim = pickle.load(f)\n",
    "\n",
    "# Load the movies dataset\n",
    "movies = pd.read_csv(\"movies.csv\")\n",
    "\n",
    "# Create an index mapping movie titles to indices\n",
    "indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()\n",
    "\n",
    "# Function to get movie recommendations\n",
    "def recommend_movies(title, cosine_sim=cosine_sim):\n",
    "    title = title.strip().lower()\n",
    "    idx = indices.get(title)\n",
    "\n",
    "    if idx is None:\n",
    "        return [\"Movie not found! Try a different title.\"]\n",
    "\n",
    "    sim_scores = list(enumerate(cosine_sim[idx]))\n",
    "    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)\n",
    "    sim_scores = sim_scores[1:6]\n",
    "    \n",
    "    movie_indices = [i[0] for i in sim_scores]\n",
    "    return movies['title'].iloc[movie_indices]\n",
    "\n",
    "# Streamlit App UI\n",
    "st.title(\"🎬 Movie Recommendation System\")\n",
    "st.write(\"Enter a movie name, and we'll suggest 5 similar movies!\")\n",
    "\n",
    "# User input\n",
    "movie_name = st.text_input(\"Enter movie title:\", \"\")\n",
    "\n",
    "if st.button(\"Get Recommendations\"):\n",
    "    if movie_name:\n",
    "        recommendations = recommend_movies(movie_name)\n",
    "        st.subheader(\"Top 5 Recommended Movies:\")\n",
    "        for i, rec_movie in enumerate(recommendations):\n",
    "            st.write(f\"{i+1}. {rec_movie}\")\n",
    "    else:\n",
    "        st.warning(\"Please enter a movie title.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
