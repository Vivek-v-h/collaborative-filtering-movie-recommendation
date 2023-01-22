import streamlit as st
import pickle
import pandas as pd


allmovie_dict=pickle.load(open('allmovie_dict.pkl','rb'))
Matrix=pickle.load(open('cmll.pkl','rb'))
x=allmovie_dict.values()

def similar(movie_name,rating):
    similar_sc = Matrix[movie_name]*(rating-2.5)
    similar_sc = similar_sc.sort_values(ascending=False)
    return similar_sc

st.title('Collaborative Filtering based Movie Recomender System')

movieone=st.selectbox("Choose first movie ",x,key=1)
ratingone=st.selectbox("Rate movie",(1,2,3,4,5),key=2)
movietwo=st.selectbox("Choose second movie ",x,key=3)
ratingtwo=st.selectbox("Rate movie",(1,2,3,4,5),key=4)
moviethree=st.selectbox("Choose third movie ",x,key=5)
ratingthree=st.selectbox("Rate movie",(1,2,3,4,5),key=6)

if st.button('Recommend'):


    providedreviews = [(movieone, ratingone), (movietwo, ratingtwo), (moviethree, ratingthree)]
    similarmovie = pd.DataFrame()
    for movie, rating in providedreviews:
        similarmovie= similarmovie.append(similar(movie, rating), ignore_index=True)

    similarmovie.head(10)
    similarmovie.sum().sort_values(ascending=False).head(20)
    newlist = list(similarmovie.columns.values)
    newdict = {stu: "Passed" for stu in newlist}
    xar = newdict.keys()
    st.header('Recommended movies are')
    for i in xar:
        st.write(i, "\n");