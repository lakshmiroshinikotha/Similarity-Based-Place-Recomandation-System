import pickle
import streamlit as st
import requests



def recommend(movie):
    index = place[place['Name'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
   
    for i in distances[1:6]:
         recommended_movie_names.append(place.iloc[i[0]].Name)
         
    return recommended_movie_names


st.header('Place Recommender System')
place = pickle.load(open('place_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
place_list = place['Name'].values

search =st.text_input("Search for place")
if search :
    fp=[p for p in place_list if search.lower() in p.lower()]
else:
    fp=place_list


#place_list = place['Name'].values
selected_place = st.selectbox(
    " select a Place from the dropdown",
    fp
)

if st.button('Show Recommendation'):
    recommended_movie_names= recommend(selected_place)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        
    with col2:
        st.text(recommended_movie_names[1])
        

    with col3:
        st.text(recommended_movie_names[2])
       
    with col4:
        st.text(recommended_movie_names[3])
        
    with col5:
        st.text(recommended_movie_names[4])
       


