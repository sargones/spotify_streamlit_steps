import streamlit as st
import pandas as pd
#from main import songs_df


st.set_page_config(page_title="Top 10 songs details", page_icon="📈")

songs_df = pd.read_csv('https://raw.githubusercontent.com/sargones/spotify_streamlit_steps/refs/heads/main/pages/songs.csv?token=GHSAT0AAAAAACZRTOVO7GIYHKKEFMM4HWZKZZCSINQ')
songs_df = songs_df.drop(columns=['id'])
songs_year = songs_df[['artist','song_name','song_album','song_release_year']]

st.title('Top 10 songs details')
st.subheader("Songs release date")
#drop_down on Band
bands = songs_year['artist'].drop_duplicates()
band = st.selectbox('Select a band', bands, index= None)
try:
  if len(band)>0:
    band_scope = songs_year['artist']==band
except:
  band_scope = songs_year['artist'].isin(list(bands))

# slider for the years
min_year = songs_year['song_release_year'].min()
max_year = songs_year['song_release_year'].max()
start_year, end_year = st.slider("Select years", min_year, max_year, (2010, 2024))

st.dataframe(songs_year[(band_scope) & ((songs_year['song_release_year']>=start_year) & (songs_year['song_release_year']<=end_year) )],
                    hide_index=True, column_config = {'song_release_year': st.column_config.NumberColumn('song_release_year', format='%d')},
                    width = 800)

st.divider()
st.subheader("Songs popularity")

popularity_df = songs_df[['artist','song_name','song_album','song_popularity']]
min_pop = popularity_df['song_popularity'].min()
max_pop = popularity_df['song_popularity'].max()


low_pop, high_pop = st.slider("Select a range", min_pop, max_pop, (min_pop + 10, max_pop - 10))

st.dataframe(popularity_df[(band_scope) & ((popularity_df['song_popularity']>=low_pop) & (popularity_df['song_popularity']<=high_pop))],
             hide_index=True, width = 800)
