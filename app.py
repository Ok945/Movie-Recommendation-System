import streamlit as st
import pickle
import pandas as pd
import requests
import base64












def fetch_Poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-Us'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']




def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #remove poster from api
        recommend_movies_posters.append(fetch_Poster(movie_id))
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies, recommend_movies_posters







movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))







st.title('Movie Recommender')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)






if st.button('Recommend'):
    names,posters = recommend((selected_movie_name))
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])




def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image.jpg')




def add_custom_style():
    # Define the custom CSS style
    custom_style = """
    <style>
    .css-k7vsyb.eqr7zpz1 {  
        text-align:center;  
    }
    
    
  @keyframes gradientTransition {
    0% { background-position: 0% 50%; }
    100% { background-position: 100% 50%; }
  }
  
    
    
    .css-10trblm.eqr7zpz0{
        font-size: 65px;
        top: -60px;
        position: relative;
        background: linear-gradient(to right,  #114551, #0b3818 );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientTransition 5s infinite linear;
    text-shadow: 10px 8px 20px #366160;
    }
    
    .block-container.css-1y4p8pa.e1g8pov64{
        position: relative;
    background: #d0c4c499;
    border: 2px solid #323030;
    border-radius: 10px;
    z-index: 37;
    margin-top: 30px;
    box-shadow: 0 0 10px 8px #494646;
    
    }
    
    .css-1avcm0n.e13qjvis2 {
        display : none;
    }
    
    
    
    
    .css-1dbtp3n p {
        word-break: break-word;
        margin-bottom: 0px;
        font-size: 25px;
        color: #161516;
        text-decoration: underline;
    
    }
    
    
    .css-183lzff {
    font-family: "Source Code Pro", monospace;
    white-space: pre;
    font-size: 14px;
    overflow-x: auto;
    color: black;
    /* font-size: 14px; */
    }
    
 
    
    
    </style>
    """

    # Add the custom style using st.markdown()
    st.markdown(custom_style, unsafe_allow_html=True)

# Call the function to apply the custom style
add_custom_style()
