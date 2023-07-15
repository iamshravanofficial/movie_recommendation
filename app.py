import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]    
    
    recommended_movies = []             #this loop is returning the 5 recommended movies 
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open("D:\Project\Movie Recommendation System\movie_dict.pkl",'rb'))   #imported data into movies_dict
movies = pd.DataFrame(movies_dict)      #creating two dimensional dataframe

similarity = pickle.load(open("D:\Project\Movie Recommendation System\similarity.pkl",'rb'))   #imported similar data vecto into similarity


st.title("Movies Recommendation System")

selected_movie_name = st.selectbox('Select your Movie',movies['title'].values)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)     #storing in recommendation variable
    for i in recommendation:
        st.write(i)